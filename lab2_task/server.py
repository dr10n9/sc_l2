#  pip install Flask
# $ FLASK_APP=hello.py flask run
#  * Running on http://localhost:5000/

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
   # return "Welcome to flask demo!"
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)   #to avoid reloading server after some changes everytime


