from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


def create_app():
    application = Flask(__name__)
    Bootstrap(application)
    application.secret_key = "Secret"
    return application


app = create_app()


class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email("Please enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    elif form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html", form=form)
    else:
        return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)