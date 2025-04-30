from telethon import TelegramClient, events
import os
import asyncio

# Read credentials and IDs from environment variables
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
source_channel = int(os.environ.get("SOURCE_CHANNEL"))
target_channel = int(os.environ.get("TARGET_CHANNEL"))

client = TelegramClient('forwarder_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(target_channel, event.message)
        print("✅ Message forwarded!")
    except Exception as e:
        print("❌ Error:", e)

async def main():
    await client.start()
    print("🚀 Bot is running and listening...")
    await client.run_until_disconnected()

asyncio.run(main())
