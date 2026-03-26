# Updated code to integrate with Polymarket API, handle Discord alerts, and utilize a config file

import requests
import discord
import json

# Load configuration from config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Function to interact with Polymarket API
def get_market_data():
    response = requests.get('https://api.polymarket.com/v1/markets')
    return response.json()

# Function to send alert to Discord
async def send_discord_alert(message):
    client = discord.Client()
    @client.event
    async def on_ready():
        channel = client.get_channel(config['discord_channel_id'])
        await channel.send(message)
        await client.close()

    await client.start(config['discord_token'])

# Example usage
if __name__ == '__main__':
    market_data = get_market_data()
    alert_message = f"Market Data: {market_data}"
    import asyncio
    asyncio.run(send_discord_alert(alert_message))