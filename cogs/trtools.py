from discord.ext import commands

# Local imports
from modules import globals, utils


class TRtools(commands.Cog,
          description="Commands for Tomb Raider modding tools."):
    def __init__(self, bot):
        self.bot = bot

    @utils.hybcommand(globals.bot,
                      name="blenderfbx",
                      description="",
                      usage="{prfx}blenderfbx",
                      help="",
                      aliases=[],
                      slash_aliases=False)
    async def blenderfbx(self, ctx):
        desc = "Fixes fbx import plugin for blender."
        await utils.embed_reply(ctx,
                                title="Blender FBX Importer",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[BlenderFBX - NexusMods](https://www.nexusmods.com/witcher3/mods/6118)",                                                                                                                                          True],
                                    ["💻 Developer", "Aaron",                                                                                                                                          True],                               ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126039246700544.png")
async def setup(bot):
    await bot.add_cog(TRtools(bot))
