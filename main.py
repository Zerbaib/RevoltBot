import asyncio
import aiohttp
import revolt
from revolt.ext import commands
from config import load_config
import os

# Charger le token et le préfixe depuis config.json
TOKEN, PREFIX = load_config()

class Client(commands.CommandsClient):
    def __init__(self, session, token, prefix):
        super().__init__(session, command_prefix=prefix)
        self.token = token

    async def start(self):
        await super().start(self.token)

# Charger les cogs depuis le dossier "cogs"
def load_cogs(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]  # Retirer l'extension ".py" du nom du fichier
            cog_module = f"cogs.{cog_name}"
            bot.load_extension(cog_module)

async def main():
    async with aiohttp.ClientSession() as session:
        bot = Client(session, TOKEN, PREFIX)
        load_cogs(bot)  # Charger toutes les cogs depuis le dossier "cogs"
        await bot.start()

asyncio.run(main())
