import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from myfunc import get_rgb_rsv

cred = credentials.Certificate('hackathonproject-257719-firebase-adminsdk-s0ba1-c65e058e66.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

class UserInfo(object):
    def __init__(self, results):
        # self.imgUrl = imgUrl
        # self.time = time
        # self.location = location
        # self.brightness = brightness 
        # self.cameraModel = cameraModel 
        self.results = results
    def to_dict(self):
        dest = {
            u'imgUrl': self.imgUrl,
            u'time': self.time,
            u'location': self.location,
            u'brightness': self.brightness,
            u'cameraModel': self.cameraModel,
            u'results': self.results
        }
        return dest
    def repr(self):
        return(u'UserInfo(imgUrl={}, time={}, location={}, brightness={}, cameraModel={},results={})'.format(self.imgUrl, self.time, self.location, self.brightness, self.cameraModel,self.results))

# usInf = UserInfo(imgRef=u'google.com/smth3/smth4', time=u'2019.02.07 15:33:47', location=u'', brightness=u'', cameraModel=u'')#name=u'Tokyo', state=None, country=u'Japan')
# db.collection(u'UsrInfo').add(usInf.to_dict()) #15:30:47 07.02.2019

docs = db.collection(u'images_test').stream()#document(u'SF')
lst = []
for doc in docs:
    lst.append(doc)

print(get_rgb_rsv(lst[-1].to_dict()['imageUrl']))
arr = get_rgb_rsv(lst[-1].to_dict()['imageUrl'])
# print(type(arr))
# db.collection(u'images_test').document(u'results').set(str(get_rgb_rsv(lst[-1].to_dict()['imageUrl'])))
# data = {
#     u'result': list(arr)#u'Los Angeles',
#     # u'state': u'CA',
#     # u'country': u'USA'
# }

# db.collection(u'images_test').document(u'results').set(data)

usrDataWithResults = UserInfo(results=get_rgb_rsv(lst[-1].to_dict()['imageUrl']))
# lst[-1].add(usrDataWithResults.to_dict())#document(u'SF')
print(lst[-1].to_dict()['imageUrl'])



