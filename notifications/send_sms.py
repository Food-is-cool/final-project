from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC09b097a2c9ed4b988fcc213cfe9c0b1a"
auth_token  = "e7082eb29c0374aa8445a18a6805303c"
client = TwilioRestClient(account_sid, auth_token)


message = client.messages.create(body="This is hard coded",
    to="+17023018118",    # Replace with your phone number
    from_="+17029601952") # Replace with your Twilio number
print(message.sid)