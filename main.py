import cv2
import face_recognition
import pickle
import os
import datetime
from twilio.rest import Client

# --- Configuration Twilio ---
account_sid = 'AC89e54523e0c7451aba663133513c8896'  # Remplace par ton SID Twilio
auth_token = 'eae98c953d61f7d77ee1d9ffe6b2a0d1'    # Remplace par ton token d’auth
twilio_number = '+1 417 742 8375'  # Numéro Twilio
my_number = '+212649962872'        # Ton numéro perso

client = Client(account_sid, auth_token)

def send_sms_alert():
    message = client.messages.create(
        body="🚨 Visage inconnu détecté !",
        from_=twilio_number,
        to=my_number
    )
    print("[SMS envoyé]")

def log_alert(name):
    with open("alertes.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{name}\n")

# Charger les encodages
with open(os.path.join("authorized_faces", "encodings.pickle"), "rb") as f:
    data = pickle.load(f)

# Démarrer la caméra
video = cv2.VideoCapture(0)

# Pour éviter d’envoyer trop de SMS en boucle pour le même inconnu
alert_sent = False

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Redimensionner pour accélérer
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Détection + encodage
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(data["encodings"], face_encoding)
        name = "Inconnu"

        if True in matches:
            match_index = matches.index(True)
            name = data["names"][match_index]
            alert_sent = False  # Reset si visage connu détecté
        else:
            log_alert(name)
            if not alert_sent:
                send_sms_alert()
                alert_sent = True

        # Affichage rectangle et nom
        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 0, 255), 2)

    cv2.imshow("Surveillance Faciale", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
