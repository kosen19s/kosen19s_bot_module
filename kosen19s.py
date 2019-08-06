import discord
import traceback


class Kosen:
    def __init__(self, message):
        self.message = message
        self.client = discord.Client()

    def get_id(self, mode):
        id_list = []
        dataset = []
        if mode == "c":
            dataset = self.message.guild.text_channels
        elif mode == "m":
            dataset = self.message.guild.members
        else:
            try:
                raise ValueError("Incorrect mode")
            except ValueError as e:
                traceback.print_exc(e)
        for data in dataset:
            id_list.append(data.id)
        return id_list

    def send_channel(self, client):
        channel = client.get_channel(603525315515645962)
        return channel

    def channel_judge(self, channel):
        if channel.id == 603525315515645962:
            return False
        else:
            return True
