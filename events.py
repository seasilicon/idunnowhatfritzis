from discord.ext import commands
import logging

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Prints a message when the bot is ready."""
        print("Bot is ready.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handles errors raised during command execution."""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You are not authorized to use this command.")
        else:
            await ctx.send("An error occurred while executing the command.")
            logging.error(f"An error occurred: {error}")
