from flask import Flask,render_template,request
from flask_mail import Message,Mail

app=Flask(__name__)

sender = "tcctesteremail@gmail.com"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = sender
app.config['MAIL_PASSWORD'] = "123BigTest654"
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False

mail=Mail(app)


@app.route('/compose')
def index():
    return render_template("compose.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(subject,sender=sender,recipients=[email])

        message.body = msg

        mail.send(message)

        success = "Congrats! You sent an Email!"

        return render_template("result.html", success=success)


if __name__ == "__main__":
    app.run(debug=True)