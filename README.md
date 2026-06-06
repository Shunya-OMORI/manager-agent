# manager-agent

研究、提案書、受験準備をエージェントと半自動で進めるための作業リポジトリです。

## First Read

人間もエージェントも、まず次の順番で確認します。

1. `AGENTS.md`: 作業ルール
2. `tasks/active/*.md`: 現在のタスク
3. 各作業場所の `status.md`: 現在状態と次の一手
4. 各作業場所の `context/source_files.md`: 最初に読む資料
5. `workflows/`: テンプレートと作業手順

## Repository Map

```text
tasks/
  20260604.md                 # 全体タスクのマスター一覧
  inbox.md                    # 未整理の依頼置き場
  active/                     # 実行中タスク
  done/                       # 完了タスク

workflows/
  agent-checklist.md          # 標準作業フロー
  pdf-to-markdown.md          # PDF 抽出、校訂、和訳、要約の手順
  task-template.md            # タスク定義テンプレート
  research-template.md        # 調査要約テンプレート
  report-template.md          # 報告書テンプレート
  log-template.md             # 作業ログテンプレート
  status-labels.md            # 状態ラベル定義

nedo/
  context/                    # NEDO 提案書の前提資料リスト
  research/                   # URL、論文、要約
  drafts/                     # ユーザ確認前の下書き
  outputs/                    # ユーザ確認後の成果物
  logs/                       # 作業ログ
  status.md                   # 現在状態

research/
  context/                    # 卒論・雑誌会の前提資料リスト
  paper_candidates/           # 候補論文の URL、PDF、要約
  drafts/                     # ユーザ確認前の下書き
  outputs/                    # ユーザ確認後の成果物
  logs/                       # 作業ログ
  status.md                   # 現在状態

tuat-master-exam/
  context/                    # 受験資料の前提資料リスト
  sources/                    # 公式 URL、入手元、問い合わせ先
  extracted/                  # PDF から抽出したテキストや表
  plans/                      # 出願・勉強計画
  outputs/                    # ユーザ確認後の成果物
  logs/                       # 作業ログ
  status.md                   # 現在状態

scripts/
  pdf_to_markdown.py          # PDF の読み順版、レイアウト版、メタデータを抽出
```

## Standard Flow

1. `tasks/active/*.md` の該当タスクを読む。
2. `status.md` と `context/source_files.md` を読む。
3. `workflows/agent-checklist.md` を読む。
4. 必要な URL、論文、公式資料を調査する。
5. 調査結果を URL 一覧と要約ファイルに分けて保存する。
6. 解決方針や設計方針を 3 案ほど提示する。
7. ユーザ確認後に、下書きまたは成果物を編集する。
8. `logs/YYYY-MM-DD.md` を更新する。
9. `status.md` を更新する。

## Workflow Templates

作業時は、目的に合わせて `workflows/` のテンプレートを使います。

| File | Use When |
| --- | --- |
| `workflows/agent-checklist.md` | すべての作業前後に標準フローを確認する |
| `workflows/pdf-to-markdown.md` | PDF を Markdown 化し、和訳・要約まで校訂する |
| `workflows/task-template.md` | `tasks/active/` に新しいタスクを作る |
| `workflows/research-template.md` | URL、論文、PDF、公式資料を 1 件ずつ要約する |
| `workflows/report-template.md` | 調査結果、設計方針、比較案をユーザに見せる |
| `workflows/log-template.md` | `logs/YYYY-MM-DD.md` を作成・追記する |
| `workflows/status-labels.md` | `status.md` とログの `Status` を決める |

## PDF Extraction

PDFをMarkdownへ変換するときは、[PDF To Markdown Workflow](workflows/pdf-to-markdown.md)を正とします。

```bash
python3 scripts/pdf_to_markdown.py \
  path/to/source.pdf \
  --output-dir path/to/drafts \
  --slug short-name \
  --title "Document Title"
```

スクリプトの出力は未検証の下書きです。二段組み、数式、表、図キャプション、参考文献、数値をPDFと照合してから、全文和訳や要約を作成します。

## Handoff To User

作業後は、ユーザが実態を確認しやすいように次を必ず示します。

- 変更したファイル
- 追加した根拠 URL、PDF、要約
- ユーザに確認してほしい判断
- 未解決点
- 次にエージェントへ依頼できるプロンプト

## Status Labels

状態ラベルは `workflows/status-labels.md` を正とします。

- `todo`: 未着手
- `researching`: 調査中
- `waiting-user`: ユーザ確認待ち
- `drafting`: 下書き・成果物作成中
- `done`: 完了

## Naming Rules

調査要約ファイル:

- 形式: `YYYY-MM-DD_short-title.md`
- 例: `2026-06-04_react-agent-workflow.md`
- `short-title` は英小文字、数字、ハイフンのみを使う。
- 1 URL または 1 論文につき 1 要約ファイルを作る。

作業ログ:

- 形式: `logs/YYYY-MM-DD.md`
- 同日に複数回作業した場合は、同じファイルに追記する。

## Editing Rules

- 既存ファイルを移動・リネーム・削除しない。
- 確定前の文章は `drafts/` に置く。
- ユーザ確認後の成果物だけ `outputs/` に置く。
- コードは関数単位、文章や論文は小段落単位で編集する。

## Drift Prevention

ファイルの実態とユーザの認識がずれないように、次を守ります。

- 作業後に `logs/YYYY-MM-DD.md` と `status.md` を必ず更新する。
- `status.md` の `Latest Outputs` には、実在する成果物だけを書く。
- 調査結果、推測、ユーザ確認済みの判断を混ぜない。
- 参照ファイルを増やしたら `context/source_files.md` または URL 一覧にも反映する。
