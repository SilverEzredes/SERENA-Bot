from discord.ext import commands
from typing import Union
import discord

# Local imports
from modules import globals, utils


class Fun(commands.Cog,
          description="Commands for them squad lols"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="herb",
                      description="Roll someone a G+G+G blunt (cosmetic, no rewards)",
                      usage="{prfx}herb [ user ]",
                      help="user: the user to give a blunt to (ping, name, id) (optional)",
                      aliases=["blunt", "based",])
    async def cookie(self, ctx, target: Union[discord.Member, discord.User, int, str] = None):
        # Convert target input to discord.Member
        if not target:
            target = ctx.author
        if isinstance(target, int):
            target = ctx.guild.get_member(target)
        elif isinstance(target, str):
            target = utils.strip_argument(target)
            target = await utils.get_best_member_match(ctx, target)
        elif isinstance(target, discord.User):
            target = ctx.guild.get_member(target.id)
        elif isinstance(target, discord.Member):
            pass
        else:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        if not target:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        # Actual command
        if target.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{target.id}>",
                                    title="🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> just rolled you a G+G+G blunt of the greenest herb🌿!\n"
                                                "A mixture of 3 Green Herbs. Completely restores health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png")
        else:
            await utils.embed_reply(ctx,
                                    title="🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> found some funny looking plant and decided to smoke it🌿!\n"
                                                "Herb that restores partial health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png")

    @commands.command(name="chocobar",
                      description="Treat someone with a delicious SewerChocolate™️ (cosmetic, no rewards)",
                      usage="{prfx}chocobar [ user ]",
                      help="user: the user to give a choco bar to (ping, name, id) (optional)",
                      aliases=["chocolatebar", "sewerchocolate", "choco", "sewerchoco"])
    async def burrito(self, ctx, target: Union[discord.Member, discord.User, int, str] = None):
        # Convert target input to discord.Member
        if not target:
            target = ctx.author
        if isinstance(target, int):
            target = ctx.guild.get_member(target)
        elif isinstance(target, str):
            target = utils.strip_argument(target)
            target = await utils.get_best_member_match(ctx, target)
        elif isinstance(target, discord.User):
            target = ctx.guild.get_member(target.id)
        elif isinstance(target, discord.Member):
            pass
        else:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        if not target:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        # Actual command
        if target.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{target.id}>",
                                    title="🍫 Sewer Chocolate™️!",
                                    description=f"<@!{ctx.author.id}> just delivered you a delicious 🍫 Sewer Chocolate™️🍫!\n"
                                                "Just don't look at the expiration date...",
                                    thumbnail="https://cdn.discordapp.com/emojis/888191417556561980.png")
        else:
            await utils.embed_reply(ctx,
                                    title="🍫 Sewer Chocolate™️!",
                                    description=f"<@!{ctx.author.id}> found some 🍫 chocolate bar looking thing while exploring the sewers.\n"
                                                "Are you really considering eating that?",
                                    thumbnail="https://cdn.discordapp.com/emojis/888191417556561980.png")

    @commands.command(name="pat",
                      description="Pat someone (cosmetic, no rewards)",
                      usage="{prfx}pat [ user ]",
                      help="user: the user to pat (ping, name, id) (optional)",
                      aliases=["pet", "patpat", "patpatpat"])
    async def pat(self, ctx, target: Union[discord.Member, discord.User, int, str] = None):
        # Convert target input to discord.Member
        if not target:
            target = ctx.author
        if isinstance(target, int):
            target = ctx.guild.get_member(target)
        elif isinstance(target, str):
            target = utils.strip_argument(target)
            target = await utils.get_best_member_match(ctx, target)
        elif isinstance(target, discord.User):
            target = ctx.guild.get_member(target.id)
        elif isinstance(target, discord.Member):
            pass
        else:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        if not target:
            await utils.embed_reply(ctx,
                                    title="💢 That is not a valid user!")
            return
        # Actual command
        if target.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{target.id}>",
                                    title="<a:PatPatPat:836341685952184388> \*PatPat\*",
                                    description=f"<@!{ctx.author.id}> just delivered you a truckload of heartfelt pats!\n"
                                                "Cheer up pal, you're a wonderful person!",
                                    thumbnail="https://cdn.discordapp.com/emojis/889187488915128421.gif")
        else:
            await utils.embed_reply(ctx,
                                    title="<a:PatPatPat:836341685952184388> \*PatPat\*",
                                    description=f"<@!{ctx.author.id}> doesn't have any friends yet so they tried consoling themselves with a few pats!\n"
                                                "Cheer up pal, life gets better!",
                                    thumbnail="https://cdn.discordapp.com/emojis/889190978001465476.gif")


def setup(bot):
    bot.add_cog(Fun(bot))
