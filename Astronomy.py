import discord
from discord.ext import commands,tasks
import requests
import datetime
class Astronomy(commands.Cog):
    """
	Contains astronomy commands such as pic of the day.
	"""
    def __init__(self, client):
        self.client = client 
    @commands.command(name='pic',help="Returns the picture of the day.")
    async def pic(self, ctx: commands.Context):
        url = "https://api.nasa.gov/planetary/apod?api_key=PFmJjSpr3F8mYvFd0DveMBZfQPlqjqXnpfV6LJMD"
        r= requests.get(url)
        result = r.json()
        name = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=N70VM2PR9GWHVUPM').text
        # await ctx.send(result)
        # print(result)
        embed=discord.Embed(title=result['title'], url='https://apod.nasa.gov/apod/astropix.html', description=result['explanation'], color=0x3dffc8)
        # embed.set_thumbnail(url=result['hdurl'])
        a=f"Astronomy Picture of The Day for {datetime.date.today().strftime('%d, %b %Y')}"
        embed.set_author(name=a)
        embed.set_footer(text = f"Requested by {ctx.message.author}", icon_url = ctx.message.author.avatar_url)
        embed.add_field(name=" ⬞",value="  ⬞")

        embed.set_image(url=result['hdurl'])
        await ctx.send(embed=embed)
        # await ctx.send(result['hdurl'])
    @tasks.loop(hours=1)
    async def send_pic(self):
        if datetime.datetime.now().hour !=8:return
        ASTRONOMY_CHANNEL = 564897396801984128
        ctx= self.client.get_channel(ASTRONOMY_CHANNEL)
        url = "https://api.nasa.gov/planetary/apod?api_key=PFmJjSpr3F8mYvFd0DveMBZfQPlqjqXnpfV6LJMD"
        r= requests.get(url)
        result = r.json()
        name = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=N70VM2PR9GWHVUPM').text
        # await ctx.send(result)
        # print(result)
        embed=discord.Embed(title=result['title'], url='https://apod.nasa.gov/apod/astropix.html', description=result['explanation'], color=0x3dffc8)
        # embed.set_thumbnail(url=result['hdurl'])
        a=f"Astronomy Picture of The Day for {datetime.date.today().strftime('%d, %b %Y')}"
        embed.set_author(name=a)
        embed.set_footer(text = f"Requested by Time")
        embed.set_image(url=result['hdurl'])
        embed.add_field(name=" ⬞",value="  ⬞")
        await ctx.send(embed=embed)
        # await ctx.send(result['hdurl'])
def setup(client):
	client.add_cog(Astronomy(client))

