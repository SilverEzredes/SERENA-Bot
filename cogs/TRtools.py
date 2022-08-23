from discord.ext import commands
import datetime
import discord
import psutil
import os

# Local imports
from modules import globals, utils


class TRtools(commands.Cog,
          description="Commands for Tomb Raider modding tools."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="BlenderFBX",
                      description="",
                      usage="{prfx}FBX",
                      help="",
                      aliases=["BlenderFBX"])
    async def BlenderFBX(self, ctx):
        desc = "Fixes fbx import plugin for blender."
        await utils.embed_reply(ctx,
                                title="Blender FBX Importer",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[BlenderFBX - NexusMods](https://www.nexusmods.com/witcher3/mods/6118)",                                                                                                                                          True],
                                    ["💻 Developer", "Aaron",                                                                                                                                          True],                               ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126039246700544.png")
def setup(bot):
    bot.add_cog(TRtools(bot))
