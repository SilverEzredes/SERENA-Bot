from discord.ext import commands
import datetime
import discord
import psutil
import os

# Local imports
from modules import globals, utils


class Bot(commands.Cog,
          description="Commands regarding the bot instance"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reframework",
                      description="A mod framework, scripting platform, and modding tool for RE Engine games.",
                      usage="{prfx}reframework",
                      help="",
                      aliases=["ref"])
    async def reframework(self, ctx):
        desc = "A mod framework, scripting platform, and modding tool for RE Engine games.\n"
        await utils.embed_reply(ctx,
                                title="REFramework",
                                description=desc
                                fields=[
                                    ["🔗 Link:",          "[REFramework - GitHub](https://github.com/praydog/REFramework-nightly/releases)",                                                                                                                                          True],
                                    ["‍💻 Developer",      "Praydog",                                                                                                                                          True],
                                ],
                                thumbnail=globals.bot.user.avatar_url)


def setup(bot):
    bot.add_cog(Bot(bot))
