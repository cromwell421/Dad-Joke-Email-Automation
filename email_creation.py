import yagmail
import os
import json
import requests

sender = os.getenv('SENDER')
receiver = os.getenv('RECIPIENT')

subject = 'Daily Pick Me To Start Your Day'

headers = {"Accept": "application/json"}

#function to make call for dad joke
def get_dad_joke():
  r = requests.get("https://icanhazdadjoke.com/", headers = headers)
  dict = r.json()
  dad_joke = dict["joke"]
  return(dad_joke)

#Run call for dad joke; access gmail api; send email every 15 seconds
contents = get_dad_joke()
yag = yagmail.SMTP(user = sender, password = os.getenv('PASSWORD'))
yag.send(to=receiver, subject = subject, contents = contents)
print("Email Sent")
