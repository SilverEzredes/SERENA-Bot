from discord.ext import commands
import datetime
import discord
import psutil
import os

# Local imports
from modules import globals, utils


class REtools(commands.Cog,
          description="Commands for RE Engine tools."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="REFramework",
                      description="",
                      usage="{prfx}reframework",
                      help="",
                      aliases=["ref"])
    async def reframework(self, ctx):
        desc = "A mod framework, scripting platform, and modding tool for\n RE Engine games."
        await utils.embed_reply(ctx,
                                title="REFramework",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[REFramework - GitHub](https://github.com/praydog/REFramework-nightly/releases)",                                                                                                                                          True],
                                    ["💻 Developer", "Praydog",                                                                                                                                          True],
                                    ["📖 More Info:",       "[REF - GitBook](https://cursey.github.io/reframework-book/)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126039246700544.png")

    @commands.command(name="Noesis Plugin & REEM",
                      description="",
                      usage="{prfx}noesisplugin",
                      help="",
                      aliases=["noesis", "reem", "Plugin", "fmt", "fmtREmesh", "newMS", "noises"])
    async def noesisplugin(self, ctx):
        desc = "A plugin for Rich Whitehouse's Noesis to import and export\n RE Engine Meshes and Textures."
        await utils.embed_reply(ctx,
                                title="Noesis Plugin - REEM Noesis CMD",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Noesis Plugin - GitHub](https://github.com/alphazolam/fmt_RE_MESH-Noesis-Plugin)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994124668690767912.png")

    @commands.command(name="REtool",
                      description="",
                      usage="{prfx}retool",
                      help="",
                      aliases=["unpak"])
    async def retool(self, ctx):
        desc = "A tool used for extracting the embedded game files from every\n RE Engine game's PAK files."
        await utils.embed_reply(ctx,
                                title="REtool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[REtool](https://residentevilmodding.boards.net/thread/10567/pak-tex-editing-tool)",                                                                                                                                          True],
                                    ["💻 Developer", "FluffyQuack",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126946680176751.png")

    @commands.command(name="FluffyModManager",
                      description="",
                      usage="{prfx}fluffymodmanager",
                      help="",
                      aliases=["fmm", "modmanager", "fluffy", "sockpuppet"])
    async def fluffymodmanager(self, ctx):
        desc = "Fluffy Manager 5000 lets you manage mods for various titles,\n such as most Resident Evil titles, Devil May Cry 5, SoulCalibur VI, and more."
        await utils.embed_reply(ctx,
                                title="Fluffy Mod Manager 5000",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Fluffy Mod Manager](https://www.fluffyquack.com/)",                                                                                                                                          True],
                                    ["💻 Developer", "FluffyQuack",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126946680176751.png")

    @commands.command(name="010 - RE RSZ",
                      description="",
                      usage="{prfx}re_rsz",
                      help="",
                      aliases=["rsz", "HolyTemplate", "010rsz"])
    async def re_rsz(self, ctx):
        desc = "010 Editor Binary Template for editing RE Engine game files contiaining RSZ data."
        await utils.embed_reply(ctx,
                                title="RE RSZ",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[RE RSZ - GitHub](https://github.com/alphazolam/RE_RSZ)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                    ["📖 More Info:",       "[RE RSZ - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932644761028939816)",                                                                                                                                           True]
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @commands.command(name="3DSmax - RE-Engine Mesh Tool",
                      description="",
                      usage="{prfx}re_3dsmaxMesh",
                      help="",
                      aliases=["3ds", "3dsmesh", "MaxScript", "ogMS"])
    async def re_3dsmaxMesh(self, ctx):
        desc = "The original Maxscript created for importing and modifying\n RE2 mesh files, now works for all RE Engine games."
        await utils.embed_reply(ctx,
                                title="3DSmax MESH Script - RE-ENGINE MESH TOOL",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[3DSmax MESH - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645540599046204)",                                                                                                                                          True],
                                    ["💻 Developers", "Maliwei777, alphaZomega, MarioKart64n, Shigu and others",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @commands.command(name="3DSmax - alphaZomega Tool",
                      description="",
                      usage="{prfx}alphaZtool",
                      help="",
                      aliases=["3dsalpha", "MaxScriptAlpha", "MSalpha", "AZT"])
    async def alphaZtool(self, ctx):
        desc = "Alpha's Maxscript tool for 3DSmax is a kind of multi-tool used for various mesh-modding related tasks."
        await utils.embed_reply(ctx,
                                title="alphaZomega Tool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[alphaZomega Tool - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645657364287519)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @commands.command(name="3DSmax - ResetMesh",
                      description="",
                      usage="{prfx}resetmesh",
                      help="",
                      aliases=["3dsreset", "MaxScriptReset", "MSreset", "reset"])
    async def ResetMesh(self, ctx):
        desc = "ResetMesh is an older 3dsmax script Alpha made to fix broken meshing without needing to re-import the mesh through Noesis."
        await utils.embed_reply(ctx,
                                title="ResetMesh",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[ResetMesh - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645788826353705)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @commands.command(name="010 - Offset Fixer",
                      description="",
                      usage="{prfx}offsetfixer",
                      help="",
                      aliases=["010offset", "offsetbt"])
    async def OffsetFixer(self, ctx):
        desc = "This universal script can instantly update thousands of offsets in any file."
        await utils.embed_reply(ctx,
                                title="Alpha's Offset Fixer",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Alpha's Offset Fixer - GitHub](https://github.com/alphazolam/Alpha-Offset-Fixer)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                    ["📖 More Info:",       "[Offset Fixer - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932646362795868240)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")


def setup(bot):
    bot.add_cog(REtools(bot))
