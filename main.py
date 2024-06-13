import os
import sys
import requests
import discord
from discord import app_commands

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
MISSKEY_TOKEN = os.environ.get("MISSKEY_TOKEN")
MISSKEY_HOST = os.environ.get("MISSKEY_HOST")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('Logged in', file=sys.stderr)
    await tree.sync()

@tree.command(name="invite", description=f"{MISSKEY_HOST}への招待トークンを作成します")
async def invite(interaction: discord.Interaction):
    await interaction.response.defer()
    resp = requests.post(f"https://{MISSKEY_HOST}/api/admin/invite/create", headers={
        "Authorization": f"Bearer {MISSKEY_TOKEN}",
        }, json={})
    if resp.status_code != 200:
        await interaction.followup.send('エラーです！')
        print(f"token create err. statuscode: {resp.status_code}. payload: {resp.json()}", file=sys.stderr)
        return
    tokens = resp.json()
    token = tokens[0]
    if token["expiresAt"] is None:
        await interaction.followup.send(f'招待トークンは「{token["code"]}」です！ https://{MISSKEY_HOST} にアクセスして登録してください')
    else:
        await interaction.followup.send(f'招待トークンは「{token["code"]}」です！{token["expiresAt"]}まで https://{MISSKEY_HOST} にアクセスして登録してください')

# Botを実行
client.run(DISCORD_TOKEN)

