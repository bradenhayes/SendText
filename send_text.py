import schedule
import time
import requests

x=0
def send_Text():
    global x
    thoughts = 
    payload = {
            'phone': 'xxxxxxxx', 
            'message': thoughts[x], 
            'key':'xxxxxxxxxxx'
          }

    resp = requests.post('https://textbelt.com/text', payload)

    print(resp.json())

    x+=1

schedule.every().day.at('06:00').do(send_Text)

while 1:
    schedule.run_pending()
    time.sleep(1)
