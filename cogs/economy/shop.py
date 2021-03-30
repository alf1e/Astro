import discord
import json
from discord.ext import commands

class shop(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def shop(self, ctx, *, buy=None):
        if not buy:
            embed = discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name="Shop!")
            embed.add_field(name="**Item 1: **Fishing Rod", value="Fishing Rod, **COST**: 30⏣", inline=False)
            #embed.add_field(name="**Item 2: **Hunting Rifle", value="Hunting Rifle, **COST**: 150⏣ + Gun license💳", inline=False)
            #embed.add_field(name="**Item 3: **Gun License💳", value="Gun License💳, **COST**: 100⏣ + Level 5 Gun Skill", inline=False)
            #embed.add_field(name="**Item 4: **Pet dog", value="Pet dog, **COST**: 500⏣ + Pet license💳", inline=False)
            #embed.add_field(name="**Item 5: **Pet cat", value="Pet cat, **COST**: 500⏣ + Pet license💳", inline=False)
            #embed.add_field(name="**Item 6: **Pet license💳", value="Pet license💳, **COST**: 250⏣ + Level 5 pet skill", inline=False)
            embed.add_field(name="**Item 2: **Book", value="Book, **COST**: 10⏣", inline=False)
            embed.add_field(name="**Item 3: **Laptop", value="Laptop, **COST**: 999⏣", inline=False)
            embed.set_footer(text="**Some items unavalible due to Skills not currently existing!** Item purchasing is case sensitive.")

            await ctx.send(embed=embed)
        else:
            with open('money.json', 'r') as f:
                users = json.load(f)
            lvl = users[f"{ctx.author.id}"]['balance']

            if buy == 'Fishing Rod':
                if lvl > 30:
                    users[f'{ctx.author.id}']['balance'] -= 30
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
                else:
                    await ctx.reply('You dont meet the requirements!')
            elif buy == 'Book':
                if lvl > 10:
                    users[f'{ctx.author.id}']['balance'] -= 10
                    with open('money.json', 'w') as f:
                        json.dump(users, f)
                else:
                    await ctx.reply('You dont meet the requirements!')
    
    @commands.command(no_pm=True)
    async def inv(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('inventory.json', 'r') as f:
               users = json.load(f)
            lvl = users[str(id)]
            await ctx.send(f'We are currently working on a translator for this!')
            await ctx.send(f'```{lvl}```')
        else:
            id = member.id
            with open('inventory.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]
            await ctx.send(f'We are currently working on a translator for this!')
            await ctx.send(f'```{lvl}```')



def setup(client):
    client.add_cog(shop(client))