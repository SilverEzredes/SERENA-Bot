from discord.ext import commands
import datetime
import discord
import psutil
import os

# Local imports
from modules import globals, utils


class REtools(commands.Cog,
          description="Commands for RE Engine tools"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="REFramework",
                      description="",
                      usage="{prfx}REFramework",
                      help="",
                      aliases=["ref"])
    async def reframework(self, ctx):
        desc = "A mod framework, scripting platform, and modding tool for RE Engine games."
        await utils.embed_reply(ctx,
                                title="REFramework",
                                description=desc,
                                fields=[
                                    ["♾️ Uptime:",          f"{utils.time_from_start()}",                                                                                                                                          True],
                                    ["☯️ Next Restart In:", f"{utils.time_to_restart()}",                                                                                                                                          True],
                                    ["⏳ Ping:",            f"{int(globals.bot.latency * 1000)}ms",                                                                                                                                True],
                                    ["📟 CPU Usage",        f"{psutil.cpu_percent()}%",                                                                                                                                            True],
                                    ["💾 RAM Usage",        f"{utils.pretty_size(psutil.Process(os.getpid()).memory_info().rss)}/{'512MB' if os.environ.get('DYNO') else utils.pretty_size(psutil.virtual_memory().total)}",       True],
                                    ["🚀 Last Update",      f"{datetime.datetime.fromisoformat(os.environ.get('HEROKU_RELEASE_CREATED_AT')[:-1]).strftime('%d/%m/%Y') if os.environ.get('HEROKU_RELEASE_CREATED_AT') else 'N/A'}", True],
                                    ["👨‍💻 Developer",        "[WillyJL](https://linktr.ee/WillyJL)",                                                                                                                               True],
                                    ["📚 Library",          f"discord.py v{discord.__version__}",                                                                                                                                  True],
                                    ["📦 Version",          f"{os.environ.get('HEROKU_RELEASE_VERSION') if os.environ.get('HEROKU_RELEASE_VERSION') else 'N/A'}",                                                                  True],
                                ],
                                thumbnail=globals.bot.user.avatar_url)

def setup(bot):
    bot.add_cog(REtools(bot))
