#!/usr/bin/python2.7

import vk
import requests
import shutil
import os

# user id
uid='userid'
email='email@example.com'
password='password'

session = vk.Session()
session = vk.AuthSession(app_id='5247537', user_login=email, user_password=password, scope='friends,audio')
api = vk.API(session)

user = api.users.get(user_ids=uid)
audio = api.audio.get(owner_id=int(user[0]['uid']))
for track in audio:
    if type(track) is dict:
        track_dst = './music/' + track['artist'] + ' - ' + track['title']
        if not os.path.isfile(track_dst):
            response = requests.get(track['url'], stream=True)
            with open(track_dst, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            print track_dst + ' ok'
