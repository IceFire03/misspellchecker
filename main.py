
from spellchecker import SpellChecker
import discord
from discord import app_commands
from keep_alive import keep_alive

keep_alive()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
admins = [850446900209516594]
exemptions = ["lol", "lmao"]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from bots

    words = message.content.split()
    spell = SpellChecker()

    invalid_words = [word for word in words if word not in spell and word.lower() not in exemptions]

    if invalid_words:
        if len(invalid_words) > 1:
            invalid_word_list = ', '.join(invalid_words[:-1])
            invalid_word_list += f", and {invalid_words[-1]}"
            reply = f"Spell better. {invalid_word_list} are not words."
        else:
            reply = f"Spell better. {invalid_words[0]} is not a word."
        await message.reply(reply)


client.run('what are you looking for??')
