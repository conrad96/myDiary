from flask import Flask,render_template,redirect,url_for,request,jsonify
import os,json
app=Flask(__name__)

users=[
{"user_id":1,"fullnames":"Bill","username":"Bill12","password":"12345"},
{"user_id":2,"fullnames":"Henry","username":"Henry12","password":"12345"},
{"user_id":3,"fullnames":"Ariho","username":"Ariho12","password":"12345"},
{"user_id":4,"fullnames":"mugisha","username":"mugisha12","password":"12345"}
	]

entries=[
{"user_id":1,"title":"My Day 1","body":"Dear Diary Today was so exhausting 1","date":"7-23-2018"},
{"user_id":3,"title":"My Day 3","body":"Dear Diary Today was so exhausting 3","date":"7-24-2018"},
{"user_id":4,"title":"My Day 4","body":"Dear Diary Today was so exhausting 4","date":"7-25-2018"},
{"user_id":2,"title":"My Day 2","body":"Dear Diary Today was so exhausting 2","date":"7-26-2018"}

]

@app.route('/')
def index():
	return render_template('index.html')

#about Page
@app.route('/about')
def register():
	return render_template('about.html')

#register Page
@app.route('/register')
def login():
	return render_template('register.html')	

#user Page
@app.route('/user')
def user():
	return render_template('user.html')	

#reminders Page
@app.route('/reminders')
def reminders():
	return render_template('reminders.html')
#view all users	
@app.route("/api/v1/users",methods=["GET"])
def api_users():
	return json.dumps(users)
#view all entries
@app.route("/api/v1/entries",methods=["GET"])
def api_entries():
	return json.dumps(entries)

@app.route('/api/v1/searchEntry/<int:id>/',methods=["GET"])
def api_searchEntry(id):
	entry= [entry for entry in entries if entry["user_id"]==id ]
	return json.dumps(entry)

#logout user
@app.route('/logout')
def logout():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)