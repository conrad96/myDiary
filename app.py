from flask import Flask,render_template,redirect,url_for
import os
app=Flask(__name__)

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
	
#logout user
@app.route('/logout')
def logout():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)