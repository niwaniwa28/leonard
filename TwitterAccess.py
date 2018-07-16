#coding:utf-8

import os
import io
import json
from twython import Twython
from PIL import Image

class TwitterAccess:

    jsonKey = {}
    
    def __init__(self):
        basePath = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.normpath(os.path.join(basePath, './twkey.json'))
        
        fileKey = open(filePath)
        self.jsonKey = json.load(fileKey)
        fileKey.close()
        
        print('TwitterAccess initialized')

    def tweet(self,text):
        apiInst = Twython(self.jsonKey['CONSUMER_KEY'],self.jsonKey['CONSUMER_SECRET'],self.jsonKey['ACCESS_TOKEN'],self.jsonKey['ACCESS_SECRET'])
        apiInst.update_status(status=text)

    def tweetImage(self,text,imgFileNm):
        apiInst = Twython(self.jsonKey['CONSUMER_KEY'],self.jsonKey['CONSUMER_SECRET'],self.jsonKey['ACCESS_TOKEN'],self.jsonKey['ACCESS_SECRET'])
        
        photo = Image.open(imgFileNm);
        image_io = io.BytesIO()
        photo.save(image_io, format='JPEG')
        image_io.seek(0)
        
        image_ids = apiInst.upload_media(media=image_io)
        apiInst.update_status(status=text, media_ids=[image_ids['media_id']])
