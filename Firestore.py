import random

import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("service-account-file.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def write(nomeProduto):
    doc_ref = db.collection(u'products').document()
    doc_ref.set({
        u'nome': f'{nomeProduto}',
        u'valor': random.randint(0, 3000)
    })
