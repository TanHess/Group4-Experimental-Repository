from flask import Flask,render_template,request

from flask_mail import mail,Message

app = Flask(__name__)

mail = Mail(app)

if __name__ == "main":
    app.run(debug=True)