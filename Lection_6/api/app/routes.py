from app import app, db
from app.models import Messages, Users
from flask import request, redirect, make_response, render_template, url_for
from flask_httpauth import HTTPBasicAuth
import datetime
import sqlalchemy

logged = False
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    users = Users.query.all()
    for user in users:
        if user.username == username and user.password == password:
            return username

@app.route('/register', methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        dataUsername = request.form.get('username')
        dataPassword = request.form.get('password')
        db.session.add(Users(username = dataUsername, password = dataPassword))
        db.session.commit()
        return redirect('http://127.0.0.1:5000/chat')
    else:
        return render_template('register.html')


@app.route('/chat')
@auth.login_required
def chat():
    return render_template('chat.html', username = auth.current_user())


@app.route('/send_message')
@auth.login_required
def send_message():
    
    username = auth.current_user()
    message = request.args.get("message")

    db.session.add(Messages(userName=username, message=message, messageDate=datetime.datetime.now()))
    db.session.commit()

    return redirect('http://127.0.0.1:5000/chat', code=302)
    #return redirect('http://192.168.0.102:8080', code=302)


@app.route('/getAll')
def get_all():
    messages = Messages.query.all()
    data = ""
    for message in messages:
        data += "{}: {} [{}]<br>".format(message.userName, message.message, message.messageDate)
    responce = make_response(data)
    responce.headers['Access-Control-Allow-Origin'] = '*'
    return responce