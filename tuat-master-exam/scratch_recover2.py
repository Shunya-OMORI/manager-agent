import os

base = os.path.join("past_exams", "過去問")
lines = []
for root, dirs, files in os.walk(base):
    for name in sorted(dirs) + sorted(files):
        try:
            fixed = name.encode("cp932").decode("utf-8")
            status = "OK"
        except Exception as e:
            fixed = name
            status = f"ERR {e}"
        rel = os.path.join(root, name)
        lines.append(f"{status}\t{rel}\t=>\t{fixed}")

with open("scratch_pastexams.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
