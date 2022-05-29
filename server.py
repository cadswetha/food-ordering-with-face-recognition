from flask import Flask, render_template, request, url_for, redirect, Blueprint, send_from_directory
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from login import login_check as lc
from register import register_on_submit as rs
import racedetection as rd
from flask_mysqldb import MySQL
import ast

main = Blueprint('main', __name__)

secret_key = str(os.urandom(24))

app = Flask(__name__)

# database credentials for connecting to the database
app.config['MYSQL_USER'] = 'sql6495906'
app.config['MYSQL_PASSWORD'] = 'ecT2HVKR8x'
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql6495906'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

app.config['TESTING'] = False
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'deployment'
app.config['SECRET_KEY'] = secret_key

app.register_blueprint(main)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    url = StringField('DataURL', validators=[])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    url = StringField('DataURL', validators=[])
    submit = SubmitField('Register')


email = None
url = None


# this is a funtion that is called when a post request is sent to the server when submitting the food choices

def sendPostRequest(email, content):
    cur = mysql.connection.cursor()
    query = f'SELECT * FROM Preferences WHERE mailid = "{email}"'
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) == 0:
        query = "INSERT INTO Preferences (mailid , fooditems) VALUES (%s,%s)"
        val = (email, content)
        cur.execute(query, val)
    else:
        query = f'UPDATE Preferences set fooditems = "{content}" WHERE mailid = "{email}"'
        cur.execute(query)

    mysql.connection.commit()


# this funtion is called when we need to get information from database - i.e saved orders in the database is fetched

def sendGetRequest(email):
    cur = mysql.connection.cursor()
    query = f'SELECT fooditems FROM Preferences WHERE mailid = "{email}"'
    cur.execute(query)
    row = cur.fetchone()
    return row[0]


# index page - login page

@app.route('/', methods=['GET', 'POST'])
def index():
    global email, url
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        url = form.url.data
        return redirect(url_for('.login'))
    elif request.method == 'POST':
        form.email.data = email
        form.url.data = url
    return render_template('index.html', form=form)


# Registeration page

@app.route('/register', methods=['GET', 'POST'])
def register():
    global email, url
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        url = form.url.data
        return redirect(url_for('.register_submit'))

    elif request.method == 'POST':
        form.email.data = email
        form.url.data = url

    return render_template('register.html', form=form)


# after the login is made checking whether data exsits , if yes display the previously saved order
@app.route('/login', methods=['GET', 'POST'])
def login():
    global email, url

    if email == '' or url == '':
        return redirect(url_for('.index'))

    if email == None or url == None:
        return redirect(url_for('.login'))

    status = lc(email, url)
    if status == "Image not clear! Please try again!":
        return render_template('fail.html', msg=status)

    if status == "Data does not exist!":
        return render_template('fail.html', msg=status)

    if status == "Successfully Logged in!":
        app.logger.info("Login Success")
        # get the saved food choices
        content = str(sendGetRequest(email))
        # print(content)
        # convert to list
        content = ast.literal_eval(content)
        return render_template('choices.html', content=content)

    else:
        app.logger.info("Login Fail")
        return render_template('fail.html', msg=status)

# after registration is successful , displays all food choices and also recommends based on the person's race


@app.route('/register_submit', methods=['GET', 'POST'])
def register_submit():
    global email, url

    if request.method == 'POST':
        content = str(request.form.getlist('food'))
        sendPostRequest(email, content)
        return redirect(url_for('.ordered'))

    if email == '' or url == '':
        return redirect(url_for('.register'))

    if email == None or url == None:
        return redirect(url_for('.register_submit'))

    status = rs(email, url)

    if status == "Registration Successful!":
        app.logger.info("Registration Success")
        # detecting race
        raceInfo = rd.detectRace(url)
        # finding out prefered cuisines
        cuisines = rd.recommendCuisine(raceInfo)
        return render_template('selection.html', mailid=email, cuisines=cuisines)

    else:
        app.logger.info("Registration fail")
        return render_template('fail.html', msg=status)


# when order is successful display this page

@app.route('/orders')
def ordered():
    return render_template('success.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
