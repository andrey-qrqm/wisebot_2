import discord
import responses
import random_event
from discord.ext import commands

intents = discord.Intents.all()
GUILD_LIST = [1093702980303323177, 1143975152930017352]

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



    @client.slash_command(name="clear", argparse="amount", guild_ids=GUILD_LIST, description="Delete n messages from this text channel")
    async def clear(ctx, arg):
        amount = 20
        if arg:
            amount = int(arg)
        await ctx.respond(str(amount))
        await ctx.channel.purge(limit=amount)

    @client.slash_command(name="role", guild_ids=GUILD_LIST, description="Get a random role")
    async def role(ctx):
        await ctx.respond(random_event.random_role())


    @client.slash_command(name="event", argparse="role", guild_ids=GUILD_LIST, description="Get a random event suitable for your role. Roles list = [top, jng, mid, bot, sup]")
    async def event(ctx, role):
        message_author = responses.get_nickname(str(ctx.author.display_name))
        await ctx.respond("WiseBot хочет чтобы "+ message_author + " "+random_event.event(role))


    @client.slash_command(name="help", guild_ids=GUILD_LIST, description="list of commands")
    async def help(ctx):
        await ctx.respond(responses.handle_response('help', str(ctx.author.display_name) ))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} is writting {user_message} in {channel}')

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