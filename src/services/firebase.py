from firebase_admin import credentials, initialize_app

def initialize_firebase():
    firebase_credential = credentials.Certificate("firebase-adminsdk.json")
    print("Initializing Firebase default app")
    initialize_app(firebase_credential)
