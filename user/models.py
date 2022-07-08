from flask import Flask, jsonify, request, session, redirect
from datetime import datetime
import uuid
from app import db

class User:
	

	def start_session(self, user):
		session['logged_in'] = True
		session['user'] = user
		return jsonify(user)


	def login(self):
		
		user = db.users.find_one({"username": request.form.get("username")})
		if user and request.form.get('password') == user['password']:
			return self.start_session(user)
		return jsonify({"error": "Invalid credentials"}), 400

	def register(self):
 
		user = {
			"_id": uuid.uuid4().hex,
			"email": request.form.get('email'),
			"username": request.form.get('username'),
			"fullname": request.form.get('fullname'), 
			"password": request.form.get('password')
		}

		#---- check for existing email/username
		if db.users.find_one({"email": user['email']}):
			return	jsonify({"error": "Email address already in use"}), 400
		if db.users.find_one({"username": user['username']}):
			return	jsonify({"error": "Username taken"}), 400


		if db.users.insert_one(user):
			return self.start_session(user)

	def new_note(self):

		note = {
			"title": request.form.get("title"),
			"text": request.form.get("noteText"),
			"keywords": request.form.get("keywords"),
			"date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		}

		db.users.find_one_and_update(
	    	{"_id" : session['user'].get('_id')},
	    	{"$push": {'note': note}}
		)

		return jsonify(note)

	def delete_user(self):
		db.users.delete_one({"_id" : session['user'].get('_id')})
		return redirect('/')

	def delete_note(user):

		note = {
			"title": request.form.get("note_title")
		}

		db.users.find_one_and_update(
			{"note": {"$elemMatch": {"title": note["title"]}}},
			{"$pull": {"note": {"title": note["title"]}}}
		)

	def edit_note(self):


		note = {
			"title": request.form.get("edit_title")
		}
		res = db.users.find_one({"note": {"$elemMatch": {"title": note["title"]}}})

		return jsonify(note), 200

	def find_note(self):

		note = {
			"title": request.form.get("search")
		}
		res = db.users.find_one({"note": {"$elemMatch": {"title": note["title"]}}})
		if(res):
			return jsonify(note), 200
		else:
			return jsonify({"error": "Didn't find a note with this title"}), 400

	def update_note(self):

		note = {
			"title": request.form.get("title"),
			"text": request.form.get("noteText"),
			"keywords": request.form.get("keywords"),
			"date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		}

		db.users.find_one_and_update(
	    	{"_id" : session['user'].get('_id')},
	    	{"$push": {'note': note}}
		)

		return jsonify(note)


	def logout(self):
		session.clear()
		return redirect('/')
