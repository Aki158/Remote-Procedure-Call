# Remote-Procedure-Call

## 🌱概要
クライアントとサーバで異なるプログラミング言語で書かれていても、クライアントプログラムがサーバ上の機能を呼び出せるシステム

## ✨デモ
![output](https://github.com/Aki158/Remote-Procedure-Call/assets/119317071/4c38fca7-9bf7-4395-8760-8f9bca19d9e4)

## 📝説明
このシステムは、クライアントとサーバで異なるプログラミング言語で書かれていても、クライアントプログラムがサーバ上の機能を呼び出せるシステムです。

システムの実行には、ターミナルという黒い画面にコマンドを入力します。

このシステムでは、RPCの簡易的なシステムを体験することができます。

RPCとは、ネットワークを介して別々のコンピュータ上にあるプログラム間(異なるアドレス空間)で、同一コンピュータ内(ローカル)で機能の呼び出しを行っているかのように感じさせることができるプログラミング手法です。

RPCの実装には、下記のようなプログラミング言語を使用しています。

| クライアント-サーバ | プログラミング言語 |
| ------- | ------- |
| クライアント | JavaScript(Node.js) |
| サーバ | Python |

基本的な機能として、RPCのシステム/送受信されたデータの表示ができます。

### 補足
[説明](#説明)で登場する用語について補足します。

用語の意味がわからない時は、下記表を確認してください。

| 用語 | 意味 |
| ------- | ------- |
| クライアント | サーバに接続し、データの取得や処理の依頼などを行うプログラムやコンピュータシステムのことです。 |
| サーバ | ネットワークを介してクライアントの要求に応答し、データ、サービス、リソースを提供するシステムやソフトウェアのことです。 |
| ターミナル | コンピュータに対してテキストベースのコマンド入力と出力を行うインターフェースのことです。<br>このインターフェースは、コマンドラインインターフェース（CLI）とも呼ばれます。<br>[デモ](#デモ)で表示されている黒い画面のことです。 |
| コマンド | コンピュータに対して特定の操作を実行するよう指示するテキストベースの命令です。<br>コマンドを入力することで、コンピュータは、コマンドの意味を読み取りアクションをおこします。 |
| RPC | ネットワークを介して別々のコンピュータ上にあるプログラム間(異なるアドレス空間)で、同一コンピュータ内(ローカル)で呼び出しを行っているかのように感じさせることができるプログラミング手法です。 |

## 🧰前提条件
このシステムを実行するには、下記ソフトウェアを事前にインストールしておく必要があります。

インストールされていない場合は、[インストール](#インストール)/[使用方法](#使用方法)/[使用例](#使用例)で記載されているコマンドが実行できませんので

必ずインストールしてから進めてください。

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

### Node.js
Node.jsは、JavaScript実行環境の1つです。

Node.jsのインストールについては、[UbuntuへのNode.jsのインストール](https://zenn.dev/toyonobu/articles/20230121-node-install-for-ubuntu)にわかりやすく解説してありましたので確認してください。

また、Node.jsについて詳しく知りたい場合は、[Japan Node.js Association](https://nodejs.jp/)を確認してください。

## 🍴インストール
### クローン
このシステムをあなたのPCで実行するために、クローンします。

クローンとは、このシステムの実行に必要なファイル(リポジトリのコンテンツ)をあなたのPCのローカル環境へコピーすることです。

下記手順でクローンしてください。

1. リポジトリをクローンする
```
git clone https://github.com/Aki158/Remote-Procedure-Call.git
```

2. クローンしたリポジトリへ移動する
```
cd Remote-Procedure-Call
```

## 🚀使用方法
1. 1つ目のターミナル(**サーバ用ターミナル**とする)を起動する
2. サーバ用ターミナルに下記コマンドを入力する
```
python3 server.py
```
3. 2つ目のターミナル(**クライアント用ターミナル**とする)を起動する
4. クライアント用ターミナルに下記コマンドを入力する
```
node client.py
```
5. クライアント用ターミナルに0から6までの数字を入力し送信する
6. クライアントが送信した数字をもとに、サーバ用ターミナルにデータが表示される
7. サーバ用ターミナルが関数の実行結果を送信し、クライアント用ターミナルにメッセージが表示される。

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

1. 1つ目のターミナル(**サーバ用ターミナル**とする)を起動する
2. サーバ用ターミナルに下記コマンドを入力する
```
python3 server.py
```
3. 2つ目のターミナル(**クライアント用ターミナル**とする)を起動する
4. クライアント用ターミナルに下記コマンドを入力する
```
node client.py
```
5. クライアント用ターミナルに0から6までの数字を入力し送信する。<br>0から6までの数字は、[RPCの入出力表](#RPCの入出力表)の入力部分に該当します。<br>今回は、0を入力しました。
6. クライアントが送信した数字をもとに、サーバ用ターミナルにデータが表示される。<br>入力した0に紐づくデータが表示されました。
7. サーバ用ターミナルが関数の実行結果を送信し、クライアント用ターミナルにメッセージが表示される。<br>クライアント用ターミナルに実行結果が表示されました。

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td rowspan=2>開発言語</td>
  <td>JavaScript(Node.js)</td>
</tr>
<tr>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
<tr>
  <td rowspan=2>その他</td>
  <td>Git</td>
</tr>
<tr>
  <td>Github</td>
</tr>
</table>

## 👀機能一覧
![image](https://github.com/Aki158/Remote-Procedure-Call/assets/119317071/797a7e00-d50d-496f-b248-a5f9270676d6)

| 機能 | 内容 |
| ------- | ------- |
| メッセージの表示 | 送受信されたメッセージを表示します。 |
| クライアント | ユーザーから入力された数字を受け取り、その入力と紐づくデータへ変換します。<br>その後、サーバーに送信します。<br>また、サーバからのメッセージを受信します。 |
| サーバ | クライアントからデータを受け取ります。<br>受け取ったデータをもとに、実行する関数を判断します。<br>関数の実行結果を応答としてクライアントに送り返します。 |
| エラーハンドリング | サーバが、クライアントから不適切なデータを受け取った場合は、下記のように表示します。<br>・サーバが期待している型とparam_typesが異なる場合:`Invalid parameter`<br>・methodの名前が見つからない場合:`Function not found` |

### RPCの入出力表
| 入力 | 入力に紐づくデータ | 出力 |
| ------- | ------- | ------- |
| 0 | {<br>"method":"floor",<br>"params":5.345,<br>"param_types":"double",<br>"id":0<br>} | {<br>"results": "5",<br> "result_type": "int",<br> "id": 0<br>} |
| 1 | {<br>"method":"nroot",<br>"params":[3,8],<br>"param_types":"[int,int]",<br>"id":1<br>} |{<br>"results": "2.0",<br> "result_type": "double",<br> "id": 1<br>}|
| 2 | {<br>"method":"reverse",<br>"params":"hello",<br>"param_types":"string",<br>"id":2<br>} |{<br>"results": "olleh",<br> "result_type": "str",<br> "id": 2<br>}|
| 3 | {<br>"method":"validAnagram",<br>"params":["anagram","ano grew"],<br>"param_types":"[string,string]",<br>"id":3<br>} |{<br>"results": "False",<br> "result_type": "bool",<br> "id": 3<br>}|
| 4 | {<br>"method":"sort",<br>"params":["Nice","to","meet","you"],<br>"param_types":"string[]",<br>"id":4<br>} |{<br>"results": "['Nice', 'meet', 'to', 'you']",<br> "result_type": "list",<br> "id": 4<br>}|
| 5 | {<br>"method":"floor",<br>"params":5.345,<br>"param_types":"float",<br>"id":5<br>} | Invalid parameter |
| 6 | {<br>"method":"subtract",<br>"params":[42,23],<br>"param_types":"[int,int]",<br>"id":6<br>} | Function not found |

## 📮今後の実装したいもの
- [ ] ユーザーが自由に入力できるようにする

## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)
- [Node.js v21.4.0 documentation](https://nodejs.org/api/net.html)

### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
- [UbuntuへのNode.jsのインストール](https://zenn.dev/toyonobu/articles/20230121-node-install-for-ubuntu)
- [Japan Node.js Association](https://nodejs.jp/)
