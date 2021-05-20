import discord
import os
import time
from discord import embeds
from discord import message
from discord.errors import InvalidArgument
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import cooldown
import random
import wikipedia
import  requests
from bs4 import BeautifulSoup
from urllib import parse, request
from discord.ext import tasks
import os
import youtube_dl
import asyncio
import re
import TenGiphPy
try:
    from googlesearch import search
except ImportError:
    print("module google not found", "Check pip installation")
prescense=[
    "with your wife",
    "Grand Theft Auto IRL",
    "Human simulator",
    "OnlyAlpacas"
]
alpaca_noises=[
    "pwaaa!",
    "pwaaaaaat!",
    "screw you",
    "Shut up im playing minecraft",
]
goodresponse=[
    "nice",
    "acceptable",
    "not bad",
    "awesome",
    "cool",
    ":kekw:"
]
badresponse=[
    "not good",
    "crap",
    "shit",
    "Know your fucking place trash"
]
ballresponse=[
    "No",
    "yes",
    "concentrate and try again",
    "not likely",
    "Likely",
    "That's not gonna happen"
]
alpaca_happy=[
    "Pwaaa! :)",
    "PWaaaat!",
    "Pwaa ~~ :heart: "
]
t = TenGiphPy.Tenor(token="QKTF66N1775V")
file=open("token.txt","r")
lines=file.readlines()
TOKEN=lines[0]
start_time = time.time()
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send("I'm BACK!Pwaaaa!")
                await channel.send(file=discord.File('happyalpaca.gif'))
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))
    print(f'{bot.user.name} has connected to discord and is now online')
    print("Connection time: \n")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("STARTED!!")
    showshow=random.choice(prescense)
    await bot.change_presence(activity=discord.Game(showshow))

bot.remove_command('help')
async def on_member_join(member):
    await member.create_dm()
    embedVar = discord.Embed(title="Pwaaaa", description="What's up nerd! Don't forget to check out this superior Alpaca! ", color=0xff0000)
    embedVar.add_field(name="Let's get started!", value="Type: (@help) to get started!!", inline=False)
    await member.dm_channel.send(f'Hi {member.name}')
    await member.dn_channel.send(embed=embedVar)

@bot.command(name="ping")
@commands.cooldown(1, 1,commands.BucketType.user)
async def ping(ctx: commands.Context):
    await ctx.send(f"Pwaaaaa! {round(bot.latency * 1000)}ms")
@bot.command(name="help")
@commands.cooldown(1,1,commands.BucketType.user)
async def help(ctx:commands.Context):
    embedVar = discord.Embed(title="Alpaca Help", description="Alpaca is here to help someone who is in distress uwu", color=0xffd700)
    embedVar.add_field(name="Wikipedia", value="Function: \n Searches valid input on wikipedia \n Syntax: \n $wikipedia (stuff)", inline=False)
    embedVar.add_field(name="Urban", value="Function: \n Searches urban dictionary\n Syntax: \n $urban (stuff) ", inline=False)
    embedVar.add_field(name="Updates", value="Function: Check recent updates\n Syntax: \n $update", inline=False)
    embedVar.add_field(name="Weather", value="Check your local weather with this awesome command! \nSyntax: \n $weather(city)", inline=False)
    embedVar.add_field(name="Ping", value="Check current ping \n Syntax: \n $ping", inline=False)
    embedVar.add_field(name="Source code", value="Check the source code \n Syntax: \n $source", inline=False)
    embedVar.add_field(name="Issues", value="Get the links to report an issue regarding any projects on NuggetCat. \n Syntax: \n $issue", inline=False)
    embedVar.add_field(name="music", value="Play music. \n syntax: \n 1. Join vc ($join) \n 2. Leave vc ($die) \n 3. Play song ($song (url)) \n 4. Pause ($pause) \n 5. Resume ($resume) \n 6. Stop ($stop)", inline=False)
    embedVar.add_field(name="query", value="For users who question their existence. \n syntax: \n $query", inline=False)
    embedVar.add_field(name="about", value="Know more about Alpaca and his developer!", inline=False)
    embedVar.add_field(name="ball", value="Make life decisions!! \n syntax: \n $ball (stuff)", inline=False)
    embedVar.add_field(name="daily", value="Claim your daily dose of alpacas! \n Syntax: \n $daily",inline=False)
    await ctx.channel.send(embed=embedVar)
@bot.command(name="harass")
@commands.cooldown(1,30,BucketType.user)
async def harrass(ctx, user: discord.User, num: int):
    if num > 31:
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
@bot.command(name="ball")
@commands.cooldown(1,1,BucketType.user)
async def ball(ctx, query):
    print(query)
    response=random.choice(ballresponse)
    await ctx.send(response)

@bot.command(name="query")
@commands.cooldown(1,1,BucketType.user)
async def query(ctx):
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

@bot.command()
@commands.cooldown(1,1,BucketType.user)
async def about(ctx):
    text = "Hi, I am Alpaca, im very smart!"
    await ctx.send(text)
