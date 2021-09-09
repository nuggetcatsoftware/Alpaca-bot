import discord
from discord.colour import Color
from discord.ext import commands
from config import config
import time
import os
from discord import embeds
from discord import message
class Uno(commands.Cog):
    """the only help command here bruh"""
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name="Uno", description="List of commands for Uno game in discord", help="-uno")
    async def _uno(self, ctx):
        print("uno")
        embedVar=discord.Embed(title="Uno", description="The list of commands for UNO", color=0x00ff00)
        embedVar.add_field(name="WIP", value="work in progress", inline=False)
        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Uno(bot))