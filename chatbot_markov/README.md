# otake_bot

## 環境
- macOS Catalina 10.15.2 Beta
- Python 3.6.5

## 使い方（CUI版）
```
pip3 install -r requirements.txt
```

```
$ cd engine
$ python3 bot.py
```

quitで終了

## 実行結果
```
you  :あなたの名前はなんですか？
otake_bot:俺がどうこう首突っ込むことだ、オリジナル、。
you  :あなたに会えて嬉しいです。
otake_bot:四個連続で八時間ほど、使えるます。
you  :明日は晴れます。
otake_bot:お腹すうてるから。
```

## 現在の機能
-受け取った単語に対してword2vecによる文章生成

-botの知識は語録から生成、ユーザーから受け取ったことがを知らなかった場合それを学習する

