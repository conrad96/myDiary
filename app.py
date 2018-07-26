
from flask import Flask,render_template,redirect,url_for,request,jsonify,abort,make_response
from database import Database
import os,json,jwt
import datetime
app=Flask(__name__)
db=Database()
app.config['SECRET_KEY']='mysecret123'
entries=[
{"entry_id":1,"username":"Bill12","title":"My Day 1","body":"Dear Diary Today was so exhausting 1","date":"7-23-2018"},
{"entry_id":3,"username":"Ariho12","title":"My Day 3","body":"Dear Diary Today was so exhausting 3","date":"7-24-2018"},
{"entry_id":4,"username":"mugisha12","title":"My Day 4","body":"Dear Diary Today was so exhausting 4","date":"7-25-2018"},
{"entry_id":2,"username":"Henry12","title":"My Day 2","body":"Dear Diary Today was so exhausting 2","date":"7-26-2018"}]

'''get all users '''
@app.route("/api/v1/users/",methods=["GET"])
def api_users():
	response=db.getUsers()
	return jsonify({"users":response})

'''add new user to database return response on activity'''
@app.route("/api/v1/users/",methods=["POST"])
def api_Adduser():
	fullnames=request.json['fullnames']
	username=request.json['username']
	password=request.json['password']
	check=db.addUser(fullnames,username,password)
	return jsonify({"response":check})
'''login user'''
@app.route("/api/v1/auth/login/",methods=['POST'])
def api_login():
	auth=request.authorization
	username=request.json['username']
	password=request.json['password']
	verify=db.loginUser(username,password)
	if verify:
		token=jwt.encode({"user":username,'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=10)},app.config['SECRET_KEY'])
		return jsonify({"token":token.decode('UTF-8')})
	else:
		return jsonify({"response":"Incorrect password or Username"})	
	# return make_response("Sorry Couldn't Verify",401,{'www-Authenticate':'Basic-Realm="Login Required"'})	
'''get all entries'''
@app.route("/api/v1/entries/",methods=["GET"])
def api_entries():
	return jsonify({"All_Entries":entries})

'''search entry by entry_id'''
@app.route('/api/v1/entries/<int:id>/',methods=["GET"])
def api_searchEntry(id):
	entry= [entry for entry in entries if entry["entry_id"]==id ]
	if entry !=[]:
		return jsonify({"Found_Entry":entry[0]})
	else:
		abort(404, {'message':'Resource Not Found'})

'''Add an Entry'''			
@app.route('/api/v1/entries/',methods=["POST"])
def api_addEntry():
	add_entry=dict(entry_id=request.json['entry_id'],title=request.json['title'],body=request.json['body'],date=request.json['date'])
	entries.append(add_entry)
	return jsonify({"response":"Entry Added"})

'''modify an entry by searching the json object where it exists and new values assigned to the keys'''
@app.route('/api/v1/entries/<int:id>',methods=["PUT"])
def modifyEntry(id):
	record= [entry for entry in entries if entry["entry_id"]==id ]
	if record !=[]:
		values=request.get_json()
		edited=dict(entry_id=values['entry_id'],title=values['title'],date=values['date'],body=values['body'],username=values['username'])
		return jsonify({"Edited":record})	
	else:
		abort(404, {'message':'Resource Not Found'})	

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