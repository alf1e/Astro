import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import io
import json
import sys
from func.sysfunc import *

file1 = open("prefix", "r")
verify = file1.read()
file1.close()

client = commands.Bot(command_prefix = f"{verify}")
client.remove_command('help')

@client.event
async def on_ready():
  ready = client.get_channel(820771240561475635)
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{verify}help'))

  print('We have logged in as {0.user}'.format(client))
  print(f"======================================")

  client.load_extension("cogs.configurator")
  client.load_extension("cogs.quote")
  client.load_extension("jishaku")
  client.load_extension("cogs.premium")
  client.load_extension("cogs.error")
  client.load_extension("cogs.economy.work")
  client.load_extension("cogs.economy.profile")
  client.load_extension("cogs.economy.shop")
  client.load_extension("cogs.help")
  loaded = discord.Embed(
    colour = discord.Colour.orange()
    )
  loaded.add_field(name ='I am loaded!', value ='yay', inline=False)
  loaded.add_field(name ='Prefix', value =f'My prefix is {verify}', inline = False)
  loaded.add_field(name ='Loaded COGS:', value ='cogs hold my code', inline=False)
  for extension in os.listdir("cogs"):
      loaded.add_field(name =f'{extension}', value =f"{extension} is loaded", inline=False)
  await ready.send(embed=loaded)

@client.command()
@commands.is_owner()
async def shutdown(ctx):
  await ctx.send('Shutting down!')
  preshut = discord.Embed()
  chnl = client.get_channel(820771240561475635)
  preshut.set_author(name='Shutting down!')
  await chnl.send(embed=preshut)
  shut = discord.Embed(
    colour = discord.Colour.orange()
    )
  shut.set_author(name='Shutdown!')
  await chnl.send(embed=shut)
  await client.change_presence(status=discord.Status.offline, activity=discord.Game(name='Offline'))
  exit()

@client.command()
@commands.is_owner()
async def premiserv(ctx, servid):
  with open("premium.json", "r+") as f:
    data = json.load(f)
    f.seek(0)
    data['premium_servers'].append(servid)
    json.dump(data,f)
    await ctx.message.add_reaction('✅')

@client.command()
@commands.is_owner()
async def premiuser(ctx, servid):
  with open("premium.json", "r+") as f:
    data = json.load(f)
    f.seek(0)
    data['premium_users'].append(servid)
    json.dump(data,f)
    await ctx.message.add_reaction('✅')

@client.command()
@commands.is_owner()
async def error(ctx):
  await ctx.reply("Doing le error")
  raise Exception(f"Le Fake error of {ctx.author.name}")

@client.command()
@commands.is_owner()
async def restart(ctx):
  embed = discord.Embed(title="Restarting!", description="Cya later!")
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  await ctx.reply(embed=embed)
  os.execv(sys.executable, ['python'] + sys.argv)

client.run(os.getenv('TOKEN'))