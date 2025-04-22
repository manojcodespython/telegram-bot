rom telethon import TelegramClient, events

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'  

client = TelegramClient('forwarder_session', api_id, api_hash)


source_channel = '@EU Gold VIP1, @GKFX VIP2, @ICT CHART PREMIUM (lifetime = monthly)3'   
target_channel = '@Combination forex VIP'  

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
print("✅ Bot is running...")
client.run_until_disconnected()
