from firebase_admin import credentials, initialize_app

def initialize_firebase(name=None):
    firebase_credential = credentials.Certificate("firebase-adminsdk.json")
    initialize_app(firebase_credential, name)