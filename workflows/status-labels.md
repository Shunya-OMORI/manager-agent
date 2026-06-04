# Status Labels

`status.md` と `logs/YYYY-MM-DD.md` の `Status` は、次のいずれかに固定する。

| Label | Meaning | Use When |
| --- | --- | --- |
| `todo` | 未着手 | タスクはあるが、まだ調査や作業を始めていない |
| `researching` | 調査中 | URL、論文、PDF、公式情報を集めている |
| `waiting-user` | ユーザ確認待ち | 方針、候補、本文案などの判断待ち |
| `drafting` | 下書き・成果物作成中 | ユーザ確認済みの方針に沿って drafts や outputs を作っている |
| `done` | 完了 | 成果物、ログ、status 更新が完了している |

## Rules

- 1 つの `status.md` には、現在の代表状態を 1 つだけ書く。
- 判断待ちがある場合は、作業途中でも `waiting-user` を優先する。
- 完了時は `Latest Outputs` に成果物パスを書く。

