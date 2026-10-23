import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from discord.ext import commands

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is online!")

def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=run_http_server, daemon=True).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "http://" in message.content or "https://" in message.content or "discord.gg/" in message.content:
        try:
            await message.delete()
            await message.channel.send(f'{message.author.mention} ممنوع نشر الروابط هنا!')
        except Exception as e:
            print(f"Error: {e}")

    await bot.process_commands(message)

bot.run(os.environ.get("MTM0Mjg3MzYwNzczMDIzNzQ1MQ.GYarx3.41K6fJwmcCPmBNlDRaGruUMG7uOqbFYSmzh3Wo"))
