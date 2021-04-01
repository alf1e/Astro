import json
import discord
from discord.ext import commands

class helpCOG(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx, cmd=None):
        embed = discord.Embed(title="Help!", description="commands will be displayed here!")
        embed.set_footer(text=f"Requested by {ctx.author.name} • Custom commands will not be included in help", icon_url=ctx.author.avatar_url)
        data = json.load(open("help.json"))

        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(helpCOG(client))