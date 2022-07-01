from app import app
from flask import render_template, redirect
from app.forms import Encode
import base64

@app.route('/', methods=['GET', 'POST'])
def redir():
	return redirect("/encode")

@app.route('/encode', methods=['GET', 'POST'])
def encode():
	username = "loliloveee"
	form = Encode()
	if form.validate_on_submit():
		string = form.b64_input.data
		result = base64.b64encode(string.encode("UTF-8")).decode("UTF-8")	
		return render_template("index.html", form=form, result=result)
	return render_template("index.html", form=form, result="")