@bot.command(name='join')
@commands.cooldown(1,2,BucketType.user)
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()
@bot.command(name='die')
@commands.cooldown(1,2,BucketType.user)
async def die(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
@bot.command(name="update")
@commands.cooldown(1,1,commands.BucketType.user)
async def update(ctx:commands.Context):
    embedVar = discord.Embed(title="Updates", color=0x123456)
    embedVar.add_field(name="Update 1.0", value="Add new embeds for commands and urban dictionary integration", inline=False)
    embedVar.add_field(name="Update 2.0", value="Added new stuff and cooler embeds! \n Better Alpaca noises \n More online time \n Bug fixes \n Now a music bot \n Admin commands!", inline=False)
    await ctx.channel.send(embed=embedVar)
@bot.command(name="source")
@commands.cooldown(1,3, commands.BucketType.user)
async def source(ctx:commands.Context):
    await ctx.channel.send("Source code is on github! https://github.com/nuggetcatsoftware/Alpaca-bot")
@bot.command(name="wikipedia")
@commands.cooldown(1, 3, commands.BucketType.user)
async def wikipedia(ctx, query):
    print(query)
    results = wikipedia.summary(query, sentences=3)
    await ctx.channel.send(results)
@bot.command(name="urban")
@commands.cooldown(1,1,commands.BucketType.user)
async def urban(ctx,query,count = 1):
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
@commands.command(name="gifs")
@commands.cooldown(1, 3, commands.BucketType.user)
async def gifs(ctx, giftag):
    getgifurl = t.random(str(giftag))
    await ctx.send(getgifurl)
    
@gifs.error
async def tenor_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('what gif you want dude?')
    else:
      raise error


@bot.command(name="hourly")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def hourly(ctx:commands.Context):
    giftag="alpaca"
    getgifurl = t.random(str(giftag))
    await ctx.send(f'{getgifurl}')
@bot.command(name="issue")
@commands.cooldown(1,3, commands.BucketType.user)
async def issue(ctx:commands.Context):
    embedVar=discord.Embed(title="Issues and suggestions", color=0x990000)
    embedVar.add_field(name="Alpha", value="https://github.com/nuggetcatsoftware/Alpha/issues", inline=False)
    embedVar.add_field(name="Alpaca bot", value="https://github.com/nuggetcatsoftware/Alpaca-bot/issues", inline=False)
    embedVar.add_field(name="Operation Yellowbird", value="https://github.com/nuggetcatsoftware/Operation-Yellowbird/issues", inline=False)
    await ctx.channel.send(embed=embedVar)
@bot.command(name="repeat")
@commands.cooldown(1,1,commands.BucketType.user)
async def repeat(ctx, repeater):
    print(repeater)
    if repeater.lower() =="i am stupid":
        await ctx.channel.send("We know")
    elif repeater.lower() =="im stupid":
        await ctx.channel.send("We know")
    elif repeater.lower() =="i'm stupid":
        await ctx.channel.send("We know")
    elif repeater.lower() =="im gay":
        await ctx.channel.send("We know")
    elif repeater.lower() =="i'm gay":
        await ctx.channel.send("We know")
    elif repeater.lower() =="i am gay":
        await ctx.channel.send("We know")
    else:
        await ctx.channel.send(repeater)
@bot.command(name="weather")
@commands.cooldown(1, 10,commands.BucketType.user)
async def weather(ctx, city):
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

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    if "gabriel" in message.content.lower():
        await message.channel.send('Ma!')
        await bot.process_commands(message)
    elif "pwa" in message.content.lower():
        response=random.choice(alpaca_happy)
        await message.channel.send(response)
        await bot.process_commands(message)      
    elif "alpaca" in message.content.lower():
        response=random.choice(alpaca_noises)
        await message.channel.send(response)
        await bot.process_commands(message)
    elif "nikita" in message.content.lower():
        await message.channel.send("Harrasspin")
        await bot.process_commands(message)
    elif "cunt" in message.content.lower():
        await message.channel.send("Pussy!")
        await bot.process_commands(message)
    elif "pls kill" in message.content.lower():
        await message.channel.send("That's very blood thirsty of you {}".format(message.author.mention))
        await bot.process_commands(message)
    elif "nigger" in message.content.lower():
        await message.channel.send("Oi! Don't be racists!{}".format(message.author.mention))
        await bot.process_commands(message)
    elif "racist" in message.content.lower():
        await message.channel.send("You can't be racist if there's no other race -Adolf Hitler")
        await bot.process_commands(message)
    elif "valorant" in message.content.lower():
        await message.channel.send("Imagine playing Valorant when you can make your own game -Alpaca")
        await bot.process_commands(message)
    elif "dick" in message.content.lower():
        await message.channel.send("Pussy")
        await bot.process_commands(message)
    elif "china" in message.content.lower():
        await message.channel.send("Wuhanhanhanhan")
        await bot.process_commands(message)
    elif "good" in message.content.lower():
        response=random.choice(goodresponse)
        await message.channel.send(response)
        await bot.process_commands(message)
    elif "bad" in message.content.lower():
        resoinse=random.choice(badresponse)
        await message.channel.send(resoinse)
        await bot.process_commands(message) 
    elif "sad" in message.content.lower():
        await message.channel.send("Sadge")
        await bot.process_commands(message)
    elif "fuck you" in message.content.lower():
        await message.channel.send("Fuck you too")
        await bot.process_commands(message)
    elif "happy" in message.content.lower():
        await message.channel.send("IKR, things are simple when you're happy")
        await bot.process_commands(message)
    elif "cara" in message.content.lower():
        await message.channel.send("Neptune")
        await bot.process_commands(message)
    elif "jas" in message.content.lower():
        pon=[
            "poooooon",
            "pooon",
            "poooooooooooooooon",
            "poooooooooooooooooooooooooooooooooooooooooooon"
        ]
        response=random.choice(pon)
        await message.channel.send(response)
        await bot.process_commands(message)
    elif "jason" in message.content.lower():
        pon=[
            "poooooon",
            "pooon",
            "poooooooooooooooon",
            "poooooooooooooooooooooooooooooooooooooooooooon"
        ]
        response=random.choice(pon)
        await message.channel.send(response)
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embedVar=discord.Embed(title="PWAAAAT!!!. Don't forget, Alpacas are smart enough to detect spam", color=0xff0000)
        embedVar.add_field(name="What a scrub", value=f"Try again after {round(error.retry_after, 2)} seconds!")
        await ctx.send(embed=embedVar)

bot.run(TOKEN)
