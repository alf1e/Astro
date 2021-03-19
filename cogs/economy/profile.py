import random
import asyncio
import json
import discord
from discord.ext import commands

class profile(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def profile(self, ctx):
        id = ctx.message.author.id
        msg = await ctx.send('Gathering info!')
        with open("profile.json", "r") as f:
            users = json.load(f)
        
        embed = discord.Embed(
        colour = discord.Colour.orange()
        )

        username = ctx.author.name
        publishness = users[str(id)]['publishness']
        has_worked = users[str(id)]['JobsAttempted']

        if publishness == 1:
            await ctx.send('This profile is private!')
        else:
            embed.set_author(name="Your profile!")
            embed.add_field(name=f"**{username}**", value="\u200b", inline=False)
            embed.add_field(name=f"Has worked", value=f"{username} has worked {has_worked} times", inline=False)
            await msg.edit(embed=embed)



def setup(client):
    client.add_cog(profile(client))