# Using request library & url link to send a quiz/poll
# to [chat_id] using created bot[X] identifier
# Создать квиз на канале [chat_id] используя бот [bot_id]

import requests
import json

base_url = "https://api.telegram.org/bot[bot_id]/sendPoll"

parameters = {
    "chat_id" : "-[chat_id]",               # Telegram Chat Identifier 
    "question" : "How much is 3+3?",        # Poll Question
    "options" : json.dumps(['3','6','9']),  # Voting Options
    "is_anonymous" : True,                  # Show Voters, Bool
    "type" : "quiz",                        # Type of Poll -> Quiz  
    "correct_option_id": 2,                 # Select Correct Answer
    "explanation" : "Test Quiz"             # Poll Description 
}

resp = requests.get(base_url,
                data=parameters)
resp.json()
