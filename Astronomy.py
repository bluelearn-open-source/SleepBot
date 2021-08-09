import discord
from discord.ext import commands
import requests
import datetime
class Astronomy(commands.Cog):
    """
	Contains astronomy commands such as pic of the day.
	"""
    def __init__(self, client):
        self.client = client 
    
    @commands.command(name='pic',help="Returns the picture of the day.")
    async def pic(self, ctx):
        url = "https://api.nasa.gov/planetary/apod?api_key=PFmJjSpr3F8mYvFd0DveMBZfQPlqjqXnpfV6LJMD"
        r= requests.get(url)
        result = r.json()
        name = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=N70VM2PR9GWHVUPM').text
        # await ctx.send(result)
        # print(result)
        embed=discord.Embed(title=result['title'], url=result['hdurl'], description=result['explanation'], color=0x9580ff)
        embed.set_author(name=name)
        embed.set_thumbnail(url=result['hdurl'])
        embed.set_footer(text=f"{result['date']} - {name} - (Nasa Pic of the day)[https://apod.nasa.gov/apod/astropix.html] ")
        embed.set_image(url=result['hdurl'])
        await ctx.send(embed=embed)
        await ctx.send(result['hdurl'])

def setup(client):
	client.add_cog(Astronomy(client))

