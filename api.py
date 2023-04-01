# coding:UTF-8 
import json
import time
import requests
import re
import random
'''message 是客户端传来的信息'''
''' go-http上看一看基本上就没啥问题'''
def keyword(message, uid, gid = None):  
    if message[0:4] == 'help':
        if(gid==None):
            requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id='+str(uid)+'&message='+'help\n点歌\n setu\nssetu)')
        else:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id='+str(gid)+'&message='+'help\n点歌\n setu\nssetu )')
    
    elif message[0:2] == '点歌':
        if(gid==None):
            requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id='+str(uid)+'&message='+dg(message))
        else:
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id='+str(gid)+'&message='+dg(message))
    
    elif message[0:2] == 'at':
        at()
 
 
    #setu 的 url = 'https://api.ghser.com/random/pc.php'
    #requests
    #别人的API自己的不太好就不放出来了
 
 
def at():
    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id='+'*********//群号'+'&message='+'[CQ:at,qq=all]')
def dg(s):
    a,b = s.split()
    urll = 'https://api.iyk0.com/wymusic/?msg='+b+'&n=1'
    music_api = requests.get(urll).json()
    name = music_api['song']
    autor = music_api['singer']
    img = music_api['img']
    url_url = music_api['url']
    cq = f'[CQ:music,type=custom,audio={url_url},title={name},content={autor},image={img}]'
    return cq;
