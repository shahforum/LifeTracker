from app import db
from sqlalchemy import Enum

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(200))

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    date = db.Column(db.String(20))

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    meal = db.Column(Enum('Breakfast','Lunch','Snack','Dinner', name='meal_types'),nullable=False)
    calories = db.Column(db.Integer)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(200))
    is_done = db.Column(db.Boolean, default=False)