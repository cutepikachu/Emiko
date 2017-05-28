# Emiko, a catgirl discord bot.
# (c) CutePikachu / MiteBCool Technology LLC
# Licensed under the MIT License

# Imports
import discord
import random
import logging

# Set up logging, to discord.log
logger=logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
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

    if message.content == "+pet":
        line = random.choice(open('responses_pet.txt').readlines())
        await client.send_message(message.channel, line)

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