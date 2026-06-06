# PDF To Markdown Workflow

PDFから，検証可能なMarkdown下書き，全文和訳，詳細要約を作るための標準手順。

## Purpose

このワークフローは，論文，募集要項，技術資料などのPDFを再利用可能なテキストへ変換するときに使う。

自動抽出だけで「正確な全文」とは判断しない。PDFは文字の読み順や段落構造を保持しない場合があり，二段組み，数式，表，脚注，図キャプション，ハイフネーションが崩れるためである。

## Outputs

`scripts/pdf_to_markdown.py` は次の3ファイルを生成する。

| File | Purpose |
| --- | --- |
| `<slug>_original.md` | 読み順を優先した本文。Markdown整形の土台 |
| `<slug>_layout.txt` | 紙面上の位置を保った確認用テキスト。数式，表，段組みの照合に使う |
| `<slug>_pdfinfo.txt` | タイトル，著者，ページ数，暗号化などのPDFメタデータ |

全文和訳と要約は，自動抽出後に別ファイルとして作成する。

- `<slug>_ja.md`: 全文和訳
- `<slug>_summary.md`: 問題設定，方法，結果，限界を含む詳細要約

## Requirements

Poppler utilitiesの`pdftotext`と`pdfinfo`が必要である。

```bash
command -v pdftotext
command -v pdfinfo
```

Ubuntu系で未導入の場合の一般的なパッケージ名は`poppler-utils`である。インストール操作は，実行環境の管理方針を確認してから行う。

画像だけのスキャンPDFにはOCRが必要である。OCRmyPDFはスキャンPDFへ検索可能なテキスト層を追加できる。ただし，OCR結果にも誤認識が含まれるため，原本照合を省略しない。

## Basic Usage

```bash
python3 scripts/pdf_to_markdown.py \
  path/to/paper.pdf \
  --output-dir path/to/drafts \
  --slug short-paper-name \
  --title "Paper Title"
```

既存の生成ファイルを意図的に置き換える場合だけ`--force`を付ける。

```bash
python3 scripts/pdf_to_markdown.py \
  path/to/paper.pdf \
  --output-dir path/to/drafts \
  --slug short-paper-name \
  --title "Paper Title" \
  --force
```

原本PDFは移動，リネーム，削除しない。出力先は対象領域の規則に従う。

- 雑誌会論文: `research/drafts/journal-club/`
- 院試資料: `tuat-master-exam/extracted/`
- NEDO関連論文: `nedo/drafts/`またはタスク指定先

## Extraction Procedure

### 1. 原本と利用条件を確認する

- `pdfinfo`でタイトル，著者，ページ数，暗号化の有無を確認する。
- 出版社版，著者最終稿，プレプリントのどれかを記録する。
- 全文転記や翻訳を共有する場合は，著作権とライセンスを確認する。

### 2. スクリプトを実行する

スクリプトは通常の`pdftotext`と`pdftotext -layout`を両方実行する。

- 通常抽出は文章の読み順を優先する。
- `-layout`抽出は紙面配置を優先する。
- どちらも単独では正確性を保証しない。

抽出文字数が極端に少ない場合，スクリプトはOCR候補であることを警告する。

### 3. 原文Markdownを校訂する

`<slug>_original.md`を基礎に，PDFと`<slug>_layout.txt`を照合する。

確認順序:

1. タイトル，著者，掲載誌，DOI
2. 見出しと節の順序
3. 段落の順序
4. 行末ハイフンで分断された単語
5. 数式，添字，上付き文字，ギリシャ文字，式番号
6. 表の行列対応と単位
7. 図番号とキャプション
8. 引用番号と参考文献
9. 結果に含まれる人数，平均，標準偏差，p値，性能指標

反復するページヘッダー，ページ番号，利用条件は，本文と混同しないよう除去または注記する。

### 4. 全文和訳を作る

原文の節構造を保った`<slug>_ja.md`を作る。

- 要約や解釈を混ぜず，全ての本文を対応させる。
- 数値，単位，式番号，引用番号を変更しない。
- 著者名，製品名，関数名，データセット名を勝手に訳さない。
- 専門用語の訳語を文書内で統一する。
- 参考文献は書誌誤変換を避けるため原題を保持してよい。
- 自動翻訳を使った場合も，段落ごとに原文と照合する。

### 5. 詳細要約を作る

`rules/reading-paper.txt`，`rules/paper-rules.txt`，`rules/paper-template.txt`，`rules/japanese_rules.txt`を読む。

最低限，次を記載する。

1. 論文が解こうとしている問題
2. 既存方法の限界と提案アプローチ
3. 実験参加者，条件，データ，除外条件，解析方法
4. 数学・統計手法と，成功を表す条件
5. 結果とその解釈
6. 著者が認識する期待通りの点と不足する点

著者が本文で述べた内容と，作成者による批判的評価を分ける。先行研究の著者名と年は参考文献から照合する。

### 6. 数値と構造を検査する

原文，和訳，要約の主要数値を`rg`で照合する。

```bash
rg -n "0\.049|74\.5|28\.59" \
  path/to/*_original.md \
  path/to/*_ja.md \
  path/to/*_summary.md
```

Markdownと変更状況も確認する。

```bash
git diff --check
git status --short
```

## Quality Gates

次の条件を満たすまで「正確な全文」と表現しない。

- 全ページを抽出している。
- 二段組みの左右カラムが混ざっていない。
- 数式と表をPDFで照合した。
- AbstractとResultsの数値差など，原文内部の不一致を記録した。
- 和訳の数値，引用番号，否定表現が原文と一致する。
- 要約が著者の主張と作成者の推測を区別している。

## Known Limitations

- PDF内部の文字格納順が視覚上の読み順と一致しない場合がある。
- 数式は記号，分数，添字が欠落しやすい。
- 表は列が崩れやすく，自動的なMarkdown表変換を信頼できない。
- 図の内容はテキスト抽出されない。必要ならPDF画像を目視する。
- スキャンPDFのOCRは，英数字，ギリシャ文字，数式で誤りやすい。
- `pandoc`はPDFを入力文書として正確なMarkdownへ直接変換する用途には使わない。

## Example From This Repository

2026-06-06の雑誌会候補では，次の構成で作成した。

```text
research/drafts/journal-club/
  real-time-eeg-cwm_original.md
  real-time-eeg-cwm_ja.md
  real-time-eeg-cwm_summary.md
  moving-mfssvep-ms_original.md
  moving-mfssvep-ms_ja.md
  moving-mfssvep-ms_summary.md
```

原文は読み順版を基礎にし，レイアウト抽出とPDFを用いて数式，表，段組みを確認した。和訳と要約では，主要数値と引用番号を原文へ照合した。

## References

- Poppler `pdftotext`: PDFの読み順抽出と`-layout`抽出に使用する。
- OCRmyPDF documentation: https://ocrmypdf.readthedocs.io/en/stable/
- Pandoc User's Guide: https://pandoc.org/demo/example2.html
