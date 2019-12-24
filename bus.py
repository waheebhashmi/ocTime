import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
import requests

URL = 'https://ocbustracker.com/BusData.aspx?stopno=8403&busnum0=44&direction0=0&agency=OC'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

bus_time = soup.find("span",{'class':'ui-li-count ui-btn-up-c ui-btn-corner-all'}).text


app = Flask(__name__)

print(bus_time)


@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
	resp = MessagingResponse()
	resp.message(f'Bus comes in: {bus_time}')
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
