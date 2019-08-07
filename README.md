Kosen19sのbot開発者のためのpythonモジュール
==
概要

kosen19sのdiscord鯖のbotをもっとかんたんにPythonで書けるようにするモジュール

## 前提ライブラリ
discord.py 1.0.1以上

## クラス呼び出し
基本的にメッセージ受け取ったときの対応を想定
    
    from kosen19s import Kosen
    import discord
    
    client = discord.Client()
    
    @event.client
    async def on_message(message):
        kosen = Kosen(message)

こう呼び出して準備完了

## 実際の機能

    kosen.get_id_list(mode)

modeには"c"か"m"を指定してください

mode = "c"ならチャンネル、
mode = "m"ならメンバーのidのリストを返します


    kosen.send_channel(discord.Client)

bot_commandチャンネルを返します

引数のClientは最後に.runしてる変数を使ってください


    kosen.channel_judge(channel)
引数のチャンネルがbot_commandかどうか判定します


    kosen.search_kosen_from_regions(regions, id=False)
引数に地方の役職名を入れるとその地方の都道府県の役職のリストが返ってきます
idがTrueの場合、役職名の代わりに役職idを使用します

    kosen.search_region_from_kosen(kosen, id=False)
引数に入れた高専が属する地方が返ってきます
idがTrueの場合、役職のidを使用します

    kosen.search_member_from__role(role, id=False)
引数に入れた名前の役職を持っているメンバーのリストを返します
idがTrueの場合、役職のidを引数として利用します

    kosen.get_id(mode, name)
nameに入れた名前のオブジェクトのidを取得します
modeにm, c, rのいずれかを代入します

    m = メンバー
    c = テキストチャンネル
    r = 役職