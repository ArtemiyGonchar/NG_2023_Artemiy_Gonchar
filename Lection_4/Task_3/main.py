import os
from flask import Flask, render_template, request

server=Flask("server")
filename_list = os.listdir('static/images/')
@server.route('/')
def index():
    if(request.args.get('image') == '' or request.args.get('image') == None):
        imageName = filename_list[0]
    else:
        imageName = request.args.get('image')
    imageIndex = filename_list.index(imageName)
    action = request.args.get('action')
    if action == 'next':
        if imageIndex == (len(filename_list) - 1):
            imageIndex = 0
        else:
            imageIndex += 1
    else:
        imageIndex -= 1
    imageName = filename_list[imageIndex]
    return render_template("index.html", data = imageName)


server.run(host="0.0.0.0", port=8080)