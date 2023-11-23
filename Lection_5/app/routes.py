from app import app, db
from app.models import Users, Messages
from flask import Flask, render_template, request, redirect
import sqlalchemy


@app.route('/register', methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        dataUsername = request.form.get('username')
        dataPassword = request.form.get('password')
        db.session.add(Users(username = dataUsername, password = dataPassword))
        db.session.commit()
        return redirect('/all')
    else:
        return render_template('register.html')


@app.route('/send', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usersValidation = Users.query.all()
        usernameData = request.form.get('username')
        passwordData = request.form.get('password')
        messageData = request.form.get('message')
        
        for user in usersValidation:
            if user.username == usernameData and user.password == passwordData:
                db.session.add(Messages(message = messageData, userId = user.id))
                db.session.commit()
                return redirect('/all')
        return "Invalid username or password! (Maybe you are not registered)"
    return render_template("send.html")

@app.route('/all', methods=['POST', 'GET'])
def all():
    responce = []
    messages = Messages.query.all()

    for messageAndId in messages:
        user = db.session.query(Users.username).filter(Users.id == messageAndId.userId).scalar()
        responce.append("{} says:{}".format(user, messageAndId.message))
    return render_template('all.html', postMessages = responce)