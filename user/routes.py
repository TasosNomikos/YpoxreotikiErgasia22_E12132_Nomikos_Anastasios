from flask import Flask
from app import app 
from user.models import User
    

@app.route("/user/register/", methods  = ['POST'])
def user_register():
    return User().register()

@app.route("/user/login/", methods  = ['POST'])
def user_login():
    return User().login()

@app.route("/user/logout/")
def user_logout():
    return User().logout()

@app.route("/user/new_note/", methods  = ['POST'])
def new_note():
    return User().new_note()

@app.route("/user/delete_note/", methods  = ['GET', 'POST'])
def delete_note():
    return User().delete_note()

@app.route("/user/edit_note/", methods  = ['GET', 'POST'])
def edit_note():
    return User().edit_note()

@app.route("/user/delete/", methods  = ['GET', 'POST'])
def delete_user():
    return User().delete_user()

@app.route("/user/find_note/", methods  = ['GET', 'POST'])
def find_note():
    return User().find_note()

@app.route("/user/update_note/", methods  = ['POST'])
def update_note():
    return User().update_note()