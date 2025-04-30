from telethon import TelegramClient, events

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

source_channel = -1001639730549
target_channel = -1002262569774

client = TelegramClient('forwarder_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    try:
        await client.send_message(target_channel, event.message.message)
        print(f"✅ Forwarded from {source_channel} to {target_channel}")
    except Exception as e:
        print(f"❌ Error forwarding: {e}")

async def main():
    await client.start()
    print("🚀 Forwarder Bot is running and listening...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
