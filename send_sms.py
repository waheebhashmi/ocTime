import os
from twilio.rest import Client

account_sid = '[twilio id]' # Found on Twilio Console Dashboard
auth_token = '[twilio auth token]' # Found on Twilio Console Dashboard

myPhone = '[your number' # Phone number you used to verify your Twilio account
TwilioNumber = '+12512946927' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)


client.messages.create(
	to=myPhone,
	from_=TwilioNumber,
	body='test')


