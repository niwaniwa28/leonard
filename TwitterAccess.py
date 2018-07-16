#coding:utf-8

import os
import io
from twython import Twython
from PIL import Image

class TwitterAccess:

    CONSUMER_KEY =''
    CONSUMER_SECRET =''
    ACCESS_TOKEN =''
    ACCESS_SECRET =''

    def __init__(self):
        print('initialized')

    def tweet(self,text):
        apiInst = Twython(TwitterAccess.CONSUMER_KEY,TwitterAccess.CONSUMER_SECRET,TwitterAccess.ACCESS_TOKEN,TwitterAccess.ACCESS_SECRET)
        apiInst.update_status(status=text)

    def tweetImage(self,text,imgFileNm):
        apiInst = Twython(TwitterAccess.CONSUMER_KEY,TwitterAccess.CONSUMER_SECRET,TwitterAccess.ACCESS_TOKEN,TwitterAccess.ACCESS_SECRET)
        
        photo = Image.open(imgFileNm);
        image_io = io.BytesIO()
        photo.save(image_io, format='JPEG')
        image_io.seek(0)
        
        image_ids = apiInst.upload_media(media=image_io)
        apiInst.update_status(status=text, media_ids=[image_ids['media_id']])
