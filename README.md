# PBL Application

学校の課題用リポジトリ。

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

## アプリケーションの実行

```
flask createdb
flask --debug run
```
