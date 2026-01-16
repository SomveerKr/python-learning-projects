from turtledemo.clock import dtfont

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 9AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 10:30PM', validators=[DataRequired()])
    coffe_rating = SelectField("Coffee Rating", choices=[("☕"), ("☕☕"), ("☕☕☕"), ("☕☕☕☕"), ("☕☕☕☕☕")])

    wifi_rating = SelectField('WiFi Rating', validators=[DataRequired()], choices=[("✘"), ("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪")])

    power_rating = SelectField('Power Rating', choices=[("🔌"), ("🔌🔌"), ("🔌🔌🔌"), ("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌")])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        opening_time = form.opening_time.data
        closing_time = form.closing_time.data
        coffe_rating = form.coffe_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data
        data_to_save =[cafe, location, opening_time, closing_time, coffe_rating, wifi_rating, power_rating]
        # Read existing data
        rows = []
        try:
            with open('cafe-data.csv', mode='r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)
        except FileNotFoundError:
            print("Error: cafe-data.csv not found")

        # Add new row
        rows.append(data_to_save)

        # Write everything back
        with open('cafe-data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
