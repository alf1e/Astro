def initembed(ctx, title, description="", image=None):
    embed = discord.Embed(title=title, description=description)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    if image is not None:
        img = discord.File(f"assets/img/{image}.png", filename=f"{image}.png")
        embed.set_thumbnail(url=f"attachment://{image}.png")
        return munch.munchify({"embed": embed, "file": img})
    else:
        return embed