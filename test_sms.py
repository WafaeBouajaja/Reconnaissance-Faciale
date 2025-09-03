from twilio.rest import Client

# Remplace ces 4 infos par les tiennes depuis https://www.twilio.com/console
account_sid = 'AC89e54523e0c7451aba663133513c8896'
auth_token = 'eae98c953d61f7d77ee1d9ffe6b2a0d1'
twilio_number = '+1 417 742 8375'
my_number = '+212649962872'

# Création du client Twilio
client = Client(account_sid, auth_token)

# Envoi du SMS
message = client.messages.create(
    body="🚀 Test Twilio : ça marche !",
    from_=twilio_number,
    to=my_number
)

print("[✅ SMS envoyé]")
