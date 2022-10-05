from main import *
import re
filename = settings['Adm']
class main(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        global log
        global laststr
        global filename
        async def massage():
            global b
            types = b['type']
            if types == 'chat' and settings['chaChat'] != 0:
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                message = b['message']
                time = b['Time']
                channel = bot.get_channel(settings['chaChat'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Chat ", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Message: \n{message}", value=time, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/2Pd43QD/15456017791607043058-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed)

            elif types == 'disconnection' and settings['chaConnect'] != 0:
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                time = b['Time']
                channel = bot.get_channel(settings['chaConnect'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Disconnection", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/VjR3r0b/7428511111582779214-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed)

            elif types == 'connection' and settings['chaConnect'] != 0:
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                time = b['Time']
                channel = bot.get_channel(settings['chaConnect'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Disconnection", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/3m0PSRP/10259377741543238901-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'dugin'and settings['chaDug'] != 0:
                obj = b['obj']
                stashсord = b['stashсord']
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                time = b['Time']
                channel = bot.get_channel(settings['chaDug'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Dugin", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=True)
                embed.add_field(name=f"Обьект: {obj}", value=stashсord, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/Xx9xDZ2/6938934591586787943-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'dugout' and settings['chaDug'] != 0:
                obj = b['obj']
                stashсord = b['stashсord']
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                time = b['Time']
                channel = bot.get_channel(settings['chaDug'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Dugout", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=True)
                embed.add_field(name=f"Обьект: {obj}", value=stashсord, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/S3hbNms/9902357741586787813-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) #suicide
            elif types == 'suicide' and settings['chaSuicid'] != 0:
                types = b['type']
                player = b['Name']
                playerid = b['Id']
                time = b['Time']
                channel = bot.get_channel(settings['chaSuicid'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Suicide", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/V9ZSLSz/8466646871637903641-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed)  

            elif types == 'unconscious' and settings['chaUncunsion'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                channel = bot.get_channel(settings['chaUncunsion'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Unconscious", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/Dks0sXN/18714323811622193854-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'conscious' and settings['chaUncunsion'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                channel = bot.get_channel(settings['chaUncunsion'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Conscious", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/B6N6CHk/8671494731632934035-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'bleed' and settings['chaBled'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                channel = bot.get_channel(settings['chaBled'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="bleed", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=True)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/B6N6CHk/8671494731632934035-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) #build

            elif types == 'build' and settings['chaBuild'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                Object = b['Object']
                Tool = b['Tool']
                channel = bot.get_channel(settings['chaBuild'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Build", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=False)
                embed.add_field(name=f"Инструмент:", value=Tool, inline=False)
                embed.add_field(name=f"Обьект:", value=Object, inline=False)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/chfkZtH/16265679131556258229-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'dismant' and settings['chaBuild'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                Object = b['Object']
                Tool = b['Tool']
                channel = bot.get_channel(settings['chaBuild'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Dismant", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=False)
                embed.add_field(name=f"Инструмент:", value=Tool, inline=False)
                embed.add_field(name=f"Обьект:", value=Object, inline=False)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/v4vnkQg/11586182731619968006-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 
            
            elif types == 'place' and settings['chaPlace'] != 0:
                player = b['Name']
                playerid = b['Id']
                pos = b['Pos']
                time = b['Time']
                Object = b['Object']
                channel = bot.get_channel(settings['chaPlace'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Place", value="Server None", inline=False)
                embed.add_field(name=f"Player: {player}", value=f"id: {playerid}", inline=False)
                embed.add_field(name=f"Время:", value=time, inline=False)
                embed.add_field(name=f"Позиция:", value=pos, inline=False)
                embed.add_field(name=f"Обьект:", value=Object, inline=False)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/chfkZtH/16265679131556258229-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 

            elif types == 'killtype' and settings['chaKill'] != 0:
                killedName =b['killedName']
                killedId = b['killedId']
                killerName =b['killerName']
                killerId =b['killerId']
                killedPos =b['killedPos']
                weapon = b['weapon']
                distance = b['distance']
                Time = b['Time']
                channel = bot.get_channel(settings['chaKill'])
                embed=nextcord.Embed(color=0x00fbff)
                embed.add_field(name="Killtype", value="Server None", inline=False)
                embed.add_field(name=f"KillerName: {killerName}", value=f"id: {killerId}", inline=False)
                embed.add_field(name=f"killedName: {killedName}", value=f"id: {killedId}", inline=False)
                embed.add_field(name=f"Позиция: {killedPos}", value=f"time: {Time}", inline=False)
                embed.add_field(name=f"Дистанция: {distance}", value=f"Оружик: {weapon}", inline=False)
                embed.set_author(name=bot.user.name, icon_url= bot.user.avatar.url)
                embed.set_thumbnail(url="https://i.ibb.co/chfkZtH/16265679131556258229-128.png")
                embed.set_footer(text=thumbnail)
                await channel.send(embed=embed) 
      
        def getlogs(filename):
            global log
            try:
                with open(filename, encoding='utf-8', mode='r') as f:
                    log = f.readlines()[-1]
            except IndexError:
                print('indexerror')

        async def check_type(log):
            global laststr
            laststr = log
            if 'is connected'.lower() in log.lower():
                print('connection type')
                await connection_type(log)

            if 'has been disconnected'.lower() in log.lower():
                print('discconect type')
                await disconnection_type(log)

            if 'Chat'.lower() in log.lower():
                print('Chat type')
                await chat_type(log)

            if 'Dug in'.lower() in log.lower():
                print('Dug in type')
                await dugin_type(log)

            if 'Dug out'.lower() in log.lower():
                print('Dug out type')
                await dugout_type(log)

            if 'killed by'.lower() in log.lower():
                print('kill type')
                try:
                    await kill_type(log)
                except AttributeError:
                    pass

            if 'committed suicide'.lower() in log.lower():
                print('suicide type')
                await suicide_type(log)

            if 'is unconscious'.lower() in log.lower():
                print('unconscious type')
                await unconscious_type(log)
            
            if 'regained consciousness'.lower() in log.lower():
                print('conscious type')
                await conscious_type(log)

            if 'bled out'.lower() in log.lower():
                print('bled out type')
                await bleed_type(log)

            if 'built'.lower() in log.lower():
                print('build type')
                await build_type(log)

            if 'dismantled'.lower() in log.lower():
                print('dismant type')
                await dismant_type(log)

            if 'placed'.lower() in log.lower():
                print('placed type')
                await place_type(log)

        async def connection_type(log):
            global b
            b = {'Name': '',
            'Id': '',
            'Time': ''}

            j = re.search('Player "', log)
            k = re.search('" is connected', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\)', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            b['type'] = ('connection')
            
            print(b)
            await massage()


        async def disconnection_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Time': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('"\(id', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\)', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            b['type'] = ('disconnection')
            
            print(b)
            await massage()

        async def chat_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Time': '',
            'message': '',
            'type': ''}

            j = re.search('Chat\("', log)
            k = re.search('"\(', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\)', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('\): ', log)
            b['message'] = (log[j.span()[1]:])

            b['type'] = ('chat')

            print(b)
            await massage()
            #channel = bot.get_channel(988455108322934864)
            #await channel.send(f"{b}")
        
        async def dugin_type(log):
            global b
            b = {'Name': '',
            'Id': '',
            'Time': '',
            'stashсord': '',
            'obj': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('" \(id', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search(' \(id=', log)
            k = re.search('= pos=', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('{<', log)
            k = re.search('>}', log)
            b['stashсord'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('in', log)
            k = re.search('at position', log)
            b['obj'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('dugin')
            
            print(b)
            await massage()

        async def dugout_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Time': '',
            'stashсord': '',
            'obj': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('" \(id', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('= pos=', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])
            
            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('{<', log)
            k = re.search('>}', log)
            b['stashсord'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('out', log)
            k = re.search('at position', log)
            b['obj'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('dugout')
            
            print(b)
            await massage()

        async def kill_type(log):
            global b
            b = {'killedName': '',
                'killedId': '',
                'killerName': '',
                'killerId': '',
                'killedPos': '',
                'killerPos': '',
                'weapon': '',
                'distance': '',
                'Time': '',
                'type': ''}

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('Player "', log)
            k = re.search('" \(DEAD\) \(id=', log)
            b['killedName'] = (log[j.span()[1]:k.span()[0]])
            log = log[k.span()[0]:]

            j = re.search('\(id=', log)
            k = re.search('= pos=', log)
            b['killedId'] = (log[j.span()[1]:k.span()[0]])
            log = log[k.span()[1]:]

            j = re.search('Player "', log)
            k = re.search('" \(', log)
            b['killerName'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('<\d', log)
            k = re.search('>\) killed', log)
            b['killedPos'] = (log[j.span()[0]+1:k.span()[0]])
            log = log[k.span()[1]:]

            j = re.search('\(id=', log)
            k = re.search('= pos=', log)
            b['killerId'] = (log[j.span()[1]:k.span()[0]])
            log = log[k.span()[1]:]

            j = re.search('<\d', log)
            k = re.search('>\) with ', log)
            b['killerPos'] = (log[j.span()[0]+1:k.span()[0]])
            log = log[k.span()[1]:]

            j = re.search(' from ', log)
            k = re.search(' meters', log)
            b['distance'] = (log[j.span()[1]:k.span()[0]])
            log = log[:j.span()[0]]

            b['weapon'] = log
            b['type'] = ('killtype')

            print(b)
            await massage()

        async def suicide_type(log):
            global b
        
            b = {'Name': '',
            'Id': '',
            'Time': '',
            'type':''}

            j = re.search("Player '", log)
            k = re.search("' \(id=", log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\) ', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            b['type'] = ('suicide')
            
            print(b)
            await massage()

        async def unconscious_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Pos': '',
            'Time': ''}

            j = re.search('Player "', log)
            k = re.search('" \(', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\ pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('pos=<', log)
            k = re.search('>\) ', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('unconscious')
            
            print(b)
            await massage()

        async def conscious_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Pos': '',
            'Time': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('" \(id=', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\ pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('pos=<', log)
            k = re.search('>\) ', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('conscious')
            
            print(b)
            await massage()

        async def bleed_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Pos': '',
            'Time': ''}

            j = re.search('Player "', log)
            k = re.search('" \(DEAD', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\ pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('pos=<', log)
            k = re.search('>\) ', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('bleed')
            
            print(b)
            await massage()

        async def build_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Object': '',
            'Tool': '',
            'Pos': '',
            'Time': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('" \(id=', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\ pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('Built ', log)
            k = re.search(' with', log)
            b['Object'] = (log[j.span()[1]:k.span()[0]])
            try:
                j = re.search('with ', log)
                k = re.search('\n', log)
                b['Tool'] = (log[j.span()[1]:k.span()[0]])
            except AttributeError:
                j = re.search('with ', log)
                b['Tool'] = (log[j.span()[1]:])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('pos=<', log)
            k = re.search('>\)', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('build')
        
            print(b)
            await massage()

        async def dismant_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Object': '',
            'Tool': '',
            'Pos': '',
            'Time': ''}

            j = re.search('Player "', log)
            k = re.search('" \(id=', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('=\ pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('Dismantled ', log)
            k = re.search(' with', log)
            b['Object'] = (log[j.span()[1]:k.span()[0]])
            try:
                j = re.search('with ', log)
                k = re.search('\n', log)
                b['Tool'] = (log[j.span()[1]:k.span()[0]])
            except AttributeError:
                j = re.search('with ', log)
                b['Tool'] = (log[j.span()[1]:])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            j = re.search('pos=<', log)
            k = re.search('>\)', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            b['type'] = ('dismant')
            
            print(b)
            await massage()

        async def place_type(log):
            global b
            
            b = {'Name': '',
            'Id': '',
            'Pos': '',
            'Object': '',
            'Time': '',
            'type':''}

            j = re.search('Player "', log)
            k = re.search('" \(id=', log)
            b['Name'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\(id=', log)
            k = re.search('= pos', log)
            b['Id'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('placed ', log)
            b['Object'] = (log[j.span()[1]:])

            j = re.search('pos=<', log)
            k = re.search('>\)', log)
            b['Pos'] = (log[j.span()[1]:k.span()[0]])

            j = re.search('\d\d:\d\d:\d\d', log)
            b['Time'] = (log[:j.span()[1]])

            b['type'] = ('place')
            
            print(b)
            await massage()

        laststr = ''
        getlogs(filename)

        while True:
            global log
            if log == laststr:
                getlogs(filename) 
            else:
                await check_type(log)
                
                
def setup(bot):
    bot.add_cog(main(bot))
