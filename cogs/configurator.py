from discord.ext import commands
import os
import sys

class configurator(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def config(self, ctx, configurator=None, action=None, actionconfigurator=None, actionconfigurator2=None):
        if configurator == 'None':
            await ctx.send('`CONFIGURATOR` is a required argument!')
        elif configurator == 'moderation':
            if action == 'enable':
                await ctx.send('enabling `MODERATION` cog')
            elif action == 'disable':
                await ctx.send('disabling `MODERATION` cog')
        elif configurator == 'exec':
            if action == 'doing':
                if actionconfigurator == 'playing':
                    await ctx.send('`playing ...` IS COMMING SOON')
                elif actionconfigurator == 'watching':
                    await ctx.send('`watching ...` IS COMMING SOON')
                elif actionconfigurator == 'listening':
                    await ctx.send('`listening ...` ISCOMMING SOON')
            elif action == 'status':
                await ctx.send('coming soon')
        elif configurator == 'quote':
            if action == 'read':
                file1 = open("quote", "r")
                verify = file1.read().splitlines()
                file1.close()
                await ctx.send(f'The quote modifier is set to `{verify}`')
            elif action == 'set':
                file = open("quote", "w")
                file.truncate(0)
                file.write(actionconfigurator)
                file1 = open("quote", "r")
                file.close()
                setto = file1.read().splitlines()
                await ctx.send(f'Quote modifier has been set to `{setto}`')
        elif configurator == 'error':
            if action == 'read':
                errors = open("errors", "r")
                setto = errors.read()
                await ctx.send('current logged errors include:')
                await ctx.send(f'```{setto}```')
            elif action == 'clear':
                errors_clear = open("errors", "w")
                errors_clear.truncate(0)
                errors_clear.close()
                await ctx.send('`ERROR` has been cleared!')
        elif configurator == 'prefix':
            if action == 'read':
                file1 = open("prefix", "r")
                verify = file1.read().splitlines()
                file1.close()
                await ctx.send(f'The prefix is set to `{verify}`! performing a restart to update the prefix')
            elif action == 'set':
                file = open("prefix", "w")
                file.truncate(0)
                file.write(actionconfigurator)
                file1 = open("prefix", "r")
                file.close()
                setto = file1.read().splitlines()
                await ctx.send(f'Prefix has been set to `{setto}! performing a restart to update the prefix`')
                os.execv(sys.executable, ['python'] + sys.argv)

        


def setup(client):
    client.add_cog(configurator(client))