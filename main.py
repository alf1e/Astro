import discord 
from discord.ext import commands
import os
import contextlib
from dotenv import load_dotenv
load_dotenv()
import io
import textwrap

file1 = open("prefix", "r")
verify = file1.read()
file1.close()

client = commands.Bot(command_prefix = f"{verify}")
#client.remove_command('help')

@client.event
async def on_ready():
  ready = client.get_channel(820771240561475635)
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name='d.'))
  print('We have logged in as {0.user}'.format(client))
  client.load_extension("cogs.configurator")
  client.load_extension("cogs.quote")
  client.load_extension("cogs.error")
  client.load_extension("cogs.economy.work")
  client.load_extension("cogs.economy.profile")
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
@commands.has_permissions(manage_messages=True)
async def shutdown(ctx):
  await ctx.send('Shutting down!')
  preshut = discord.Embed(
    colour = discord.Colour.orange()
    )
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
async def eval(ctx, *, code):
  id = str(ctx.author.id)
  if id == '677252870722027549':
    eval(code)
    await ctx.send(f'{ctx.author.mention}, your eval has been run and sent to the console!')


client.run(os.getenv('TOKEN'))