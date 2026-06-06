# Agent Checklist

このリポジトリでエージェントが作業する時の標準手順。

1. `tasks/active/*.md` を読む。
2. タスクに書かれた `Required Inputs` と `Working Directories` を確認する。
3. `context/` と既存資料を読む。
4. ネットワーク上の事例、関連論文、公式情報を調査する。
5. PDFを抽出する場合は、`workflows/pdf-to-markdown.md`に従い、読み順版とレイアウト確認版を作る。
6. URL、PDF、要約を所定の evidence ディレクトリに分けて記録する。
7. 解決策や実現方法を 3 案ほど提示する。
8. ユーザ確認を受けてから編集する。
9. コードは関数単位、文章や論文は小段落単位で編集する。
10. `logs/YYYY-MM-DD.md` に作業内容、根拠、未解決点、次の依頼文を残す。
11. `status.md` を更新する。
12. 最終回答で、ユーザに見てほしいファイル、確認してほしい判断、未解決点、次に使える依頼文を示す。

テンプレートの使い分け:

- `task-template.md`: 新しいタスクを作る時。
- `research-template.md`: URL、論文、PDF、公式資料を 1 件ずつ要約する時。
- `pdf-to-markdown.md`: PDF本文を抽出し、校訂、和訳、詳細要約を作る時。
- `report-template.md`: 調査結果や設計方針を人間に見せる時。
- `log-template.md`: 作業ログを書く時。
- `status-labels.md`: 状態ラベルを決める時。

状態ラベル:

- `todo`: 未着手
- `researching`: 調査中
- `waiting-user`: ユーザ確認待ち
- `drafting`: 下書き・成果物作成中
- `done`: 完了

調査要約の命名:

- `YYYY-MM-DD_short-title.md`
- 1 URL または 1 論文につき 1 要約ファイル

禁止事項:

- 明示許可なしに既存ファイルを移動・リネーム・削除しない。
- 根拠のない市場規模、論文品質、出願締切を確定情報として書かない。
- 調査と要約を成果物本文に混ぜない。

作業後の確認:

- `git status --short` で変更ファイルを確認する。
- `rg --files` または対象ディレクトリの一覧で、参照しているファイルが実在するか確認する。
- `status.md` の状態と実際の成果物が食い違っていないか確認する。
