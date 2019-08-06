Kosen19sのbot開発者のためのpythonモジュール
==
概要

kosen19sのdiscord鯖のbotをもっとかんたんにPythonで書けるようにするモジュール

## 前提ライブラリ
discord.py 1.0.1以上

## クラス呼び出し
基本的にメッセージ受け取ったときの対応を想定

    kosen = Kosen(message)

これをon_message内で呼び出して準備完了

## 実際の機能

    kosen.get_id(mode)

modeには"c"か"m"を指定してください

mode = "c"ならチャンネル、
mode = "m"ならメンバーのidのリストを返します


    kosen.send_channel(discord.Client)

bot_commandチャンネルを返します

引数のClientは最後に.runしてる変数を使ってください


    kosen.channel_judge(channel)
引数のチャンネルがbot_commandかどうか判定します


    kosen.search_kosen_from_regions(regions)
引数に地方の役職名を入れるとその地方の都道府県の役職のリストが返ってきます

    kosen.search_region_from_kosen(kosen)
引数に入れた高専が属する地方が返ってきます