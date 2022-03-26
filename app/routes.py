from app import myobj
from app import LoginForm
from flask import render_template, request, flash, redirect


name = 'Carlos'
city_names = [{'city':'Paris'}, {'city':'New york'}, {'city': 'Tokyo'}, {'city':'Livermore'}]

@myobj.route("/", methods = ['GET','POST'])
def home():
	form = LoginForm()
	if form.validate_on_submit():
		flash(form.user_input.data)
		return redirect('/')
	return render_template('home.html', username = name, city_names = city_names, form = form)
