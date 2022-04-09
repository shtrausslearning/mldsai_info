# Send an multiple images to [chat_id] using [bot_id]
# using request library & time libray
# Послать множество картинок в Телеграм чат [chat_id]
# через бот [bot_id] request, используя request,time

import requests
import time

base_url = "https://api.telegram.org/bot[bot_id]/sendPhoto"

# http link to images using list
urls = ['http1','http2']

# caption description using list
descriptions = ['image1','image2']

# image send interval
intervals = 0.1

# cycle through list of http links
for i,url in enumerate(urls):

	# wait intervals before continuing
	time.sleep(intervals)

	# request parameters
	parameters = {
      "chat_id" : "-[chat_id]",
      "photo" : url,
      "caption" : descriptions[i]}

	resp = requests.get(base_url,
                       data = parameters) 
	# print request content
	print(resp.text) 
