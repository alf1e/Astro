import munch

def initembed(ctx, title, description=""):
    embed = discord.Embed(title=title, description=description)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    return embed