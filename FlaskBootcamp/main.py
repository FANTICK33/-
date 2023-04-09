from flask import Flask #importing a module

app = Flask(__name__) #Creating an application

@app.route('/') #Creating the first page
def main():
	return '<h1>Hello, Flask!</h1><br><a href = "/project">перейти на 2-ую страницу</a>'

@app.route('/project')
def project():
	return f'<h3>It\'s my first project on flask</h3><br><a href = "/index/0/0">перейти на 3-ую страницу</a>'

#Passing arguments through the address bar. It can be used as an index to find data from the database.
@app.route('/index/<x>/<y>')
def index(x, y):
	return f"Результат {float(x) + float(y)}"

if __name__ == '__main__':
	app.run(debug=True)
