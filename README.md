# PBL Application

## セットアップ

仮想環境を作成していない場合は以下のコマンドで作成する。環境によっては`python3`を`python`にすると動く。

```
python3 -m venv ./venv
```

以下のコマンドで仮想環境に入る。作業する時は常に仮想環境に入ること。

Linux:
```sh
source ./venv/bin/activate  # 仮想環境に入る
```

Windows:
```sh
.\venv\bin\activate.bat  # 仮想環境に入る
```
もしくは
```sh
.\venv\bin\activate.ps1  # 仮想環境に入る
```

仮想環境に入ったら最初は必要なパッケージをインストールする。(以降は不要)

```
pip install -r requirements.txt
```

以前渡した`GOOGLE_OAUTH_CLIENT_ID`などが書かれているファイルを`.env`という名前でこのディレクトリの下に保存すること。

# アプリケーションの実行

```
flask createdb
flask run
```

# gitの使い方

<!-- gitなんもわからん -->

新しく作業を始めるときはまずmasterブランチの変更をローカルのgitに取り込む。

```sh
git pull origin master
```

新しく機能を追加/修正するときは次のようにブランチを切ること。

```sh
git branch ブランチ名
git checkout ブランチ名
```

一定の作業が終わったら、commitしたいファイルをステージングに追加する。

```sh
git add ファイル名1 ファイル名2 ...
```

次にcommitをしてaddしたファイルの変更を記録する。

```sh
git commit -m "コミットのコメント"
```

実装が完了したらリモートにpushする。

```sh
git push origin ブランチ名
```

pushしたらGitHubにアクセスし、Pull Requestを作成する。

その後、masterにmergeする。Conflict(変更の衝突)が起こった場合はGitHub上で修正するか、ローカルで修正したものをcommitしてpushする。


