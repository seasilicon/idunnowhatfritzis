import asyncio
import logging
from discord.ext import commands
from resources.shared import CONFIG, TOKEN, intents
from commands import Commands
from events import Events

# Configure logging
logging.basicConfig(filename='discord_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Discord client
bot = commands.Bot(command_prefix="Hey Fritz, ", intents=intents)

# Load extensions
bot.add_cog(Commands(bot))
bot.add_cog(Events(bot))

# Start the bot
async def start_bot():
    try:
        print(f"Starting with personality {CONFIG['personality']}")
        await bot.start(TOKEN)
    except Exception as err:
        logging.error(f"Failed to start bot: {err}")

asyncio.run(start_bot())
