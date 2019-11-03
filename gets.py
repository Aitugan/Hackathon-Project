import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('hackathonproject-257719-f77ef84ee100.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'images_text').#.document(u'LA')

try:
    doc = doc_ref.get()
    # print(u'Document data: {}'.format(doc.to_dict()))
    print(doc.to_dict()['date'])#['image'])
except Exception:#google.cloud.exceptions.NotFound:
    print("Error handled!")#u'No such document!')

##############################################################################################
# from google.cloud import storage
# from firebase import firebase
# import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.json"
# firebase = firebase.FirebaseApplication('<your firebase database path>')
# client = storage.Client()
# bucket = client.get_bucket('<your firebase storage path>')
# # posting to firebase storage
# imageBlob = bucket.blob("/")
# # imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
# imagePath = "bgi.png"
# imageBlob = bucket.blob("bgi")
# imageBlob.upload_from_filename(imagePath)
###############################################################################################

# import sys
# import requests
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage

# image_url = 'https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'#sys.argv[1] #we pass the url as an argument

# cred = credentials.Certificate('hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.web.app'#'<mysuperstorage>.appspot.com'
# })
# bucket = storage.bucket()

# image_data = requests.get(image_url).content
# blob = bucket.blob('bgi.png')
# blob.upload_from_string(
#         image_data,
#         content_type='image/png'
#     )
# print(blob.public_url)
###################################################################################################


# import sys
# import requests
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage
# from firebase_admin import db
# import pyrebase

# cred = credentials.Certificate('hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL':'https://hackathonproject.firebaseio.com'
# })

# ref = db.reference('restricted_access/secret_document')
# print(ref.get())


# db = firestore.client()

# docs = db.collection(u'UsrInfo').stream()#document(u'SF')
# lst = []
# for doc in docs:
#     lst.append(doc)
# try:
#     # BirzhansFunction(format(lst[-1].to_dict())['imgRef']))
#     print(lst[-1].to_dict()['imgRef'])
#     print(lst[-1].to_dict()['time'])

# except Exception:
#     print(u'No such document!')
##########################################################################################################

