import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from myfunc import get_rgb_rsv

cred = credentials.Certificate('hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

class UserInfo(object):
    def __init__(self, imgRef, time, location, brightness, cameraModel):
        self.imgRef = imgRef
        self.time = time
        self.location = location
        self.brightness = brightness 
        self.cameraModel = cameraModel 

    def to_dict(self):
        dest = {
            u'imgRef': self.imgRef,
            u'time': self.time,
            u'location': self.location,
            u'brightness': self.brightness,
            u'cameraModel': self.cameraModel
        }

        return dest

    def __repr__(self):
        return(u'UserInfo(imgRef={}, time={}, location={}, brightness={}, cameraModel={})'.format(self.imgRef, self.time, self.location, self.brightness, self.cameraModel))

# usInf = UserInfo(imgRef=u'google.com/smth3/smth4', time=u'2019.02.07 15:33:47', location=u'', brightness=u'', cameraModel=u'')#name=u'Tokyo', state=None, country=u'Japan')
# db.collection(u'UsrInfo').add(usInf.to_dict()) #15:30:47 07.02.2019

docs = db.collection(u'images_test').stream()#document(u'SF')
lst = []
for doc in docs:
    lst.append(doc)

get_rgb_rsv(lst[-1].to_dict()['imageUrl'])

    # print(lst[-1].to_dict()['name'])


###################################
###################################
# from PIL import Image
# import requests
# from io import BytesIO
# response = requests.get(lst[-1].to_dict()['imageUrl'])
# img = Image.open(BytesIO)