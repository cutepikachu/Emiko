# Emiko, a catgirl discord bot.
# (c) CutePikachu / MiteBCool Technology LLC
# Licensed under the MIT License

# Imports
import discord
import random
import logging
import asyncio
from subprocess import call

# Set up logging, to discord.log
logger=logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Initialise the client
client = discord.Client()

# Get the token from token.txt
token = open('token.txt').readline()

# Message handler
@client.event
async def on_message(message):

    # Ignore the message if it's sent from us, so people can't self-command with echo
    if message.author == client.user:
        return

    # Pet command
    if message.content == "+pet":
        line = random.choice(open('responses_pet.txt').readlines())
        await client.send_message(message.channel, line)

    # Ping command
    if message.content == "+ping":
        await client.send_message(message.channel, "Pong!")



    # Poke command
    if message.content == "+poke" or message.content == "+touch":
        line = random.choice(open('responses_poke.txt').readlines())
        await client.send_message(message.channel, line)


    # Echo command
    if message.content.startswith("+echo"):
        fuck = message.content.split('=')
        await client.send_message(message.channel, fuck[1])

    # Exit command
    if message.content == "+exit" or message.content == "+quit":
        if not message.author.id == "235019900618407937":
            line = random.choice(open('responses_unauthorised.txt').readlines())
            await client.send_message(message.channel, line)
        else:
            await client.send_message(message.channel, "See you later!")
            quit()

    # Update command, for easy updating
    if message.content == "+update":
        if not message.author.id == "235019900618407937":
            line = random.choice(open('responses_unauthorised.txt').readlines())
            await client.send_message(message.channel, line)
        else:
            await client.send_message(message.channel, "Updating, brb")
            print("Updating...")
            call(["git", "pull"])
            print("Restarting...")
            call(["run.bat"])
            quit()

    # Restart command
    if message.content == "+restart":
        if not message.author.id == "235019900618407937":
            line = random.choice(open('responses_unauthorised.txt').readlines())
            await client.send_message(message.channel, line)
        else:
            await client.send_message(message.channel, "brb")
            print("Restarting...")
            call(["run.bat"])
            quit()

    # Set game command
    if message.content.startswith("+setgame"):
        if not message.author.id == "235019900618407937":
            line = random.choice(open('responses_unauthorised.txt').readlines())
            await client.send_message(message.channel, line)
        else:
            blah = message.content.split(':')
            await client.change_presence(game=discord.Game(name=blah[1], type=1))
            await message.delete()


# Client ready handler
@client.event
async def on_ready():
    print("Connected to Discord!")
    print("-------")
    print("Bot: " + client.user.name)
    print("Client id:" + client.user.id)
    print("-------")

# Actually log in
client.run(token)