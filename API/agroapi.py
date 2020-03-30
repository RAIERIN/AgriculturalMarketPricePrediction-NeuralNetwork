from flask import Flask, request, jsonify, redirect, url_for,abort, send_file, make_response, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from sqlalchemy import and_
import datetime


today = datetime.date.today()
first = today.replace(day=1)
lastMo = first - datetime.timedelta(days=1)
lastMonth = lastMo.replace(day=1)


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://erin:admin@localhost/agroprediction'
db = SQLAlchemy(app)

class product_detail(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True, nullable=False)
	scientificname = db.Column(db.String(50), unique=True)


	def __init__(self, name,id):
		self.name
		self.id
		self.scientificname

	def __repr__(self):
		return '<product_detail %r>'%self.name

class product_average(db.Model):
	sno = db.Column(db.Integer, primary_key=True)
	id = db.Column(db.Integer, db.ForeignKey(product_detail.id),nullable = False)
	date = db.Column(db.Date, nullable=False)
	avg = db.Column(db.Integer, nullable=False)

	def __init__(self, id, date,avg):
		self.id
		self.date
		self.avg

class product_rate(db.Model):
	sno = db.Column(db.Integer, primary_key=True)
	id = db.Column(db.Integer, db.ForeignKey(product_detail.id),nullable = False)
	date = db.Column(db.Date, nullable=False)
	min = db.Column(db.Integer, nullable=False)
	max = db.Column(db.Integer, nullable=False)
	avg = db.Column(db.Integer, nullable=False)

	def __init__(self, id, date,min,max,avg):
		self.id
		self.date
		self.min
		self.max
		self.avg


class product_predict(db.Model):
	sno = db.Column(db.Integer, primary_key=True)
	id = db.Column(db.Integer, db.ForeignKey(product_detail.id),nullable = False)
	date = db.Column(db.Date, nullable=False)
	prediction = db.Column(db.Integer, nullable=False)

	def __init__(self, id, date,prediction):
		self.id
		self.date
		self.prediction

class product_url(db.Model):
	sno = db.Column(db.Integer, primary_key=True)
	id = db.Column(db.Integer, db.ForeignKey(product_detail.id),nullable = False)
	url = db.Column(db.String(100), unique=True, nullable=False)

	def __init__(self, id, url):
		self.id
		self.url

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, unique=True, nullable=False)
    create_date = db.Column(db.Date, nullable=False)

    def __init__(self,title,author, body, create_date):
        self.title = title
        self.author = author
        self.body = body
        self.create_date = create_date

@app.route('/product_detail', methods=['GET'])
def product():
	products = db.session.query(product_detail.name, product_rate.date,product_rate.max, product_rate.min,product_rate.avg).join(product_rate).filter(product_detail.id == product_rate.id, product_rate.date == today)
	output=[]
	for row in products:
		output.append(row)
	arr=[]
	for product in output:
	    vals = {}
	    vals['name']=product[0]
	    vals['date']=product[1]
	    vals['min']=product[2]
	    vals['max']=product[3]
	    vals['avg']=product[4]
	    arr.append(vals)
	if not output:
		error = "empty data"
		return jsonify({'error':error})
	else:
		response = app.response_class(
			response=json.dumps(arr),
			status=200,
			mimetype='application/json'
		)

		return response

@app.route('/product_detail/<date>', methods=['GET'])
def get_product_date(date):
	products = db.session.query(product_detail.name, product_rate.date,product_rate.max, product_rate.min,product_rate.avg).join(product_rate).filter(product_detail.id == product_rate.id, product_rate.date == date)
	output=[]
	for row in products:
		output.append(row)
	arr=[]
	for product in output:
	    vals = {}
	    vals['name']=product[0]
	    vals['date']=product[1]
	    vals['min']=product[2]
	    vals['max']=product[3]
	    vals['avg']=product[4]
	    arr.append(vals)
	if not output:
		error = "empty data"
		return jsonify({'error':error})
	else:
		response = app.response_class(
			response=json.dumps(arr),
			status=200,
			mimetype='application/json'
		)

		return response

@app.route('/product_avg', methods=['GET'])
def productAvg():
	products = db.session.query(product_detail.name, product_detail.scientificname, product_average.avg, product_average.date, product_predict.prediction,product_predict.date, product_url.url).join(product_average).filter(and_(product_detail.id == product_average.id,product_average.date >= lastMonth, product_average.date < first)).join(product_predict).filter(and_(product_detail.id == product_predict.id, product_predict.date >= first)).join(product_url).filter(product_detail.id == product_url.id)
	output=[]
	for row in products:
		output.append(row)
	arr=[]
	for product in output:
	    vals = {}
	    vals['name']=product[0]
	    vals['scientificname']=product[1]
	    vals['avg']=product[2]
	    vals['date']=product[3]
	    vals['predict']=product[4]
	    vals['pdate']=product[5]
	    vals['url']=product[6]
	    arr.append(vals)
	if not output:
		error = "empty data"
		return jsonify({'error':error})
	else:
		response = app.response_class(
			response=json.dumps(arr),
			status=200,
			mimetype='application/json'
		)

		return response
#news
@app.route('/news', methods=['GET'])
def articles():
	data = News.query.all()
	output=[]
	for row in data:
		output.append(row)
	news = []
	for new in output:
		vals = {}
		vals['id']=new.id
		vals['title']=new.title
		vals['author']=new.author
		vals['body']=new.body
		vals['current_date']=new.create_date
		news.append(vals)
	if not data:
		error = "empty data"
		return jsonify({'error':error})
	else:
		response = app.response_class(
			response=json.dumps(news),
			status=200,
			mimetype='application/json'
		)
		return response


@app.route("/imgs/<imagename>", methods=['GET'])
def images(imagename):
	# print('executing local_photo...')
	# with open('test.jpg', 'rb') as image_file:
	# 	def wsgi_app(environ, start_response):
	# 		start_response('200 OK', [('Content-type', 'image/jpeg')])
	# 		return image_file.read()
	# 	return make_response(wsgi_app)
	path='static/images/'+imagename
	try:
		if path=="static/images/apple.png":
			return send_file(path)
		elif path == "static/images/banana.png":
			return send_file(path)
		elif path == "static/images/carrot.png":
			return send_file(path)
		elif path == "static/images/smalltomato.png":
			return send_file(path)
		elif path == "static/images/bigtomato.png":
			return send_file(path)
	except:
		abort(404)
if __name__ == "__main__":
    app.run(host= '0.0.0.0')
