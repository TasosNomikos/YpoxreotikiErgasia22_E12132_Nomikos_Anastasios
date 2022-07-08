from flask import Flask, render_template, request, session, redirect
from functools import wraps
import pymongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'Pliroforiaka_Yonson21'

#---------Database-----------

client = pymongo.MongoClient('localhost', 27017)
db = client.DigitalNotes

#---------Login-------------

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect('/');

    return wrap
  
# ---------Routes------------
from user import routes


@app.route("/")
def login ():
    return render_template("login.html")

@app.route("/register/")
def register ():
    return render_template("register.html")

@app.route("/main/")
@login_required
def main():
    results = db.users.find_one({"_id":session['user'].get("_id")}).get('note')
    if(results):
        noNotes= len(results)
    else:
        noNotes = 0
    return render_template("main.html", results = results, noNotes = noNotes)    

@app.route("/note/")
def note():
    return render_template("note.html")

@app.route("/findNote/")
def findNote():
    search = request.args.get("search")
    res = db.users.find_one({"note": {"$elemMatch": {"title": search}}})
    return render_template("findNote.html", res = res['note'])

@app.route("/editNote/")
def editNote():
    search = request.args.get("edit_title")
    res = db.users.find_one({"note": {"$elemMatch": {"title": search}}})
    db.users.find_one_and_update(
            {"note": {"$elemMatch": {"title": search}}},
            {"$pull": {"note": {"title": search}}}
        )
    return render_template("editNote.html", res = res['note'])

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)