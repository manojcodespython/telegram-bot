from telethon import TelegramClient, events
import os
import asyncio

# Load credentials
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# Map each source channel to its target channel
channel_map = {
    -1002527087260: -1002658790774,  # VIP 🤑 ➝ VIP fx
    -1001639730549: -1002262569774,  # EU Gold VIP ➝ Combination forex VIP
}

# Create the Telegram client
client = TelegramClient('forwarder_session', api_id, api_hash)

# Event listener for all mapped source channels
@client.on(events.NewMessage(chats=list(channel_map.keys())))
async def forward(event):
    try:
        source = event.chat_id
        target = channel_map.get(source)
        if target:
            await client.send_message(target, event.message)
            print(f"✅ Forwarded from {source} ➝ {target}")
        else:
            print(f"⚠️ No target defined for source {source}")
    except Exception as e:
        print(f"❌ Error while forwarding: {e}")

# Start the bot
async def main():
    await client.start()
    print("🚀 Multi-channel forwarder bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
