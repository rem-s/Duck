# Duck
Projekt Duck<br>
### Duck the Karugamo projekt

部員向けにGitコマンドのチートシートを置いておく。(部長の個人的なメモ)

## git cmd ch sh
### クローンする&ブランチに入る
`git clone [URL_REPO_REMOTE]`

`cd [NAME_REPO]`
### チェックアウト
`git checkout [NAME_BRANCH]`
### ブランチの新規作成
`git branch [NAME_BRANCH_NEU]`
### リモートブランチの削除
`git push --delete origin [NAME_BRANCH_REMOTE]`
### ローカルブランチの削除
`git branch -D [NAME_BRANCH_LOCAL]`
### すでにGitHub上にあるブランチにチェックアウトする
`git checkout -b [NAME_BRANCH_LOCAL] origin/[NAME_BRANCH_REMOTE]`
### ブランチ名の変更
`git branch -m [NAME_BRANCH_OLD] [NAME_BRANCH_NEU]`

`リモートの[NAME_BRANCH_OLD]を削除`

`[NAME_BRANCH_NEU]をプッシュ`
