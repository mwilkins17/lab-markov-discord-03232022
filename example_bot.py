import discord
import markov

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("markov"):
        await message.channel.send('No.')

client.run('OTU2MjY4NzM0Njk0MTc0NzYw.YjtwqA.Ct_ROk4t3FH_K9fwYCKtp9a3I_g')