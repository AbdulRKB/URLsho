from flask import Flask, flash, request, render_template, redirect
from short import *
from forms import *

app=Flask(__name__)
app.secret_key ='B\x04\x8b\xb7\x00\xb1\x02.K[\xe2XB\x04\x8b\xb7\x00\xb1\x02.K[\xe2X'
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def main():
	form = subMit()
	if request.method == 'POST':
		link = request.form['url']
		shorted_urls = shortURL(link)
		flash('Shorted URLs Successfully!','success')
		return render_template('index.html', shorted_urls=shorted_urls, form=form)
	return render_template('index.html',form=form)


if __name__ == '__main__':
	app.run()