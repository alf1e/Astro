from discord.ext import commands

class error(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        file = open("errors", "a")
        file.write(f'{error}' + '\n')
        file.close()
        await ctx.send('UhOh an error has occured!')
        await ctx.send(f'`{error}`')
    



def setup(client):
    client.add_cog(error(client))