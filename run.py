print("Started")
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
iam=[
    "im",
    "i am",
    "i'm"
]
import random
import discord
import os
from discord.ext import commands
import time
from config import config
from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot import utils
from musicbot.utils import guild_to_audiocontroller, guild_to_settings

from musicbot.commands.general import General
from musicbot.commands.others import Others
from musicbot.commands.uno import Uno

initial_extensions = ['musicbot.commands.music',
                    'musicbot.commands.general', 'musicbot.plugins.button',"musicbot.commands.others", "musicbot.commands.uno"]
bot = commands.Bot(command_prefix=config.BOT_PREFIX, pm_help=True, case_insensitive=True)


if __name__ == '__main__':

    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if config.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)


@bot.event
async def on_ready():
    print(config.STARTUP_MESSAGE)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Music, type {}help".format(config.BOT_PREFIX)))

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(config.STARTUP_COMPLETE_MESSAGE)
#await current_guild.voice_client.disconnect(force=True)
                
@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    vc_channels = guild.voice_channels
    await guild.me.edit(nick=guild_to_settings[guild].get('default_nickname'))
    start_vc = guild_to_settings[guild].get('start_voice_channel')
    if start_vc != None:
        for vc in vc_channels:
            if vc.id == start_vc:
                await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])

                #place for disconnect
                try:
                    await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                except Exception as e:
                    print(e)
    else:
        await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
        try:
            await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
        except Exception as e:
            print(e)
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
    elif "groovy" in message.content.lower():
        await message.channel.send("Groovy was killed by the capitalist Youtube, may we all have Fs in the chat for the death of Groovy. -Alpaca")
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
    elif "janice" in message.content.lower():
        await message.channel.send("Neptune")
        await bot.process_commands(message)
    elif "fuck you" in message.content.lower():
        await message.channel.send("Fuck you too")
        await bot.process_commands(message)
    elif "fuck u" in message.content.lower():
        await message.channel.send("Fuck u too")
        await bot.process_commands(message)
    elif "happy" in message.content.lower():
        await message.channel.send("IKR, things are simple when you're happy")
        await bot.process_commands(message)
    elif "no u" in message.content.lower():
        await message.channel.send("no u ")
        await bot.process_commands(message)
    elif "no you" in message.content.lower():
        await message.channel.send("no u ")
        await bot.process_commands(message)
    elif message.content.startswith("i am"):
        input=message.content.lower()
        input =input.replace("i am", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("im"):
        input=message.content.lower()
        input =input.replace("im", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("iam"):
        input=message.content.lower()
        input =input.replace("iam", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("i'm"):
        input=message.content.lower()
        input =input.replace("i'm", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("I am"):
        input=message.content.lower()
        input =input.replace("i am", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("Im"):
        input=message.content.lower()
        input =input.replace("im", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("Iam"):
        input=message.content.lower()
        input =input.replace("iam", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif message.content.startswith("I'm"):
        input=message.content.lower()
        input =input.replace("i'm", "")
        await message.channel.send("Hi " + input + " I'm Alpaca")
    elif "cara" in message.content.lower():
        await message.channel.send("Neptune")
        await bot.process_commands(message)
    elif "simp" in message.content.lower():
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

bot.run(config.BOT_TOKEN, bot=True)
