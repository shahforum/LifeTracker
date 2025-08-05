from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random123321123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/life_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Goal, Workout, Meal, Todo

@app.route('/')
def home():
    return render_template(home.html)

@app.route('/goals')
def goals():
    goals = Goal.query.all()
    return render_template('goals.html',goals=goals)

if __name__ =='__main__':
    app.run(debug=True)
    