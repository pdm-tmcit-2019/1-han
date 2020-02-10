# otake_bot

## 環境
- macOS Catalina 10.15.2 Beta
- Python 3.6.5

## 使い方（CUI版）
```
pip3 install -r requirements.txt
```
### 初めにwebサーバーを立ち上げる
※webServerに移動してから実行しないとエラーが起こる
```
$ cd engine/webServer/
$ python3 SimpleHttpServer.py
```
その後、実行
```
$ python3 engine/bot.py
$ python3 engine/vote.py
```


## 実行結果(bot.py)
jsonldに記述されている値とそれに対する応答が表示される。出力されるjsonldファイルは"engin/jsonld_rerurn/chat_return.jsonld"を参照。
```
それで、あなたは人狼が誰だと思うの？

私はパメラが人狼だと思う。
otake_bot:広告が出るますた見るますたっていう。
```
## 実行結果(vote.py)
データを取得する際に使用したRDFと、ランダムで決定した投票する相手が表示される。出力されるjsonldファイルは"engin/jsonld_rerurn/noonVote_return.jsonld"を参照。
```
https://licos.online/state/0.3/village#3/character#13
Pamela
パメラ
```
