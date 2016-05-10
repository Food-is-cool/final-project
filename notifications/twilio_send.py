from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC09b097a2c9ed4b988fcc213cfe9c0b1a"
AUTH_TOKEN = "e7082eb29c0374aa8445a18a6805303c"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+17023018118",
    from_="+17023027449",
    body="Hey Jenny! Good luck on the bar exam!",
    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg",
)