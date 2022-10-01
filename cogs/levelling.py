from PIL import Image, ImageDraw
from discord.ext import commands
import datetime
import asyncio
import discord
import math
import io

# Local imports
from modules import globals, db, utils, xp


class Levelling(commands.Cog,
                description="Everything to do with levels and XP\n"
                            "There are 3 types of XP: level, cred and assistance\n"
                            "You earn level from chatting anywhere (except in bot commands channels)\n"
                            "Cred is only earned by users with modder role and only in modding channels\n"
                            "Assistance XP is generated in the hospital and support channels, everyone earns, modders earn 2x\n"
                            f"When you post a contribution, for example a discord exclusive mod, you gain {globals.CONTRIB_AMOUNT} cred\n"
                            "There are cooldowns on all this, spamming won't get you far"):
    def __init__(self, bot):
        self.bot = bot

    @utils.hybcommand(globals.bot,
                      name="stats",
                      description="See your server stats (level, cred, assistance)",
                      usage="{prfx}stats [ user ]",
                      help="user: the user to check stats for (ping, name, id) (optional)",
                      aliases=["levels", "level", "rank"])
    async def stats(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        level_xp, cred_xp, assistance_xp = await db.get_user_xp(user.id)
        level      = xp.xp_to_lvl(level_xp )
        cred       = xp.xp_to_lvl(cred_xp  )
        assistance = xp.xp_to_lvl(assistance_xp)
        level_next      = math.floor((level [2] - level [1]) * 100 / level [2])
        cred_next       = math.floor((cred  [2] - cred  [1]) * 100 / cred  [2])
        assistance_next = math.floor((assistance[2] - assistance[1]) * 100 / assistance[2])
        # Setup image foundation
        if user.id == globals.ADMIN_ID:
            img = Image.open("assets/backgrounds/staff_bg_MH.png"  )
        elif utils.is_staff(user):
            img = Image.open("assets/backgrounds/staff_bg_MH.png"  )
        else:
            img = Image.open("assets/backgrounds/default_bg_MH.png")
        draw = ImageDraw.Draw(img)
        # Draw user avatar
        if str(user.display_avatar.url).startswith("https://cdn.discordapp.com/embed/avatars"):
            avatar = globals.default_avatar
        else:
            avatar = (await utils.pil_img_from_link(str(user.display_avatar.url))).resize((200, 200,))
        try:
            img.paste(avatar, (24, 18,), avatar)
        except ValueError:
            img.paste(avatar, (24, 18,))
        # Apply base overlay
        if user.id == globals.ADMIN_ID:
            img.paste(globals.overlays_admin_MH,   (0, 0,), globals.overlays_admin_MH  )
        elif utils.is_staff(user):
            img.paste(globals.overlays_staff_MH,   (0, 0,), globals.overlays_staff_MH  )
        else:
            img.paste(globals.overlays_default_MH, (0, 0,), globals.overlays_default_MH)
        # Draw username
        username = user.name.encode('ascii', 'replace').decode('ascii')  # Remove non-ascii glyphs
        utils.draw_text(draw, globals.font35, username, "#FFFFFF", (268, 85,), 298)
        # Draw main level and cred values
        if user.id == globals.ADMIN_ID:
            utils.draw_text(draw, globals.font47, f"LV:{level[0]}", "#F06B02", (277, 141,), 999)
            utils.draw_text(draw, globals.font47, f"SC:{cred[0]}",  "#E10000", (434, 141,), 999)
        else:
            utils.draw_text(draw, globals.font47, f"LV:{level[0]}", "#F06B02", (277, 141,), 999)
            utils.draw_text(draw, globals.font47, f"SC:{cred[0]}",  "#E10000", (434, 141,), 999)
        # Draw trophy shards
        x = 267
        for i in range(utils.get_trophy_amount(user)):
            if i % 2:
                img.paste    (globals.shards_white,  (x, 194,), globals.shards_white )
            else:
                if user.id == globals.ADMIN_ID:
                    img.paste(globals.shards_red,    (x, 194,), globals.shards_red   )
                else:
                    img.paste(globals.shards_orange, (x, 194,), globals.shards_orange)
            x += 32
        # Draw single level values
        if user.id == globals.ADMIN_ID:
            utils.draw_text(draw, globals.font16, f"LVL:",            "#FFFFFF", (275, 425,), 999)
            utils.draw_text(draw, globals.font24, f"{level[0]}",      "#FFFFFF", (308, 423,), 999)
        else:
            utils.draw_text(draw, globals.font16, "LVL:",             "#FFFFFF", (275, 425,), 999)
            utils.draw_text(draw, globals.font24, f"{level[0]}",      "#FFFFFF", (308, 423,), 999)
        utils.draw_text    (draw, globals.font16, "LVL:",             "#FFFFFF", (275, 518,), 999)
        utils.draw_text    (draw, globals.font24, f"{cred[0]}",       "#FFFFFF", (308, 516,), 999)
        if user.id == globals.ADMIN_ID:
            utils.draw_text(draw, globals.font16, f"LVL:",            "#F06B02", (275, 619,), 999)
            utils.draw_text(draw, globals.font24, f"{assistance[0]}", "#F06B02", (308, 617,), 999)
        else:
            utils.draw_text(draw, globals.font16, "LVL:",             "#F06B02", (275, 619,), 999)
            utils.draw_text(draw, globals.font24, f"{assistance[0]}", "#F06B02", (308, 617,), 999)
        # Draw single percentage values
        if level_next >= 100:
            utils.draw_text(draw, globals.font30, "MAX",                "#090D18", (579-globals.font30.getsize("MAX")[0],                398,), 999)
        else:
            utils.draw_text(draw, globals.font30, f"{level_next}",      "#090D18", (565-globals.font30.getsize(f"{level_next}")[0],      398,), 999)
            utils.draw_text(draw, globals.font20, "%",                  "#090D18", (565,                                                 407,), 999)
        if cred_next >= 100:
            utils.draw_text(draw, globals.font30, "MAX",                "#090D18", (579-globals.font30.getsize("MAX")[0],                491,), 999)
        else:
            utils.draw_text(draw, globals.font30, f"{cred_next}",       "#090D18", (565-globals.font30.getsize(f"{cred_next}")[0],       491,), 999)
            utils.draw_text(draw, globals.font20, "%",                  "#090D18", (565,                                                 500,), 999)
        if assistance_next >= 100:
            utils.draw_text(draw, globals.font30, "MAX",                "#090D18", (579-globals.font30.getsize("MAX")[0],                593,), 999)
        else:
            utils.draw_text(draw, globals.font30, f"{assistance_next}", "#090D18", (565-globals.font30.getsize(f"{assistance_next}")[0], 593,), 999)
            utils.draw_text(draw, globals.font20, "%",                  "#090D18", (565,                                                 602,), 999)
        # Overlay percentage bars
        if user.id == globals.ADMIN_ID:
            level_bar      = globals.bars["orange_white"][utils.get_bar_index_from_lvl_percent(level_next     )]
            cred_bar       = globals.bars[ "red_white"  ][utils.get_bar_index_from_lvl_percent(cred_next      )]
            assistance_bar = globals.bars["white_orange"][utils.get_bar_index_from_lvl_percent(assistance_next)]
        else:
            level_bar      = globals.bars["orange_white"][utils.get_bar_index_from_lvl_percent(level_next     )]
            cred_bar       = globals.bars[ "red_white"  ][utils.get_bar_index_from_lvl_percent(cred_next      )]
            assistance_bar = globals.bars["white_orange"][utils.get_bar_index_from_lvl_percent(assistance_next)]
        img.paste(level_bar,      (218, 457,), level_bar     )
        img.paste(cred_bar,       (218, 550,), cred_bar      )
        img.paste(assistance_bar, (218, 650,), assistance_bar)
        # Send the image
        binary = io.BytesIO()
        img.save(binary, format="PNG")
        binary.seek(0)
        await ctx.reply(file=discord.File(binary, filename=username[:16] + ".png"))

    @utils.hybcommand(globals.bot,
                      name="xp",
                      description="See your XP amounts (levels depend on XP amount)\n"
                                  "LVL1 = 1000XP, LVL2 = 2000XP, LVL3 = 3000XP, LVL4 = 4000XP and so on...",
                      usage="{prfx}xp [ user ]",
                      help="user: the user to check xp amounts for (ping, name, id) (optional)",
                      aliases=["xpamount", "levelxp", "levelsxp"])
    async def xp(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        level_xp, cred_xp, assistance_xp = await db.get_user_xp(user.id)
        await utils.embed_reply(ctx,
                                title=f"🔥 {user.name}'s XP:",
                                fields=[
                                    ["Level",      f"{level_xp}",      True],
                                    ["Cred",       f"{cred_xp}",       True],
                                    ["Assistance", f"{assistance_xp}", True]
                                ],
                                thumbnail=user.display_avatar.url)

    @utils.hybgroup(globals.bot,
                    name="top",
                    description="List top ten users per XP type",
                    usage="{prfx}top [ type ]",
                    help="type: either level, cred or assistance (required)",
                    aliases=["top10", "leaderboard", "ranking"],
                    case_insensitive=True)
    async def top(self, ctx):
        if ctx.invoked_subcommand is None:
            await utils.embed_reply(ctx,
                                    title="🏆 Leaderboard Categories:",
                                    description=f"{globals.BOT_PREFIX.lower()}top **level**: Top 10 users for Server Level\n"
                                                f"{globals.BOT_PREFIX.lower()}top **cred**: Top 10 users for Server Cred\n"
                                                f"{globals.BOT_PREFIX.lower()}top **assistance**: Top 10 users for Assistance")

    @utils.hybcommand(globals.bot,
                      group=top,
                      name="level",
                      aliases=[])
    async def top_level(self, ctx):
        top_users = await db.get_top_users(10, "level")
        max_line_length = 34
        lines = []
        lines.append("User:" + "".join([" " for _ in range(max_line_length+2-len("User:")-len("Server Level XP:"))]) + "Server Level XP:")
        for i, row in enumerate(top_users):
            id, level = row
            level = str(level)
            user = globals.bot.get_user(id)
            if user:
                name = str(user.name)
            else:
                name = str(id)
            left = name if len(name) <= (max_line_length-(len(level)+1)) else name[:(max_line_length-(len(level)+1))-3] + "..."
            spacing = "".join([" " for _ in range(max_line_length-len(left)-len(level))])
            line = left + spacing + level
            lines.append(("+ " if i % 2 else "= ") + line)
        await utils.embed_reply(ctx,
                                title="🏆 Server Level Leaderboard:",
                                description="```asciidoc\n" + "\n".join(lines) + "\n```")

    @utils.hybcommand(globals.bot,
                      group=top,
                      name="cred",
                      aliases=[])
    async def top_cred(self, ctx):
        top_users = await db.get_top_users(10, "cred")
        max_line_length = 34
        lines = []
        lines.append("User:" + "".join([" " for _ in range(max_line_length+2-len("User:")-len("Server Cred XP:"))]) + "Server Cred XP:")
        for i, row in enumerate(top_users):
            id, cred = row
            cred = str(cred)
            user = globals.bot.get_user(id)
            if user:
                name = str(user.name)
            else:
                name = str(id)
            left = name if len(name) <= (max_line_length-(len(cred)+1)) else name[:(max_line_length-(len(cred)+1))-3] + "..."
            spacing = "".join([" " for _ in range(max_line_length-len(left)-len(cred))])
            line = left + spacing + cred
            lines.append(("+ " if i % 2 else "= ") + line)
        await utils.embed_reply(ctx,
                                title="🏆 Server Cred Leaderboard:",
                                description="```asciidoc\n" + "\n".join(lines) + "\n```")

    @utils.hybcommand(globals.bot,
                      group=top,
                      name="assistance",
                      aliases=["assist"])
    async def top_assistance(self, ctx):
        top_users = await db.get_top_users(10, "assistance")
        max_line_length = 34
        lines = []
        lines.append("User:" + "".join([" " for _ in range(max_line_length+2-len("User:")-len("Assistance XP:"))]) + "Assistance XP:")
        for i, row in enumerate(top_users):
            id, assistance = row
            assistance = str(assistance)
            user = globals.bot.get_user(id)
            if user:
                name = str(user.name)
            else:
                name = str(id)
            left = name if len(name) <= (max_line_length-(len(assistance)+1)) else name[:(max_line_length-(len(assistance)+1))-3] + "..."
            spacing = "".join([" " for _ in range(max_line_length-len(left)-len(assistance))])
            line = left + spacing + assistance
            lines.append(("+ " if i % 2 else "= ") + line)
        await utils.embed_reply(ctx,
                                title="🏆 Server Assistance Leaderboard:",
                                description="```asciidoc\n" + "\n".join(lines) + "\n```")

    @utils.hybcommand(globals.bot,
                      name="rep",
                      description=f"Gift a cool person some reputation ({globals.REP_CRED_AMOUNT} cred XP)\n"
                                  "Only once every 24 hours (or sooner if the bot restarts)",
                      usage="{prfx}rep [ user ]",
                      help="user: the user to give rep to (ping, name, id) (required)",
                      aliases=["reputation", "giverep", "givereputation"],
                      cooldown_rate=1,
                      cooldown_key=lambda ctx: ctx.author.id,
                      cooldown_time=datetime.timedelta(days=1).total_seconds())
    async def rep(self, ctx, user: discord.Member):
        if user.id == ctx.author.id:
            await utils.embed_reply(ctx,
                                    title="💢 Thats low even by your standards...",
                                    description="No more rep for you today lmao",
                                    ephemeral=False)
            return
        await db.add_user_xp(user.id, cred=globals.REP_CRED_AMOUNT)
        await utils.embed_reply(ctx,
                                content=user.mention,
                                title="💌 You got some reputation!",
                                description=f"{ctx.author.mention} likes what you do and showed their gratitude by gifting you **{globals.REP_CRED_AMOUNT} server cred XP**!",
                                thumbnail=globals.REP_ICON,
                                ephemeral=False)

    @utils.hybcommand(globals.bot,
                      name="daily",
                      description=f"Claim your daily reward ({globals.DAILY_LEVEL_AMOUNT} level XP)\n"
                                  "Only once every 24 hours (or sooner if the bot restarts)",
                      usage="{prfx}daily",
                      help="",
                      aliases=["riseandshine", "ijustwokeup", "gibreward", "claimdaily", "gibdaily"],
                      cooldown_rate=1,
                      cooldown_key=lambda ctx: ctx.author.id,
                      cooldown_time=datetime.timedelta(days=1).total_seconds(),
                      cooldown_title="It's called 'daily' for a reason!",
                      cooldown_desc=False)
    async def daily(self, ctx):
        await db.add_user_xp(ctx.author.id, level=globals.DAILY_LEVEL_AMOUNT)
        await utils.embed_reply(ctx,
                                title="📅 Daily reward claimed!",
                                description=f"You just grabbed yourself a cool **{globals.DAILY_LEVEL_AMOUNT} server level XP**!\n"
                                            f"Come back **tomorrow** for more!",
                                thumbnail=ctx.author.display_avatar.url)


async def setup(bot):
    asyncio.get_event_loop().create_task(xp.tick_cooldowns())
    await bot.add_cog(Levelling(bot))
