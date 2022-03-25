from flask import Flask

myobj = Flask(__name__)

name = {'name': 'Carlos'}
city_names = ['Paris', 'New york', 'Tokyo', 'Livermore']

@myobj.route("/")
def home():
	return'''
	<html>
		<head>
		<h1> Welcome '''+name['name']+'''!</h1> </head>
		<body> <a href = "www.google.com">not google</a>
		<div>
			<ul>
			<li> '''+city_names[0]+''' </li> <li> '''+city_names[1]+''' </li>
			<li> '''+city_names[2]+''' </li> <li> '''+city_names[3]+''' </li>
			</ul>
		</div>
		</body>
	</html> '''

if __name__ == '__main__':
        myobj.run()
