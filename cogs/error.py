from discord.ext import commands
import munch
import discord

class error(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        file = open("errors", "a")
        file.write(f'{error}' + '\n')
        file.close()
        embed = discord.Embed(title="An error has occurred", description=f"```{error}```")
        embed.set_footer(text=f"Caused by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    



def setup(client):
    client.add_cog(error(client))