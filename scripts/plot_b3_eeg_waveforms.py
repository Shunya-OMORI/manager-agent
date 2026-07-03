from __future__ import annotations

import argparse
import json
from pathlib import Path

import mne
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw


DEFAULT_COLORS = [
    "#9448dc",
    "#2dd2e8",
    "#a6acb8",
    "#f6d64a",
    "#ec568e",
    "#4d90f5",
    "#7ed359",
    "#ff9a3e",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot b3/map raw EEG CSV waveforms as transparent PNG assets.",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("../b3/map/rawdata/RecordingS19R000_CSV"),
        help="Directory containing wert_eeg.csv and info.json.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("research/outputs/eeg-waveforms"),
        help="Directory where PNG files are written.",
    )
    parser.add_argument("--duration", type=float, default=1.0, help="Seconds to plot.")
    parser.add_argument("--start", type=float, default=19.0, help="Start time in seconds.")
    parser.add_argument("--channels", type=int, default=4, help="Number of leading EEG channels to plot.")
    parser.add_argument(
        "--picks",
        default="",
        help="Comma-separated channel names to plot. Overrides --channels when set.",
    )
    parser.add_argument("--bandpass-low", type=float, default=None, help="Optional high-pass edge in Hz.")
    parser.add_argument("--bandpass-high", type=float, default=None, help="Optional low-pass edge in Hz.")
    parser.add_argument(
        "--colors",
        default=",".join(DEFAULT_COLORS[:4]),
        help="Comma-separated CSS hex colors. Use one value, e.g. #000000, to apply it to all channels.",
    )
    parser.add_argument("--prefix", default="b3_rawdata_waveform", help="Output filename prefix.")
    parser.add_argument("--line-width", type=int, default=2, help="Line width in output pixels.")
    parser.add_argument("--amplitude-scale", type=float, default=1.0, help="Multiplier for vertical waveform amplitude.")
    parser.add_argument("--fill-below", action="store_true", help="Fill the area below each waveform.")
    parser.add_argument("--fill-color", default="#ffffff", help="Fill color used with --fill-below.")
    parser.add_argument(
        "--fill-reference",
        choices=("floor", "minimum"),
        default="floor",
        help="Fill down to a visual floor or only down to the waveform minimum.",
    )
    parser.add_argument("--flat-width", type=int, default=1700, help="Flat PNG width in pixels.")
    parser.add_argument("--flat-height", type=int, default=900, help="Flat PNG height in pixels.")
    parser.add_argument("--projected-width", type=int, default=1500, help="Projected PNG width in pixels.")
    parser.add_argument("--projected-height", type=int, default=1900, help="Projected PNG height in pixels.")
    return parser.parse_args()


def hex_to_rgba(color: str) -> tuple[int, int, int, int]:
    value = color.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected 6-digit hex color, got {color!r}")
    return (int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16), 255)


def color_list(spec: str, count: int) -> list[tuple[int, int, int, int]]:
    colors = [hex_to_rgba(item) for item in spec.split(",") if item.strip()]
    if not colors:
        colors = [hex_to_rgba(DEFAULT_COLORS[0])]
    if len(colors) == 1:
        return colors * count
    if len(colors) < count:
        raise ValueError(f"Need at least {count} colors or exactly one shared color.")
    return colors[:count]


def load_raw(raw_dir: Path, channel_count: int, picks: str = "") -> tuple[mne.io.RawArray, list[str]]:
    info_path = raw_dir / "info.json"
    csv_path = raw_dir / "wert_eeg.csv"
    with info_path.open(encoding="utf-8") as handle:
        info_json = json.load(handle)
    eeg_info = next(signal for signal in info_json["signals"] if signal["id"] == "wert_eeg")
    sfreq = float(eeg_info["sampling_rate"])
    all_labels = list(eeg_info["signal_loc"])
    if picks.strip():
        requested = [item.strip() for item in picks.split(",") if item.strip()]
        missing = [label for label in requested if label not in all_labels]
        if missing:
            raise ValueError(f"Unknown channel(s): {missing}; available={all_labels}")
        channel_labels = requested
    else:
        channel_labels = all_labels[:channel_count]
    columns = [f"ch{all_labels.index(label) + 1}-{label}" for label in channel_labels]

    frame = pd.read_csv(csv_path, usecols=columns)
    values = frame.to_numpy(dtype=float).T
    scale_to_uv = 1e-3 if float(np.median(np.abs(values))) > 1000.0 else 1.0
    data_uv = values * scale_to_uv

    info = mne.create_info(ch_names=channel_labels, sfreq=sfreq, ch_types="eeg")
    raw = mne.io.RawArray(data_uv * 1e-6, info, verbose=False)
    return raw, channel_labels


