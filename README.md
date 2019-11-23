# mtsBattler

社内イベント用の対戦アプリ

## Features

* ステータス自動生成（氏名判断？）
* ターン制バトル

## For Developers

1. 「Docker」と「Docker-Compose」をインストール

2. このリポジトリをクローン

3. 「docker-compose.yml」があるディレクトリで下記を実行

   ```
   docker-compose build
   docker-compose up -d
   ```

4. 下記へアクセスし画面が表示されればOK

   ```
   http://localhost/test
   ```

5. Dockerを停止するには下記を実行

   ```
   docker-compose down
   ```

### vagrant

Windows で Hyper-v を有効にしない場合は vagrant 上にDockerを入れて開発する。
vagrant/Vagrantfile を使って `vagrant up` すれば「Docker」「Docker-Compose」が入ったVM（Centos 8）が立てられる。