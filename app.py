from flask import Flask,render_template,redirect,url_for,request,jsonify
import os,json
app=Flask(__name__)

users=[{"fullnames":"conrad mugisha","username":"conrad96","password":"12345"}]

entries=[{"username":"conrad96","title":"My Day","body":"Dear Diary Today was so exhausting","date":"7-23-2018"}]

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
	
@app.route("/api/v1/users",methods=["GET"])
def api_users():
	return json.dumps(users)

@app.route("/api/v1/entries",methods=["GET"])
def api_entries():
	return json.dumps(entries)


#logout user
@app.route('/logout')
def logout():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)