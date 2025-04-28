from telethon import TelegramClient, events

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'  

client = TelegramClient('forwarder_session', api_id, api_hash)


source_channel_id = -1001639730549  # your source channel id
target_channel_id = -1002262569774  # your target channel id

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    await client.send_message(target_channel_id, event.message)
  

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
print("✅ Bot is running...")
client.run_until_disconnected()
