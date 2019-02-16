import vk_api
import requests
from vk_api.utils import get_random_id
#import datetime
from vk_api import VkUpload 
from main import startParse, conn, cur

###Session Creation
session = requests.Session()
login, password = '+79166463387', '3004990q'
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
    print("Success")
except vk_api.AuthError as error_msg:
    print(error_msg)

work_list = ["Хей, бот", "Оладьи", "Салам"]


###Longpool Creation
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print(event.text)
