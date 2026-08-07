import os
import re
import unicodedata

# Names to leave completely untouched (genuinely unrecoverable / ambiguous)
SKIP_EXACT = {
    "遨榊・",
    "髯｢隧ｦ謨ｰ蟄ｦ縺溘°繧・pdf",
    "._髯｢隧ｦ謨ｰ蟄ｦ縺溘°繧・pdf",
}

LITERAL_SUBS = [
    ("諠・ｱ謨ｰ蟄ｦ", "情報数学"),
    ("繝｢繝・ｙ繝ｫ蟆る摩", "モデル専門"),
    ("驕主悉蝠・", "過去問"),
    ("蟷ｳ謌・", "平成"),
    ("2022蟷ｴ8譛・3譌･", "2022年8月3日"),
    ("驟榊ｸ・", "配布."),
]

POST_FIXES = [
    ("コンピュータ基礁Eコンピュータ", "コンピュータ"),
    ("コンピュータ基礁E", "コンピュータ基礎"),
    ("過去啁E", "過去問"),
    ("朁E", "月"),
]


def apply_dot_sensitive(name: str) -> str:
    name = re.sub(r"蝠城｡・(?=pdf)", "問題.", name)
    name = name.replace("蝠城｡・", "問題")
    name = re.sub(r"隗｣遲・(?=pdf)", "解答.", name)
    name = name.replace("隗｣遲・", "解答")
    return name


def fix_component(name):
    if name in SKIP_EXACT:
        return name, True

    name = apply_dot_sensitive(name)
    for old, new in LITERAL_SUBS:
        name = name.replace(old, new)

    correct_runs = set(re.findall(r"[過去問題答情報数学モデル専門成年月日配布.]+", name))
    tok_map = {}
    for idx, run in enumerate(sorted(correct_runs, key=len, reverse=True)):
        if not run:
            continue
        token = "\x00%d\x00" % idx
        tok_map[token] = run
        name = name.replace(run, token)

    try:
        name = name.encode("cp932").decode("utf-8")
    except UnicodeError:
        pass
    name = unicodedata.normalize("NFC", name)

    for old, new in POST_FIXES:
        name = name.replace(old, new)

    for token, run in tok_map.items():
        name = name.replace(token, run)

    return name, False


TARGETS = [
    os.path.join("lecture_materials", "コンピュータ基礎"),
    os.path.join("lecture_materials", "情報理論"),
    os.path.join("lecture_materials", "論理回路"),
    os.path.join("past_exams", "過去問"),
]


def main():
    renamed = []
    skipped = []
    for target in TARGETS:
        for root, dirs, files in os.walk(target, topdown=False):
            for fname in files:
                new_name, was_skipped = fix_component(fname)
                if was_skipped:
                    skipped.append(os.path.join(root, fname))
                elif new_name != fname:
                    src = os.path.join(root, fname)
                    dst = os.path.join(root, new_name)
                    os.rename(src, dst)
                    renamed.append((src, dst))
            for dname in dirs:
                new_name, was_skipped = fix_component(dname)
                if was_skipped:
                    skipped.append(os.path.join(root, dname))
                elif new_name != dname:
                    src = os.path.join(root, dname)
                    dst = os.path.join(root, new_name)
                    os.rename(src, dst)
                    renamed.append((src, dst))

    with open("scratch_rename_plan.txt", "w", encoding="utf-8") as f:
        for old, new in renamed:
            f.write("%s\t->\t%s\n" % (old, new))
        f.write("\n--- SKIPPED (left untouched) ---\n")
        for s in skipped:
            f.write(s + "\n")

    print("renamed %d items, %d skipped" % (len(renamed), len(skipped)))


if __name__ == "__main__":
    main()
