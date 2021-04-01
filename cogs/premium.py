import json
import asyncio
import discord
from discord.ext import commands

class profile(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["t"])
    async def tag(self, ctx, tag=None, user: discord.Member=None):
        with open("premium.json", "r+") as f:
            dat = json.load(f)
            data = dat["premium_servers"]
        if str(ctx.guild.id) in data:
            with open("tags.json", "r") as g:
                tags = json.load(g)

            tag_name = f"{ctx.guild.id}/{tag}"
            try:
                if not user:
                    await ctx.send(tags[tag_name])
                    await ctx.message.delete()
                else:
                    await ctx.send(f"{user.mention} Please see the info below: \n {tags[tag_name]}")
                    await ctx.message.delete()
            except Exception:
                await ctx.send('Tag not found')

        else:
            await ctx.reply("⚠️ This is NOT a Premium server! ⚠️")

    @commands.command(aliases=["tCreate"])
    @commands.has_permissions(manage_messages=True)
    async def tagCreate(self, ctx, tag_name, *, tag_info):
        with open("premium.json", "r+") as f:
            dat = json.load(f)
            data = dat["premium_servers"]
        if str(ctx.guild.id) in data:
            with open("tags.json", "r+") as g:
                tags = json.load(g)
                tags[f'{ctx.guild.id}/{tag_name}'] = tag_info
                g.seek(0)
                json.dump(tags, g)
                await ctx.send('Done!')

        else:
            await ctx.reply("⚠️ This is NOT a Premium server! ⚠️")


    # Stolen from https://github.com/TechnoShip123/thonk-bot/blob/master/lib/cogs/utility.py go check em out or bad
    @commands.cooldown(1, 150, commands.BucketType.user)  # Cooldown of 2 uses every 150 seconds per user.
    @commands.command(aliases=["reminder, remindme"])
    async def remind(self, ctx, time, *, reminder):
        with open("premium.json", "r+") as f:
            dat = json.load(f)
            data = dat["premium_users"]
        if str(ctx.author.id) in data:
            user = "<@!" + str(ctx.author.id) + ">"
            embed = discord.Embed(color=0x55a7f7)
            embed.set_footer(text="Requested by: " + ctx.author.name, icon_url=f"{ctx.message.author.avatar_url}")
            seconds = 0
            # If no reminder is specified:
            if reminder is None:
                embed.add_field(name='Warning',
                                value="Please specify what do you want me to remind you about. (after the time interval)")  # Error message
                self.remind.reset_cooldown(ctx)
            elif time[:-1].isnumeric() is False:
                self.remind.reset_cooldown(ctx)
                embed.add_field(name='Warning',
                        value="Please specify a valid time! For example, `5m` for 5 minutes, or `2d for 2 days`!")
            else:
                if time.lower().endswith("d"):
                    seconds += int(time[:-1]) * 60 * 60 * 24
                    counter = f"{seconds // 60 // 60 // 24} day(s)"
                if time.lower().endswith("h"):
                    seconds += int(time[:-1]) * 60 * 60
                    counter = f"{seconds // 60 // 60} hour(s)"
                elif time.lower().endswith("m"):
                    seconds += int(time[:-1]) * 60
                    counter = f"{seconds // 60} minute(s)"
                elif time.lower().endswith("s"):
                    seconds += int(time[:-1])
                    counter = f"{seconds} second(s)"
            if seconds == 0:
                embed.add_field(name='Invalid Duration!',
                                value='Please specify a proper duration, `?!remind <time> <name>`. For example, `?!remind 5m Coding` for a reminder in 5 minutes.')
                self.remind.reset_cooldown(ctx)
            elif seconds < 300:
                embed.add_field(name='Duration Too Small!',
                                value='You have specified a too short duration!\nThe minimum duration is 5 minutes.')
                self.remind.reset_cooldown(ctx)
            elif seconds > 604800:
                embed.add_field(name='Duration Too Large!',
                                value='You have specified too long of a duration!\nThe maximum duration is 7 days.')
                self.remind.reset_cooldown(ctx)
            else:
                await ctx.reply(f"Alright, I will remind you about {reminder} in {counter}.")
                await asyncio.sleep(seconds)
                await ctx.send(f"Hey {user}, you asked me to remind you about {reminder} {counter} ago.")
                return
            await ctx.send(embed=embed)  # Send the embed with the information.
        else:
            await ctx.reply("⚠️ You are NOT a Premium user! ⚠️")
        

def setup(client):
    client.add_cog(profile(client))