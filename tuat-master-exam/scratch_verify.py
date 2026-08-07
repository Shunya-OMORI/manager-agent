import os

target_dir = os.path.join("past_exams", "過去問", "過去問専門科目", "H25")
lines = []

for f in os.listdir(target_dir):
    if "驕主悉蝠柔" in f:
        lines.append(f"actual on-disk name: {f!r}")
        # isolate exactly the still-garbled middle segment
        start = f.index("驕主悉蝠柔")
        end = f.index("隗｣隱ｬ")
        segment = f[start:end]
        lines.append(f"segment={segment!r}")
        try:
            d = segment.encode("cp932").decode("utf-8")
            lines.append(f"segment decoded={d!r}")
        except UnicodeError as e:
            lines.append(f"segment ERROR: {e}")

        # try decoding the segment plus tail together
        tail = f[start:]
        try:
            d2 = tail.encode("cp932").decode("utf-8")
            lines.append(f"segment+tail decoded={d2!r}")
        except UnicodeError as e:
            lines.append(f"segment+tail ERROR: {e}")

with open("scratch_verify_out.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
