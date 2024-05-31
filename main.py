#This is a website that lists cafes with wifi and power for remote working.
#I currently live in Busan, South Korea, so this is for my particular city.

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from config import Config


app = Flask(__name__)

app.debug = True

app.config.from_object(Config)

bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired()])  #, URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=[("None", "✘"), ("Wifi", "💪")],
                              validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=[("None", "✘"), ("Power", "🔌")],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html", form=form)

#Decided not to do an add method; unnecessary user functionality
#I left the add.html intact
# @app.route('/add', methods=['POST'])  #ADDED methods=['POST']
# def add_cafe():
#     form = CafeForm()
#     if form.validate_on_submit():
#         with open("cafe-data.csv", mode="a", encoding="utf-8") as csv_file:
#             csv_file.write(f"\n{form.cafe.data},"
#                            f"{form.location.data},"
#                            f"{form.open.data},"
#                            f"{form.close.data},"
#                            f"{form.wifi_rating.data},"
#                            f"{form.power_rating.data}")
#         return redirect(url_for('cafes'))
#     return render_template('add.html', form=form)


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
