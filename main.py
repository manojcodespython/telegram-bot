from telethon.sync import TelegramClient, events

# Your Telegram API credentials
api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'

# Session Name
client = TelegramClient('forwarder_session', api_id, api_hash)

# Source and Target Channel IDs
source_channel = -1001639730549
target_channel = -1002262569774

# Start listening to new messages
@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    try:
        await client.send_message(target_channel, event.message)
        print(f"✅ Forwarded a message from Source ID {source_channel} to Target ID {target_channel}")
    except Exception as e:
        print(f"❌ Error while forwarding: {e}")

print("🚀 Forwarder Bot is running...")
client.start()
client.run_until_disconnected()
