import random
from discord.ext import commands

class quote(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def quote(self, ctx):
        guild = ctx.guild.id
        if guild == 820748921013796948:
            quote_setter = open("quote", "r")
            quoteconf = quote_setter.read().splitlines()
            if quoteconf == ['Q1']:
                Q1pre = [
                    "It'll all be over soon and then I can go have dinner.",
                    "Oh, no! I've never seen Kestrel be mean before! That's so unexpected and out of character!",
                    "Wake me up when something exciting happens. And make sure it's actually exciting, not Sunny-exciting.",
                    "You said, 'Hey, sparkling teeth, I totally love three if your claws but not the others, and I wish your nose was a herring so I could eat it, and also your wings sound like sharks snoring.",
                    "Why, do you lose a lot of eggs? Maybe whoever's in charge of defense isn't doing a good job, then. Oh, wait, that's you, isn't it?",
                ]
                Q1 = random.choice(Q1pre)
                await ctx.send(Q1)
            if quoteconf == ['Q2']:
                Q2pre = [
                    "Is that an egg? Wow, they work fast in the Kingdom of the Sea. Who's the lucky father?",
                    "MOTHER! I have something DREADFULLY SHOCKING to tell you! NO, this is TOO SHOCKING! WOULD YOU BELIEVE, that my friends--the DRAGONETS OF DESTINY, remember--were CHAINED UP? And STARVED? In YOUR CAVES? By YOUR DRAGONS? I KNOW! It's UNBELIEVABLE! And GEUSS WHO ordered your guards to chain up Clay? COMMANDER SHARK! Of all the dragons who should obey you and everything! Is that not UTTERLY SHOCKING?",
                    "I am saying to your face. Or was I saying it to your rear end? It's easy to get the two confused.",
                    "I AM GOING TO BITE THAT DRAGONS HEAD OFF AND STUFF HIM IN A VOLCANO!!! LETS GO BACK AND KILL HIM AGAIN!",
                    "CHICKENS GIVE UP! WE'RE GOING TO EAT YOU AND THERE'S NOTHING YOU CAN DO ABOUT IT! STOP RUNNING AWAY NOW!",
                ]
                Q2 = random.choice(Q2pre)
                await ctx.send(Q2)



def setup(client):
    client.add_cog(quote(client))