def normalized_crop(
    raw: mne.io.RawArray,
    channels: list[str],
    start: float,
    duration: float,
    bandpass_low: float | None,
    bandpass_high: float | None,
) -> tuple[np.ndarray, np.ndarray]:
    sample_count = int(round(duration * float(raw.info["sfreq"])))
    crop = raw.copy().crop(tmin=start, tmax=start + (sample_count - 1) / float(raw.info["sfreq"]), include_tmax=True)
    if bandpass_low is not None or bandpass_high is not None:
        crop.load_data()
        crop.filter(
            l_freq=bandpass_low,
            h_freq=bandpass_high,
            picks=channels,
            method="iir",
            verbose=False,
        )
    data_uv = crop.get_data(picks=channels) * 1e6
    times = np.arange(data_uv.shape[1], dtype=float) / float(raw.info["sfreq"])
    centered = data_uv - np.median(data_uv, axis=1, keepdims=True)
    scales = np.percentile(np.abs(centered), 99.0, axis=1)
    scales = np.where(scales <= 1e-9, np.max(np.abs(centered), axis=1), scales)
    scales = np.where(scales <= 1e-9, 1.0, scales)
    return times, np.clip(centered / scales[:, None], -1.0, 1.0)


def save_flat(
    path: Path,
    times: np.ndarray,
    values: np.ndarray,
    colors: list[tuple[int, int, int, int]],
    duration: float,
    width: int,
    height: int,
    line_width: int,
    fill_below: bool,
    fill_color: tuple[int, int, int, int],
    amplitude_scale: float,
    fill_reference: str,
) -> None:
    scale = 3
    image = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    left, right = 70, width - 70
    if values.shape[0] == 1:
        baselines = np.array([height / 2])
        amplitude = int(height * 0.32 * amplitude_scale)
    else:
        baselines = np.linspace(150, height - 150, values.shape[0])
        amplitude = max(24, int(height / (values.shape[0] * 3.2) * amplitude_scale))
    for channel_index in range(values.shape[0]):
        coords = []
        floor_coords = []
        min_value = float(np.min(values[channel_index]))
        for time_value, sample_value in zip(times, values[channel_index]):
            x = (left + (right - left) * (float(time_value) / duration)) * scale
            y = (baselines[channel_index] - amplitude * float(sample_value)) * scale
            coords.append((x, y))
            floor_y = (
                baselines[channel_index] - amplitude * min_value
                if fill_reference == "minimum"
                else baselines[channel_index] + amplitude * 1.25
            )
            floor_coords.append((x, floor_y * scale))
        if fill_below:
            draw.polygon(coords + list(reversed(floor_coords)), fill=fill_color)
        draw.line(coords, fill=colors[channel_index], width=line_width * scale)
    image.resize((width, height), Image.Resampling.LANCZOS).save(path)


def save_projected(
    path: Path,
    times: np.ndarray,
    values: np.ndarray,
    colors: list[tuple[int, int, int, int]],
    duration: float,
    width: int,
    height: int,
    line_width: int,
    fill_below: bool,
    fill_color: tuple[int, int, int, int],
    amplitude_scale: float,
    fill_reference: str,
) -> None:
    scale = 3
    image = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    base_x = int(width * 0.24)
    base_y = int(height * 0.79)
    run = int(min(width * 0.55, height * 0.55))
    channel_gap = max(34, int(height * 0.048))
    amplitude = max(28, int(channel_gap * 0.78 * amplitude_scale))
    for channel_index in range(values.shape[0]):
        coords = []
        floor_coords = []
        min_value = float(np.min(values[channel_index]))
        for time_value, sample_value in zip(times, values[channel_index]):
            ratio = float(time_value) / duration
            x = (base_x + run * ratio) * scale
            baseline_y = base_y - run * ratio + channel_index * channel_gap
            y = (baseline_y - amplitude * float(sample_value)) * scale
            coords.append((x, y))
            floor_y = (
                baseline_y - amplitude * min_value
                if fill_reference == "minimum"
                else baseline_y + amplitude * 1.25
            )
            floor_coords.append((x, floor_y * scale))
        if fill_below:
            draw.polygon(coords + list(reversed(floor_coords)), fill=fill_color)
        draw.line(coords, fill=colors[channel_index], width=line_width * scale)
    image.resize((width, height), Image.Resampling.LANCZOS).save(path)


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    raw, channels = load_raw(args.raw_dir, args.channels, args.picks)
    times, values = normalized_crop(
        raw,
        channels,
        args.start,
        args.duration,
        args.bandpass_low,
        args.bandpass_high,
    )
    colors = color_list(args.colors, len(channels))
    fill_color = hex_to_rgba(args.fill_color)

    duration_label = f"{args.duration:g}s".replace(".", "p")
    flat_path = args.output_dir / f"{args.prefix}_{len(channels)}electrodes_{duration_label}.png"
    projected_path = args.output_dir / f"{args.prefix}_{len(channels)}electrodes_{duration_label}_projected45.png"
    save_flat(
        flat_path,
        times,
        values,
        colors,
        args.duration,
        args.flat_width,
        args.flat_height,
        args.line_width,
        args.fill_below,
        fill_color,
        args.amplitude_scale,
        args.fill_reference,
    )
    save_projected(
        projected_path,
        times,
        values,
        colors,
        args.duration,
        args.projected_width,
        args.projected_height,
        args.line_width,
        args.fill_below,
        fill_color,
        args.amplitude_scale,
        args.fill_reference,
    )
    print(f"raw={raw}")
    print(f"channels={channels}")
    print(f"flat={flat_path.resolve()}")
    print(f"projected={projected_path.resolve()}")


if __name__ == "__main__":
    main()
