# Create a Poll in group [chat_id] using [bot_id] 
# Extract data and plot results using Plotly Express
# Создать опрос в телеграм канале [chat_id] используя
# бот [bot_id], выгрузить данныые и визуалезировать результат

import requests
import json
import plotly.express as px

# 1. Create Poll

base_url = "https://api.telegram.org/bot[bot_id]/"
poll_url = base_url + "sendPoll"

parameters = {
    "chat_id" : "-[chat_id]",              # Telegram Chat Identifier
    "question" : "Do you use Telegram?",   # Poll Question
    "options" : json.dumps(['Yes','No']),  # Voting Options
    "is_anonymous" : True,                 # Show Voters, Bool
    "allows_multiple_answers" : False,     # Allow Multiple Answers in Vote  
    "type" : "regular",                    # Type of Poll -> Normal Poll
    "explanation" : "Test Poll"            # Poll Description 
}

resp = requests.get(poll_url,
					  data=parameters)
resp.json() # show request content

# 2. getUpdates Information
# Get Show all Updates for Bot Interactions
# Eg. if bot is located in group, updates will contain group(chat_id) data

getUpdates_url = base_url + "getUpdates"

parameters = {
    "offset" : "offset_id"
}

resp = requests.get(getUpdates_url,
                    data=parameters)
# list of all updates
lst_updIDs = resp.json()['result'] 

# 3. Show poll results
# Select the desired poll update
# -> if not last, check last_upIDs & select relevant output

options = lst_updIDs[-1]['poll']['options']

# Store poll data in lists
lst_res = []; lst_options = []

for i in options:
    option = i['text']
    votes = i['voter_count']
    lst_res.append(votes)
    lst_options.append(option)
   
# Plot results

px.bar(x=lst_options,
       y=lst_res)
