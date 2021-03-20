import discord
from discord.ext import commands

class profile(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def shop(self, ctx, *, buy=None):
        if not buy:
            embed = discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name="Shop!")


            await ctx.send(embed=embed)
        else:
            await ctx.send('Purchasing coming soon!')


def setup(client):
    client.add_cog(profile(client))