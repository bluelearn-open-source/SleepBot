from threading import Thread
import discord
from discord.ext.commands.converter import GuildConverter
from flask import Flask,jsonify
from functools import partial
from discord.ext import commands
from dotenv import load_dotenv
import os
# Getting Token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Initialize our app and the bot itself
app = Flask(__name__)
bot = commands.Bot(command_prefix="!")
partial_run = partial(app.run, host="0.0.0.0", port=5000, debug=True, use_reloader=False)


# Set up the 'index' route
@app.route("/")
def hello():
    return "Hello from {}".format(bot.user.name)

@app.route("/stats")
def stats():
    SERVER_ID = 786066239537020948
    guild:discord.Guild = bot.get_guild(SERVER_ID)
    member_count = guild.member_count
    roles_count=len(guild.roles)
    return jsonify(
        {
        "member_count":member_count,
        "roles_count":roles_count,
        }
        )
t = Thread(target=partial_run)
t.start()

# Run the bot
bot.run(TOKEN)