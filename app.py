from flask import Flask, render_template, request
import requests
app = Flask(__name__)

def shortify(URL):
	res = requests.get(f'https://api.shrtco.de/v2/shorten?url={URL}').json()['result']
	return (res['full_short_link'], res['full_short_link2'], res['full_short_link3'])

@app.get('/')
def index():
	return render_template('index.html')

@app.post('/')
def ipost():
	link = request.form['link']
	return render_template('index.html', links=shortify(link))

if __name__ == '__main__':
	app.run()