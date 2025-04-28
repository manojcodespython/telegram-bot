from telethon import TelegramClient, events
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()

api_id = 10705683
api_hash = '7844949a3031003987ea51e99177ad70'
client = TelegramClient('forwarder_session', api_id, api_hash)

source_channel_id = -1001639730549
target_channel_id = -1002262569774

@client.on(events.NewMessage(chats=source_channel_id))
async def handler(event):
    await client.send_message(target_channel_id, event.message)

client.start()
print("✅ Bot is running... Waiting for messages to forward.")
client.run_until_disconnected()
