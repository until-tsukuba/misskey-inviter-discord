import os
import sys
import requests
import discord
from discord import app_commands

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
MISSKEY_TOKEN = os.environ.get("MISSKEY_TOKEN")
MISSKEY_HOST = os.environ.get("MISSKEY_HOST")
MISSKEY_HOST_URL = os.environ.get("MISSKEY_HOST_URL")

intents = discord.Intents.default()
client = discord.Client(intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('Logged in', file=sys.stderr)
    await tree.sync()

@tree.command(name="invite", description=f"{MISSKEY_HOST}への招待トークンを作成します")
async def invite(interaction: discord.Interaction):
    resp = requests.post(f"{MISSKEY_HOST_URL}/api/invite/create", headers={
        "Authorization": f"Bearer {MISSKEY_TOKEN}"
        })
    if resp.status_code != 200:
        await interaction.response.send('エラーです！')
        print(f"token create err. statuscode: {resp.status_code}. payload: {resp.json()}", file=sys.stderr)
        return
    token = resp.json()
    await interaction.response.send(f'招待トークンは「{token["token"]}」です！\n{MISSKEY_HOST_URL} にアクセスして登録してください')

# Botを実行
client.run(DISCORD_TOKEN)

