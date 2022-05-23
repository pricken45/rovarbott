import discord
from discord.ext import commands

TOKEN = "OTc4MzE5ODU1OTE4OTMyMDE5.GS224m.twzvOcmCBgFGt1os0vvi0IJ2IhKYsuNYIusdNM"

def rovare(txt):
    import requests
    return requests.post('https://rovare.herokuapp.com/rovar', json = {'text': txt}).text[11:].removesuffix('"}')


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def rs(ctx, *args):
    text = " ".join(args)
    await ctx.send("Översättning: " + rovare(text))

bot.run(TOKEN)