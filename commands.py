import asyncio
import os
import subprocess
from discord.ext import commands
from resources.shared import registeredDevelopers

def is_developer():
    async def predicate(ctx):
        return str(ctx.author.id) in registeredDevelopers
    return commands.check(predicate)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="panic")
    @is_developer()
    async def panic_command(self, ctx):
        """Initiates a panic procedure."""
        await ctx.send("Panic initiated.")
        await asyncio.gather(
            self.send_notification(ctx),
            self.kill_process(ctx)
        )
        await ctx.send("Panic successful. Exiting...")

    async def send_notification(self, ctx):
        """Sends a system notification for panic."""
        subprocess.run([
            "notify-send", "-u", "critical", "-t", "2000", "Fritz", "Panic code 0x30",
            "--icon", f"/home/{os.getlogin()}/Pictures/fritzSystemIcon.jpeg", "-e"
        ])

    async def kill_process(self, ctx):
        """Kills the Fritz process."""
        process = await asyncio.create_subprocess_exec(
            "pkill", "-f", f"/home/{os.getlogin()}/Documents/Fritz/",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await process.communicate()
