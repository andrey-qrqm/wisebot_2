import bot
from sys import argv


if __name__ == '__main__':
    script, TOKEN, AI_TOKEN = argv
    bot.run_discord_bot(TOKEN, AI_TOKEN)