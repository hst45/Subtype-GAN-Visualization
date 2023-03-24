from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
import sys
path = os.path.dirname (__file__)
sys.path.append(path)
print(path)
import config

mail = Mail ()
app = Flask (__name__)
app.config.from_object (config)
mail.init_app (app)


@app.route('/visual_performance', methods=['GET', 'POST'])
def performance_visualize():
	if request.method == 'GET':
		return render_template('performance-visualize.html')


@app.route('/visual_gmm', methods=['GET', 'POST'])
def train_visualize():
	if request.method == 'GET':
		return render_template('gmm.html')


@app.route('/visual_model', methods=['GET', 'POST'])
def model_visualize():
	if request.method == 'GET':
		return render_template('train_visualize.html')


@app.route('/inceptionv3', methods=['GET', 'POST'])
def inceptionv3():
	if request.method == 'GET':
		return render_template('inceptionv3.html')


@app.route('/mobilenet', methods=['GET', 'POST'])
def mobilenet():
	if request.method == 'GET':
		return render_template('mobilenet.html')


@app.route('/resnet50', methods=['GET', 'POST'])
def resnet50():
	if request.method == 'GET':
		return render_template('resnet50.html')


@app.route('/acgan', methods=['GET', 'POST'])
def acgan():
	if request.method == 'GET':
		return render_template('acganGen.html')


@app.route('/subtypegan', methods=['GET', 'POST'])
def subtypegan():
	if request.method == 'GET':
		return render_template('model-visualize.html')


@app.route('/', methods=['GET', 'POST'])
def home_and_concat():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		form = request.form
		sj = form['name'] + ' ' + form['email']
		message = Message(subject = sj, recipients = ['xiaoyang_fang@outlook.com'], body = form['message'])
		try:
			mail.send(message)
			return render_template('index.html', status="I reveived the email and I will connect to you soon!")
		except Exception as e:
			print(e)
			return render_template('index.html', status="Something went wrong and the email cannot be sent :(")


if __name__ == '__main__':
	app.run(debug=True)
