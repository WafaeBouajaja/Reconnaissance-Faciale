import os
import face_recognition
import pickle

# Dossier contenant les visages autorisés
dataset_dir = "authorized_faces"
known_encodings = []
known_names = []

# Parcourir toutes les images
for filename in os.listdir(dataset_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(dataset_dir, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            encoding = encodings[0]
            known_encodings.append(encoding)
            name = os.path.splitext(filename)[0]
            known_names.append(name)
            print(f"[INFO] Encodé : {name}")
        else:
            print(f"[ATTENTION] Aucun visage détecté dans {filename}")

# Sauvegarder les encodages
data = {"encodings": known_encodings, "names": known_names}
with open(os.path.join(dataset_dir, "encodings.pickle"), "wb") as f:
    f.write(pickle.dumps(data))

print("[INFO] Encodage terminé.")
