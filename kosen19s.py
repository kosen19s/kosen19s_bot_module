import discord
import traceback


class Kosen:
    def __init__(self, message):
        self.message = message
        self.client = discord.Client()
        # 順番は北海道:[旭川, 釧路, 苫小牧, 函館]
        # 東北:[八戸, 一関, 仙台, 秋田, 鶴岡, 福島]
        # 関東:[茨城,小山,群馬,木更津, 東京, 東京都立, サレジオ]
        # 中部:[長岡, 富山, 石川, 国際, 福井, 長野, 岐阜, 沼津, 豊田]
        # 近畿:[鳥羽, 鈴鹿, 近畿, 舞鶴, 大阪, 明石, 神戸, 奈良, 和歌山]
        # 中国:[米子, 松江, 津山, 広島, 呉, 徳山, 宇部, 大島]
        # 四国:[阿南, 香川, 新居浜, 弓削, 高知(なんか無い]
        # 九州・沖縄:[北九州, 久留米, 有明, 佐世保, 熊本, 大分, 都城, 鹿児島, 沖縄]
        self.region_kosen = {604207176092876830:[603505471827083265, 603505471852380173, 603505472074547221,
                                                 603505474293202974],
                             604207302907527190:[603505471684476929, 603505457801199616, 603506204983164928,
                                                 603506322956353536, 603506394838335489, 603506439125860412],
                             604207349149859871:[603506506255826945, 603506538740449300, 603506570642325504,
                                                 603506680973492254, 603506849152499739, 603506901774499870,
                                                 603506947102212096],
                             604207385254428689:[603507015289143312, 603507052064669696, 603507084528451596,
                                                 603507127889428492, 603507197283926026, 603507232889634816,
                                                 603507266334752769, 603507311092301827, 603507449286361089],
                             604208047103016962:[603507489392295963, 603507558094864394, 603507593587195905,
                                                 603507657264857098, 603507696733257738, 603507760243408906,
                                                 603507792955047938, 603507829055422464, 603507884994723852],
                             604208105932193798:[603507918574452747, 603508037906464801, 603508081015652362,
                                                 603508116323303444, 603508165354455050, 603508242710265866,
                                                 603508278772891654, 603508311677075466],
                             604208148038811648:[603508372171653120, 603508459635212299, 603508498428329984,
                                                 603508587909742623],
                             604208190233509898:[603508621585940490, 603508654674542603, 603508736342097920,
                                                 603508886133014528, 603508925479911434, 603508960900808745,
                                                 603509027049177099, 603509072716890133, 603509125380308993]}
        self.gender = {"man" : 604212899270885386, "woman" : 604231080043872256}

    def get_id_list(self, mode):
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

    def search_kosen_from_regions(self, region, id=False):
        if id:
            region_id = region
        else:
            region_role = discord.utils.get(self.message.guild.roles, name=region)
            region_id = region_role.id
        region_kosen_ids = self.region_kosen[region_id]
        region_kosen_list = []
        for region_kosen_id in region_kosen_ids:
           region_kosen_list.append(discord.utils.get(self.message.guild.roles, id=region_kosen_id))
        return region_kosen_list

    def search_region_from_kosen(self, kosen, id=False):
        if id:
            kosen_id = kosen
        else:
            kosen_id = discord.utils.get(self.message.guild.roles, name=kosen).id
        for region, kosen_search in self.region_kosen.items():
            if kosen_id in kosen_search:
                region_id = region
        return discord.utils.get(self.message.guild.roles, id=region_id)

    def search_member_from_role(self, role, id=False):
        member_list = []
        members = self.message.guild.members
        if id:
            for member in members:
                mem_roles = member.roles
                for roles in mem_roles:
                    if str(roles.id) == role:
                        member_list.append(member)
                        break
        else:
            for member in members:
                mem_roles = member.roles
                for roles in mem_roles:
                    if str(roles.name) == role:
                        member_list.append(member)
                        break
        return member_list

    def get_id(self, mode, name):
        if mode == "m":
            return discord.utils.find(lambda m: m.name == name, self.message.guild.members)
        elif mode == "c":
            return discord.utils.find(lambda m: m.name == name, self.message.guild.text_channels)
        elif mode == "r":
            return discord.utils.find(lambda m: m.name == name, self.message.guild.roles)
        else:
            try:
                raise ValueError("mode is m, c or r")
            except ValueError as e:
                traceback.print_exc(e)

    def get_roles_dict(self):
        roles_list = []
        roles_raw_list = self.message.guild.roles
        for roles in roles_raw_list:
            raw_dict = {}
            raw_dict["name"] = roles.name
            raw_dict["id"] = roles.id
            roles_list.append(raw_dict)
        return roles_list

    def judge_gender(self, name, id=False):
        if id:
            user = discord.utils.find(lambda m:m.id == name, self.message.guild.members)
        else:
            user = discord.utils.find(lambda m:m.name == name, self.message.guild.members)
            if user == None:
                try:
                    raise ValueError('member "{0}" is not exist'.format(name))
                except ValueError as e:
                    traceback.print_exc(e)
        print(user)
        roles = user.roles
        for role in roles:
            if role.id in list(self.gender.values()):
                if role.id == self.gender["man"]:
                    return "man"
                elif role.id == self.gender["woman"]:
                    return "woman"
        return "undefined"
