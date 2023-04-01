# coding:UTF-8 
from flask import Flask, request
from gevent import pywsgi
import api
 
app = Flask(__name__)
 
'''监听'''
@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type')=='private':	
    	uid = request.get_json().get('sender').get('user_id')
    	message = request.get_json().get('raw_message')
	print(message)
    	api.keyword(message, uid)
    if request.get_json().get('message_type')=='group':
    	gid = request.get_json().get('group_id')
    	uid = request.get_json().get('sender').get('user_id')
    	message = request.get_json().get('raw_message') 
    	api.keyword(message, uid, gid) 
    return True
'''
message_type 是消息类型群聊或私聊 uid 是qq号 gid 是群号默认为空
'''
if __name__ == '__main__':
    #app.run(debug=True, host='127.0.0.1', port=8000)
    server = pywsgi.WSGIServer(('127.0.0.1',5701),app)
    server.serve_forever()
