import os
from twilio.rest import Client # type: ignore

# Récupération des identifiants depuis les variables d'environnement
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")     
my_number = os.getenv("MY_NUMBER")              

if not account_sid or not auth_token:
    raise RuntimeError("TWILIO_ACCOUNT_SID et TWILIO_AUTH_TOKEN doivent être définis dans les variables d'environnement")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="🚀 Test Twilio : ça marche !",
    from_=twilio_number,
    to=my_number
)

print("[✅ SMS envoyé]")

