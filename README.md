README - Versions FR & EN
🇫🇷 Version Française

# 🎯 Système de Reconnaissance Faciale avec Alertes SMS

Un projet de surveillance intelligent permettant la reconnaissance faciale en temps réel et l’envoi automatique d’alertes SMS  lorsqu’un visage non autorisé est détecté.  
Ce système combine vision par ordinateur, apprentissage automatique et services cloud pour offrir une solution moderne et sécurisée.

---

## ✨ Fonctionnalités
- 📷 Capture vidéo en temps réel via une caméra (webcam ou Raspberry Pi Camera).
- 🧠 Reconnaissance faciale basée sur des encodages pré-enregistrés.
- 📩 Envoi  automatique d’alertes SMS  via l’API  Twilio  lorsqu’un intrus est détecté.
- 📝 Sauvegarde des événements dans un fichier **CSV** (logs).
- ⚡ Traitement optimisé pour des performances en temps réel.
- 👀 Interface visuelle avec **OpenCV** pour le monitoring.

---

## 🛠️ Technologies
- **Python** → Langage principal (3.7+)  
- **OpenCV** → Capture et affichage vidéo (4.0+)  
- **face_recognition** → Détection et encodage des visages (Latest)  
- **dlib** → Traitement d’images (Latest)  
- **Twilio** → API d’envoi de SMS (Latest)  
- **Pickle** → Stockage des encodages (Built-in)  

---

## 📋 Prérequis
- ✅ **Python 3.7 ou supérieur**  
- ✅ Caméra (webcam ou caméra externe)  
- ✅ Compte **Twilio** (pour l’envoi des SMS)  
- ✅ Système d’exploitation : Windows, macOS ou Linux  

---

## ⚙️ Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/WafaeBouajaja/Reconnaissance-Faciale.git
   cd Reconnaissance-Faciale
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

### 🔑 Configuration Twilio
- Créez un fichier `.env` à la racine du projet et ajoutez vos identifiants Twilio :
  ```env
  TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxxxxxxxx
  TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx
  TWILIO_PHONE_NUMBER=xxxxxxxxx
  ALERT_PHONE_NUMBER=xxxxxxxxx
  ```

### 🖼️ Préparation des images de référence
1. Créez un dossier `authorized_faces/`.  
2. Ajoutez-y les photos des personnes autorisées (format **.jpg / .png**).  
3. Générez les encodages en lançant :
   ```bash
   python encode_faces.py
   ```

---

## ▶️ Utilisation
Lancez le système :
```bash
python main.py
```

Le programme va :  
- Activer la caméra et analyser les visages en temps réel.  
- Afficher les noms des personnes reconnues en **vert**.  
- Afficher les visages inconnus en **rouge** avec la mention *“Inconnu”*.  
- Envoyer un SMS d’alerte en cas d’intrus.  
- Enregistrer tous les événements dans `logs.csv`.  

👉 Pour arrêter le programme, appuyez sur **`q`** dans la fenêtre vidéo.

---

## 🏗️ Architecture
📂 Face-Recognition-Alert  
 ├── authorized_faces/      # Photos des personnes autorisées  
 ├── encodings.pickle       # Encodages générés  
 ├── encode_faces.py        # Script d’encodage des visages  
 ├── main.py                # Script principal de reconnaissance  
 ├── test_camera.py         # Test de la caméra  
 ├── requirements.txt       # Dépendances du projet  
 └── logs.csv               # Journal des événements  

---

## 📸 Démonstration
- ✅ **Visages reconnus** : Encadrés en vert avec le nom.  
- ❌ **Visages inconnus** : Encadrés en rouge avec “Inconnu”.  
- 📲 **Alertes SMS** : Confirmation d’envoi en cas d’intrus.  
- 📑 **Logs CSV** : Sauvegarde automatique des événements.  

---

## 👤 Auteur
Projet réalisé dans un but académique et éducatif.  
Auteur : **WAFAE BOUAJAJA**  

🇬🇧 English Version

# 🎯 Facial Recognition System with SMS Alerts

An intelligent surveillance project enabling **real-time facial recognition** and **automatic SMS alerts** when an unauthorized face is detected.  
This system combines computer vision, machine learning, and cloud services to provide a modern and secure solution.

---

## ✨ Features
- 📷 Real-time video capture via camera (webcam or Raspberry Pi Camera).  
- 🧠 Facial recognition based on pre-encoded authorized faces.  
- 📩 **Automatic SMS alerts** via **Twilio API** when an intruder is detected.  
- 📝 Event logging into a **CSV file**.  
- ⚡ Optimized processing for real-time performance.  
- 👀 Visual monitoring interface with **OpenCV**.  

---

## 🛠️ Technologies
- **Python** → Main language (3.7+)  
- **OpenCV** → Video capture and display (4.0+)  
- **face_recognition** → Face detection and encoding (Latest)  
- **dlib** → Image processing (Latest)  
- **Twilio** → SMS sending API (Latest)  
- **Pickle** → Encoding storage (Built-in)  

---

## 📋 Requirements
- ✅ **Python 3.7 or higher**  
- ✅ Camera (webcam or external camera)  
- ✅ **Twilio account** (for SMS sending)  
- ✅ Operating System: Windows, macOS, or Linux  

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

### 🔑 Twilio Setup
- Create a `.env` file at the root of the project and add your Twilio credentials:
  ```env
  TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxxxxxxxx
  TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx
  TWILIO_PHONE_NUMBER=+123456789
  ALERT_PHONE_NUMBER=+987654321
  ```

### 🖼️ Reference Images
1. Create a folder `authorized_faces/`.  
2. Add photos of authorized people (**.jpg / .png**).  
3. Generate encodings by running:
   ```bash
   python encode_faces.py
   ```

---

## ▶️ Usage
Run the system:
```bash
python main.py
```

The program will:  
- Activate the camera and analyze faces in real time.  
- Display recognized faces in **green**.  
- Display unknown faces in **red** with the label *“Unknown”*.  
- Send an SMS alert in case of intruder detection.  
- Log all events into `logs.csv`.  

👉 To stop the program, press **`q`** in the video window.

---

## 🏗️ Architecture
📂 Face-Recognition-Alert  
 ├── authorized_faces/      # Authorized people's photos  
 ├── encodings.pickle       # Generated encodings  
 ├── encode_faces.py        # Encoding script  
 ├── main.py                # Main recognition script  
 ├── test_camera.py         # Camera testing script  
 ├── requirements.txt       # Project dependencies  
 └── logs.csv               # Event logs  

---

## 📸 Demonstration
- ✅ **Recognized faces**: Green box with name.  
- ❌ **Unknown faces**: Red box with “Unknown”.  
- 📲 **SMS Alerts**: Confirmation of SMS sending.  
- 📑 **CSV Logs**: Automatic event saving.  

---

## 👤 Author
Project created for academic and educational purposes.  
Author: **WAFAE BOUAJAJA**  

