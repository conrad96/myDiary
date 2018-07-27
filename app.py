
from flask import Flask,render_template,redirect,url_for,request,jsonify,abort,make_response
from database import Database
from functools import wraps
import os,json,jwt
import datetime

app=Flask(__name__)
db=Database()
app.config['SECRET_KEY']='conrad12'

''' token verification method (time,secretkey) '''
def token_verify(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		token=request.args.get('token')
		if not token:
			return jsonify({"response":"Token String is Null "}),401
		try:
			data=jwt.decode(token,app.config['SECRET_KEY'])
		except:
			return jsonify({"response":"Token is INVALID OR EXPIRED"}),401

		return f(*args,**kwargs)	
	return decorated_function	

'''method to fetch  all users from database '''
@app.route("/api/v1/users/",methods=["GET"])
def api_users():
	response=db.getUsers()
	return jsonify({"users":response})

'''add new user to database return appopriate response'''
@app.route("/api/v1/auth/signup",methods=["POST"])
def api_Adduser():
	fullnames=request.json['fullnames']
	username=request.json['username']
	password=request.json['password']
	check=db.addUser(fullnames,username,password)
	if not check:
		return jsonify({"response":"Registration Failed"})

'''login user and return Valid Token '''
@app.route("/api/v1/auth/login/",methods=['POST'])
def api_login():
	auth=request.authorization
	username=request.json['username']
	password=request.json['password']
	verify=db.loginUser(username,password)
	if verify:
		token=jwt.encode({"user":username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
		return jsonify({"token":token.decode('UTF-8')})
	else:
		return jsonify({"response":"Incorrect password or Username"})	
	return make_response("Sorry Couldn't Verify",401,{'www-Authenticate':'Basic-Realm="Login Required"'})	

''' Redirect to Authenticated users with Valid Token '''
@app.route('/api/v1/user/')
@token_verify
def users_page():
	return jsonify({"response":"Welcome Authenticated User"})	

'''User adds  an new Entry '''			
@app.route('/api/v1/entries/',methods=["POST"])
def api_addEntry():
	user_id=request.json['user_id']
	title=request.json['title']
	body=request.json['body']
	local = datetime.datetime.now() #insert local machines date
	current_date = local.strftime("%Y-%m-%d")
	entry=db.addEntry(user_id,title,body,current_date)#pass post request values to db method for adding Entry
	if not entry:
		return jsonify({"response":"Entry Not Added"})
	return jsonify({"response":"Entry Added"})	

'''Fecth all entries of a user '''
@app.route('/api/v1/entries/',methods=["GET"])
def api_fetchEntries():
	rows=db.getEntries()
	return jsonify({"Entries":rows})

'''Fetch entries of single user'''
@app.route('/api/v1/entries/<int:id>/',methods=["GET"])
def api_getuserEntry(id):
	user_id=str(id)
	fetch=db.getuserEntries(user_id)
	if not fetch:
		return jsonify({"response":"Empty no Entries Found"})
	return jsonify({"User Entrys":fetch })	

'''modify an entry of '''
@app.route('/api/v1/entries/<int:entry_id>',methods=["PUT"])
def api_modifyEntry(entry_id):
	entry_id=str(entry_id)
	title=request.json['title']
	body=request.json['body']
	get_date=db.getDate(entry_id)
	local = datetime.datetime.now()
	current_date = local.strftime("%Y-%m-%d")
	if get_date != current_date: 	#compare  postDate and Localdate 
		return jsonify({"response":"Sorry You can only Modify Today's Entries "})
	else:	
		fetch=db.modifyEntry(entry_id,title,body,current_date)
		if not fetch:
			return jsonify({"response":"Entry Not Modified"})
	return jsonify({"response": "Entry Modified successfully" })

'''custom ErrorHandler for resource not found 404'''
@app.errorhandler(404)
def custom404(error):
    response = jsonify({'message': error.description,'status':404})
    return response

#logout user
@app.route('/logout')
def logout():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)