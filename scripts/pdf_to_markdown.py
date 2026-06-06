#!/usr/bin/env python3
"""Create a reviewable Markdown/text extraction bundle from a PDF."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


MIN_USEFUL_CHARACTERS = 200


@dataclass(frozen=True)
class OutputPaths:
    markdown: Path
    layout: Path
    metadata: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract a PDF into reading-order Markdown, layout-preserving text, "
            "and PDF metadata. The output is a review draft, not a verified "
            "transcription."
        )
    )
    parser.add_argument("pdf", type=Path, help="source PDF")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        required=True,
        help="directory for generated files",
    )
    parser.add_argument(
        "--slug",
        help="safe output filename stem; defaults to a sanitized PDF stem",
    )
    parser.add_argument(
        "--title",
        help="Markdown title; defaults to the PDF filename stem",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing generated files",
    )
    return parser.parse_args()


def require_command(command: str) -> None:
    if shutil.which(command) is None:
        raise RuntimeError(
            f"required command not found: {command}. "
            "Install Poppler utilities before running this script."
        )


def validate_source(pdf: Path) -> Path:
    source = pdf.expanduser().resolve()
    if not source.is_file():
        raise ValueError(f"PDF does not exist: {source}")
    if source.suffix.lower() != ".pdf":
        raise ValueError(f"input must have a .pdf extension: {source}")
    return source


def validate_slug(slug: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", slug):
        raise ValueError(
            "slug may contain only letters, numbers, dots, underscores, "
            f"and hyphens: {slug}"
        )
    if slug in {".", ".."}:
        raise ValueError(f"invalid slug: {slug}")
    return slug


def default_slug(source: Path) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", source.stem).strip("-._")
    return slug or "document"


def output_paths(output_dir: Path, slug: str) -> OutputPaths:
    directory = output_dir.expanduser().resolve()
    return OutputPaths(
        markdown=directory / f"{slug}_original.md",
        layout=directory / f"{slug}_layout.txt",
        metadata=directory / f"{slug}_pdfinfo.txt",
    )


def check_overwrite(paths: OutputPaths, force: bool) -> None:
    existing = [path for path in paths.__dict__.values() if path.exists()]
    if existing and not force:
        formatted = "\n".join(f"- {path}" for path in existing)
        raise FileExistsError(
            "generated file already exists; use --force to overwrite:\n"
            f"{formatted}"
        )


def run_command(arguments: list[str]) -> str:
    completed = subprocess.run(
        arguments,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return completed.stdout


def extract_text(pdf: Path, preserve_layout: bool) -> str:
    arguments = ["pdftotext"]
    if preserve_layout:
        arguments.append("-layout")
    arguments.extend(["-enc", "UTF-8", str(pdf), "-"])
    return run_command(arguments).replace("\r\n", "\n")


def extract_metadata(pdf: Path) -> str:
    return run_command(["pdfinfo", str(pdf)]).replace("\r\n", "\n")


def markdown_header(title: str, source: Path) -> str:
    return (
        f"# {title}\n\n"
        f"- Source PDF: `{source}`\n"
        "- Extraction: `pdftotext` reading-order text\n"
        "- Verification status: unverified draft\n\n"
        "> This file is an extraction aid. Check headings, paragraph order, "
        "hyphenation, equations, tables, figure captions, references, and "
        "numeric values against the PDF before treating it as accurate.\n\n"
        "---\n\n"
    )


def non_whitespace_characters(text: str) -> int:
    return sum(not character.isspace() for character in text)


def write_outputs(
    paths: OutputPaths,
    title: str,
    source: Path,
    reading_order: str,
    layout: str,
    metadata: str,
) -> None:
    paths.markdown.parent.mkdir(parents=True, exist_ok=True)
    paths.markdown.write_text(
        markdown_header(title, source) + reading_order,
        encoding="utf-8",
    )
    paths.layout.write_text(layout, encoding="utf-8")
    paths.metadata.write_text(metadata, encoding="utf-8")


def print_report(paths: OutputPaths, character_count: int) -> None:
    print(f"Extracted non-whitespace characters: {character_count}")
    print(f"Reading-order Markdown: {paths.markdown}")
    print(f"Layout review text: {paths.layout}")
    print(f"PDF metadata: {paths.metadata}")
    if character_count < MIN_USEFUL_CHARACTERS:
        print(
            "WARNING: very little text was extracted. The PDF may be scanned, "
            "image-only, protected, or malformed. Run OCR first and retry.",
            file=sys.stderr,
        )
    print(
        "Next: compare the reading-order file with the layout file and PDF, "
        "then manually restore Markdown structure."
    )


def main() -> int:
    args = parse_args()
    try:
        require_command("pdftotext")
        require_command("pdfinfo")
        source = validate_source(args.pdf)
        slug = validate_slug(args.slug) if args.slug else default_slug(source)
        title = args.title or source.stem.replace("_", " ")
        paths = output_paths(args.output_dir, slug)
        check_overwrite(paths, args.force)

        reading_order = extract_text(source, preserve_layout=False)
        layout = extract_text(source, preserve_layout=True)
        metadata = extract_metadata(source)
        write_outputs(paths, title, source, reading_order, layout, metadata)
        print_report(paths, non_whitespace_characters(reading_order))
        return 0
    except (
        FileExistsError,
        RuntimeError,
        ValueError,
        subprocess.CalledProcessError,
        OSError,
    ) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
