ユーザは，日常のタスク管理と作業をこのリポジトリ内で行っています．ユーザが直近で抱えているタスクは tasks/ に記載されています．
タスクごとに nedo/ ，research/，tuat-master-exam/ という作業場所を設けていますので，
それぞれの中で作業を行ってください．

ユーザは作業内容の詳細や成果物の詳細を知りたいので，逐次聞くようにしてください．

## 作業開始時

- まず `tasks/active/*.md` の該当タスクを読む。
- 次に各作業場所の `status.md` と `context/source_files.md` を読む。
- 詳細な作業手順は `workflows/agent-checklist.md` を読む。
- 新しいタスク、調査、報告、ログを作る場合は `workflows/` の対応テンプレートを使う。
- 既存ファイルを移動・リネーム・削除しない。
- 文章編集や成果物作成に入る前に、必要な調査と根拠整理を行う。

## workflows の使い分け

- `workflows/agent-checklist.md`: 作業前後に必ず確認する標準手順。
- `workflows/task-template.md`: `tasks/active/` に新しいタスクを追加するときに使う。
- `workflows/research-template.md`: URL、論文、PDF などを 1 件ずつ要約するときに使う。
- `workflows/report-template.md`: 調査結果や設計方針をまとめてユーザに見せるときに使う。
- `workflows/log-template.md`: `logs/YYYY-MM-DD.md` を作成・追記するときに使う。
- `workflows/status-labels.md`: `status.md` とログの `Status` を決めるときに使う。

## 標準フロー

1. task file を読む
2. context/source files を読む
3. 不足情報を調査する
4. URL、PDF、要約を所定の場所に記録する
5. 解決方針を3案ほど提示する
6. ユーザ確認後に編集する
7. logs/YYYY-MM-DD.md を更新する
8. status.md を更新する

## 編集ルール

- コードは関数単位で編集する。
- 文章や論文は小段落単位で編集する。
- ユーザが明示的に許可するまで、確定成果物 `outputs/` は更新しない。
- 下書きは `drafts/` に置く。

## 説明方針

- 作業内容、根拠、未解決点、次に何をすべきかを日本語で説明する。
- 調査結果とエージェント自身の推測を分けて書く。
- 作業後は、ユーザに見てほしいファイル、確認してほしい判断、次に許可が必要な作業を明示する。
