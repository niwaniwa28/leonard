#coding:UTF-8

import time
import datetime

from twython import Twython

import TwitterAccess


dateTimeFormat = "%Y/%m/%d %H:%M:%S"
filePath = '/tmp/motion/capture.jpg'

twitter = TwitterAccess.TwitterAccess()

current_time = datetime.datetime.now().strftime(dateTimeFormat)

textTweet = 'ゲンザイノ ニチジハ ' + current_time + ' ウゴキガ アリマシタ.'

print(filePath)

time.sleep(1)

twitter.tweetImage(textTweet, filePath)

print('success tweeted.')
