from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])

    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ])

    submit = SubmitField(label='Log In')

app = Flask(__name__)
#always put it in .env
app.secret_key = 'a-very-secret-string'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Here you would typically check the database and log the user in.
        if email=="admin@email.com" and password=="admin@123":
            return render_template("success.html")
        return render_template("denied.html")
    # If GET request OR validation failed:
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
