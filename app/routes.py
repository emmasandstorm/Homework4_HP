from app import myapp_obj
from app.forms import LoginForm
from flask import render_template, request


@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	name = {'name':'Carlos'}
	city_names = [{'city':'Paris'}, {'city':'New york'}, {'city': 'Tokyo'}, {'city':'Livermore'}]
	form = LoginForm()
	if form.is_submitted():
		result = request.form
		return render_template ('not_google.html', username = name, city_names = city_names, form = form, result = result)
	return render_template('not_google.html', username = name, city_names = city_names, form = form)
