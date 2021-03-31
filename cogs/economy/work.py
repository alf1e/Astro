import random
import asyncio
import json
import discord
from discord.ext import commands

class economy(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def work(self, ctx):
        await ctx.send('Loading...')

        async def setup_money(self, user):
            with open('money.json', 'r') as f:
                users = json.load(f)
            if not f'{user.id}' in users:
                users[f'{user.id}'] = {}
                users[f'{user.id}']['balance'] = 0
            with open('money.json', 'w') as f:
                json.dump(users, f)
    
        async def add_money(self, user, money):
            with open('money.json', 'r') as f:
                users = json.load(f)
                users[f'{user.id}']['balance'] += money
                with open('money.json', 'w') as g:
                    json.dump(users, g)
        
        async def setup_profile(self, user):
            with open('profile.json', 'r') as f:
                users = json.load(f)
            if not f'{user.id}' in users:
                users[f'{user.id}'] = {}
                users[f'{user.id}']['publishness'] = 0
                users[f'{user.id}']['JobsAttempted'] = 0
            with open('profile.json', 'w') as f:
                json.dump(users, f)
    
        async def add_has_worked(self, user, money):
            with open('profile.json', 'r') as f:
                users = json.load(f)
                users[f'{user.id}']['JobsAttempted'] += 1
                with open('profile.json', 'w') as g:
                    json.dump(users, g)

        money_to_get = random.randint(1,5)

        pre_sentance = [
            "Hello how are you",
            "Hi i am a user",
            "Dank memer is bad",
            "i am rich",
        ]

        sentance = random.choice(pre_sentance)

        def check(message):
            if message.author == ctx.author:
                return True

        sentence_message = await ctx.send(content=f'Send the sentance `{sentance}`')
        await asyncio.sleep(0.5)
        await sentence_message.delete()
        await ctx.send(content='GO!')
        user_sentaance = await self.bot.wait_for('message', check=check)
        if user_sentaance.content == sentance:
            await ctx.send(f'GREAT JOB {ctx.author.mention}, you were awarded {money_to_get} coins for your efforts!')
            await setup_money(self, ctx.author)
            await add_money(self, ctx.author, money_to_get)
            await setup_profile(self, ctx.author)
            await add_has_worked(self, ctx.author, money_to_get)
        else:
            await ctx.send(f'`{user_sentaance.content}` is incorrect the correct one was `{sentance}`!')

    @commands.command(no_pm=True, aliases=["bal"])
    async def balance(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('money.json', 'r') as f:
               users = json.load(f)
            lvl = users[str(id)]['balance']
            await ctx.send(f'You have {lvl} coins!')
        else:
            id = member.id
            with open('money.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['balance']
            await ctx.send(f'{member} has {lvl} coins!')


def setup(client):
    client.add_cog(economy(client))