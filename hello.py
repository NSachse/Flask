from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)


@app.route("/")
def hello():
    return "<html><body><h1>Welcome</h1></body></html>"

@app.route("/about")
def about():
	return "About Page"

@app.route('/login')
@app.route('/login/<name>')
def login(name=None):
    return render_template('show_login.html', name=name)

if __name__ == "__main__":
	app.debug = True
	app.run()
