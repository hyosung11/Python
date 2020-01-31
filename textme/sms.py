from twilio.rest import Client
import config

account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+16102981505',
    to='+12012544696',
    body='I am the milkman of human kindness ... test'
)

print(message.sid)
