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
import re
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
    "imagine playing valorant, when you can make your own game"
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
file=open("token.txt","r")
lines=file.readlines()
TOKEN=lines[0]
start_time = time.time()
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
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
    embedVar.add_field(name="youtube", value="Search youtube \n Syntax: \n $youtube (item)", inline=False)
    embedVar.add_field(name="Source code", value="Check the source code \n Syntax: \n $source", inline=False)
    embedVar.add_field(name="Issues", value="Get the links to report an issue regarding any projects on NuggetCat. \n Syntax: \n $issue")
    await ctx.channel.send(embed=embedVar)
@bot.command(name="youtube")
@commands.cooldown(1,1,BucketType.user)
async def youtube(ctx, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
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
    backsticks = "```"
    query = backsticks + query + backsticks
    results = wikipedia.summary(query, sentences=3)
    await ctx.channel.send(results)
@bot.command(name="urban")
@commands.cooldown(1,1,commands.BucketType.user)
async def urban(ctx,query):
    r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(query))
    soup = BeautifulSoup(r.content)
    await ctx.send("Here is your definition on "+ query)
    await ctx.send(soup.find("div",attrs={"class":"meaning"}).text)
@bot.command(name="issue")
@commands.cooldown(1,3, commands.BucketType.user)
async def issue(ctx:commands.Context):
    embedVar=discord.Embed(title="Issues and suggestions", color=0x990000)
    embedVar.add_field(name="Alpha", value="https://github.com/nuggetcatsoftware/Alpha/issues", inline=False)
    embedVar.add_field(name="Alpaca bot", value="https://github.com/nuggetcatsoftware/Alpaca-bot/issues", inline=False)
    embedVar.add_field(name="Operation Yellowbird", value="https://github.com/nuggetcatsoftware/Operation-Yellowbird/issues", inline=False)
    await ctx.channel.send(embed=embedVar)
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
    if "gabriel" in message.content.lower():
        await message.channel.send('Ma!')
        await bot.process_commands(message)
    if "alpaca" in message.content.lower():
        response=random.choice(alpaca_noises)
        await message.channel.send(response)
        await bot.process_commands(message)
    if "nikita" in message.content.lower():
        await message.channel.send("Harrasspin")
        await bot.process_commands(message)
    if "cunt" in message.content.lower():
        await message.channel.send("Pussy!")
        await bot.process_commands(message)
    if "pls kill" in message.content.lower():
        await message.channel.send("That's very blood thirsty of you {}".format(message.author.mention))
        await bot.process_commands(message)
    if "nigger" in message.content.lower():
        await message.channel.send("Oi! Don't be racists!{}".format(message.author.mention))
        await bot.process_commands(message)
    if "racist" in message.content.lower():
        await message.channel.send("You can't be racist if there's no other race -Adolf Hitler")
        await bot.process_commands(message)
    if "valorant" in message.content.lower():
        await message.channel.send("Imagine playing Valorant when you can make your own game -Alpaca")
        await bot.process_commands(message)
    if "dick" in message.content.lower():
        await message.channel.send("Pussy")
        await bot.process_commands(message)
    if "China" in message.content.lower():
        await message.channel.send("Wuhanhanhanhan")
        await bot.process_commands(message)
    if "good" in message.content.lower():
        response=random.choice(goodresponse)
        await message.channel.send(response)
        await bot.process_commands(message)
    if "bad" in message.content.lower():
        resoinse=random.choice(badresponse)
        await message.channel.send(resoinse)
        await bot.process_commands(message)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embedVar=discord.Embed(title="PWAAAAT!!!. Don't forget, Alpacas are smart enough to detect spam", color=0xff0000)
        embedVar.add_field(name="What a scrub", value=f"Try again after {round(error.retry_after, 2)} seconds!")
        await ctx.send(embed=embedVar)

bot.run(TOKEN)