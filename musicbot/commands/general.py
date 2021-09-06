import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext import commands
from config import config
from musicbot import utils
from musicbot.audiocontroller import AudioController
from musicbot.utils import guild_to_audiocontroller, guild_to_settings
import time
import psutil
import TenGiphPy
class General(commands.Cog):
    """ A collection of the commands for moving the bot around in you server.

            Attributes:
                bot: The instance of the bot that is executing the commands.
    """

    def __init__(self, bot):
        self.bot = bot

    # logic is split to uconnect() for wide usage
    @commands.command(name='connect', description=config.HELP_CONNECT_LONG, help=config.HELP_CONNECT_SHORT, aliases=['c'])
    async def _connect(self, ctx):  # dest_channel_name: str
        await self.uconnect(ctx)

    async def uconnect(self, ctx):

        vchannel = await utils.is_connected(ctx)

        if vchannel is not None:
            await ctx.send(config.ALREADY_CONNECTED_MESSAGE)
            return

        current_guild = utils.get_guild(self.bot, ctx.message)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return

        if utils.guild_to_audiocontroller[current_guild] is None:
            utils.guild_to_audiocontroller[current_guild] = AudioController(
                self.bot, current_guild)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("Connected to {} {}".format(ctx.author.voice.channel.name, ":white_check_mark:"))

    @commands.command(name='disconnect', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['dc'])
    async def _disconnect(self, ctx, guild=False):
        await self.udisconnect(ctx, guild)

    async def udisconnect(self, ctx, guild):

        if guild is not False:

            current_guild = guild

            await utils.guild_to_audiocontroller[current_guild].stop_player()
            await current_guild.voice_client.disconnect(force=True)

        else:
            current_guild = utils.get_guild(self.bot, ctx.message)

            if current_guild is None:
                await ctx.send(config.NO_GUILD_MESSAGE)
                return

            if await utils.is_connected(ctx) is None:
                await ctx.send(config.NO_GUILD_MESSAGE)
                return

            await utils.guild_to_audiocontroller[current_guild].stop_player()
            await current_guild.voice_client.disconnect(force=True)
            await ctx.send("Disconnected from voice channel. Use '{}c' to rejoin.".format(config.BOT_PREFIX))

    @commands.command(name='reset', description=config.HELP_DISCONNECT_LONG, help=config.HELP_DISCONNECT_SHORT, aliases=['rs', 'restart'])
    async def _reset(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} Connected to {}".format(":white_check_mark:", ctx.author.voice.channel.name))

    @commands.command(name='changechannel', description=config.HELP_CHANGECHANNEL_LONG, help=config.HELP_CHANGECHANNEL_SHORT, aliases=['cc'])
    async def _change_channel(self, ctx):
        current_guild = utils.get_guild(self.bot, ctx.message)

        vchannel = await utils.is_connected(ctx)
        if vchannel == ctx.author.voice.channel:
            await ctx.send("{} Already connected to {}".format(":white_check_mark:", vchannel.name))
            return

        if current_guild is None:
            await ctx.send(config.NO_GUILD_MESSAGE)
            return
        await utils.guild_to_audiocontroller[current_guild].stop_player()
        await current_guild.voice_client.disconnect(force=True)

        guild_to_audiocontroller[current_guild] = AudioController(
            self.bot, current_guild)
        await guild_to_audiocontroller[current_guild].register_voice_channel(ctx.author.voice.channel)

        await ctx.send("{} Switched to {}".format(":white_check_mark:", ctx.author.voice.channel.name))


    @commands.command(name="gifs", description="Grabs you gifs", help="-gifs (target) to grab your gifs")
    async def _gifs(self, ctx, *,giftag:str):
        t = TenGiphPy.Tenor(token="QKTF66N1775V")
        getgifurl = t.random(str(giftag))
        await ctx.send(getgifurl)
    @_gifs.error
    async def tenor_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('what gif you want dude?')
        else:
            raise error
    @commands.command(name="weather", description="Provides weather stats of your city", help="-weather (city) to know the weather")
    async def _weather(self, ctx, *, city: str):
        print(city)
        # Python program to find current 
        # weather details of any city
        # using openweathermap api
        # import required modules
        import requests, json
        # Enter your API key here
        api_key = "599697465b8997b41ed0b72b66702336"
        
        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        
        # json method of response object 
        # convert json format data into
        # python format data
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature= current_temperature-273.15
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
        
            # store the value of "weather"
            # key in variable z
            z = x["weather"]
        
            # store the value corresponding 
            # to the "description" key at 
            # the 0th index of z
            weather_description = z[0]["description"]
        
            # print following values
            await ctx.send(" Temperature (Celcius) = " +
                            str(current_temperature) + 
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description))
        
        else:
            await ctx.send(" City Not Found ")
    
    @commands.command(name="harass", description="harass someone with this command!!", help="-harass @someone (no. of times) to harass a person")
    async def _harass(self, ctx,*, user: discord.User, num: int):
        if num > 31:
            if ctx.message.author.id=="394049095544733706":
                await ctx.send(f'Started pinging {user.name} {num} times.', delete_after=0.1)
                for i in range(num):
                    await ctx.channel.send(user.mention, delete_after=0.1)
                await ctx.send(f'Finished {num} pings for {user.name}', delete_after=0.1)
            else:
                embedVar=discord.Embed(title="Chill")
                embedVar.add_field(name="Bruh", value="m8 you need a bo'oh o' wo'er m8 innit? calm tf down", inline=False)
                embedVar.add_field(name="But", value="Premium users get more harrassment")
                await ctx.channel.send(embed=embedVar)
                return
        else:
            await ctx.send(f'Started pinging {user.name} {num} times.', delete_after=0.1)
            for i in range(num):
                await ctx.channel.send(user.mention, delete_after=0.1)
            await ctx.send(f'Finished {num} pings for {user.name}', delete_after=0.1)

    @commands.command(name="ball",description="Make life decisions with 8ball!!", help="-ball (your question), to generate wisdom")
    async def _ball(self,ctx, *, query:str):
        ballresponse=[
            "No",
            "yes",
            "concentrate and try again",
            "not likely",
            "Likely",
            "That's not gonna happen"
        ]
        print(query)
        import random
        response=random.choice(ballresponse)
        await ctx.send(response)

    @commands.command(name="urban", description="Search urban dictionary", help="-urban (word) (definition no.) to search your word. NSFW BE WARNED")
    async def _urban(self,ctx,*,query,count=1):
        try:
            count = int(count)
            import requests
            from bs4 import BeautifulSoup
            r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(query))
            soup = BeautifulSoup(r.content, features="html.parser")
            item_id = int(count)
            entries = soup.find_all("div", class_="meaning")
            if item_id == 1:
                item_id -= 1
            if item_id < len (entries):
                await ctx.send("Here is your definition on "+ query)
                await ctx.send(entries[item_id].text)
            else:
                await ctx.send("No result.")
        except ValueError:
            count=1
            import requests
            from bs4 import BeautifulSoup
            r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(query))
            soup = BeautifulSoup(r.content, features="html.parser")
            item_id = int(count)
            entries = soup.find_all("div", class_="meaning")
            if item_id == 1:
                item_id -= 1
            if item_id < len (entries):
                await ctx.send("Here is your definition on "+ query)
                await ctx.send(entries[item_id].text)
            else:
                await ctx.send("No result.")
    
    @commands.command(name="hourly", description="Get your hourly dose of alpaca", help="Just run the command dumbo")
    async def _hourly(self,ctx):
        giftag="alpaca"
        t = TenGiphPy.Tenor(token="QKTF66N1775V")
        getgifurl = t.random(str(giftag))
        await ctx.send(f'{getgifurl}')

    @commands.command(name='ping', description=config.HELP_PING_LONG, help=config.HELP_PING_SHORT)
    async def _ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
    


    @commands.command(name="Debug", description="For nerds only", help="don't even try this ")
    async def debug(self, ctx):
        print("Debug command")
        await ctx.send("IF you are reading this: The bot has: \n 0: Exceptions raised \n Unknown number of warnings \n Bot is online")
        time.sleep(1)
        await ctx.send("Host clinet ram usage: ")
        await ctx.send(psutil.virtual_memory())
        before = time.monotonic()
        message = await ctx.send("Ping: ")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping:  `{int(ping)}ms`")

    @commands.command(name="issues", description="Report issues with this command", help="-issue for further instructions")
    async def issues(self,ctx):
        print("issue command issued! YOU HAVE A BUG DIPSHIT, FIX IT")
        embedVar = discord.Embed(title="Issues", description="Please see below are ways to tech support or bug report.Sorry for any inconvenience.", color=0xffd700)
        embedVar.add_field(name="Discord", value="Go to the tech support and we will have developers to help you. Click [here](https://discord.gg/KggWRtC7Z9)", inline=False)
        embedVar.add_field(name="Github", value="Report serious bugs to devs. ONLY USE IT FOR BUGS. Tech support will not be addressed!! Click [here](https://github.com/nuggetcatsoftware/Alpaca-bot/issues)", inline=False)
        embedVar.add_field(name="Fix it yourself", value="Click [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", inline=False)
        await ctx.channel.send(embed=embedVar)
    @commands.command(name="query", description="Checks server query", help="-query checks the server where you sent your command.")
    async def query(self, ctx):
        owner=str(ctx.guild.owner)
        region = str(ctx.guild.region)
        guild_id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        desc=ctx.guild.description
        
        embed = discord.Embed(
            title=ctx.guild.name + " Server Information",
            description=desc,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)

        members=[]
        async for member in ctx.guild.fetch_members(limit=150) :
            await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))

    @commands.command(name='setting', description=config.HELP_SHUFFLE_LONG, help=config.HELP_SETTINGS_SHORT, aliases=['settings', 'set'])
    @has_permissions(administrator=True)
    async def _settings(self, ctx, *args):

        sett = guild_to_settings[ctx.guild]

        if len(args) == 0:
            await ctx.send(embed=await sett.format())
            return

        args_list = list(args)
        args_list.remove(args[0])

        response = await sett.write(args[0], " ".join(args_list), ctx)

        if response is None:
            await ctx.send("`Error: Setting not found`")
        elif response is True:
            await ctx.send("Setting updated!")



def setup(bot):
    bot.add_cog(General(bot))
