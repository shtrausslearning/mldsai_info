# Send a text to [chat_id] using [bot_id]
# Послать сообщение в телеграм чат [chat_id] 
# используя бот [bot_id]

import requests

base_url = "https://api.telegram.org/bot[bot_id]/sendMessage"

parameters = {
    "chat_id" : "[chat_id]",
    "text" : "Message"
}

resp = requests.get(base_url,
                    data = parameters)
print(resp.text)
