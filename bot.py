import discord
import responses
from discord.ext import commands

intents = discord.Intents.all()

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, message.author.display_name)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot(TOKEN):
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix='!', intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')




    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} is shitting {user_message} in {channel}')

        if user_message.startswith('!clear'):
            amount = 20
            if '[' in user_message:
                amount = int(user_message[user_message.index('[')+1:user_message.index(']')])
            await message.channel.send(str(amount))
            await message.channel.purge(limit=amount)


        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)




    client.run(TOKEN)