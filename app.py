import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Home
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists
        existing_member = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_member:
            # ensure password matched username
            if check_password_hash(
               existing_member["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "home", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/get_workouts")
def get_workouts():
    workouts = list(mongo.db.workouts.find())
    return render_template("barbell_workouts.html", workouts=workouts)


# Search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    workouts = list(mongo.db.workouts.find({"$text": {"$search": query}}))
    return render_template("barbell_workouts.html", workouts=workouts)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check username
        existing_member = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_member:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # put new user in 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome to the Pack!")
        return redirect(url_for(
            "home", username=session["user"]))

    return render_template("register.html")


# Logout
@app.route("/logout")
def logout():
    # remove user from session
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Log workout
@app.route("/log_workout", methods=["GET", "POST"])
def log_workout():
    if request.method == "POST":
        workout = {
            "is_cardio": request.form.get("is_cardio"),
            "exercise_type": request.form.get("exercise_type"),
            "workout_name": request.form.get("workout_name"),
            "date": request.form.get("date"),
            "exercise_name": request.form.get("exercise_name"),
            "sets1": request.form.get("sets1"),
            "reps1": request.form.get("reps1"),
            "weight": request.form.get("weight"),
            "duration": request.form.get("duration"),
            "created_by": session["user"]
        }
        mongo.db.workouts.insert_one(workout)
        flash("Nice work, Workout Successfully Logged")
        return redirect(url_for("get_workouts"))

    exercises = mongo.db.exercises.find().sort("exercise_type", 1)
    return render_template("log_workout.html", exercises=exercises)


# Edit button
@app.route("/edit_workout/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    if request.method == "POST":
        submit = {
            "is_cardio": request.form.get("is_cardio"),
            "exercise_type": request.form.get("exercise_type"),
            "workout_name": request.form.get("workout_name"),
            "date": request.form.get("date"),
            "exercise_name": request.form.get("exercise_name"),
            "sets1": request.form.get("sets1"),
            "reps1": request.form.get("reps1"),
            "weight": request.form.get("weight"),
            "duration": request.form.get("duration"),
            "created_by": session["user"]
        }
        mongo.db.workouts.update({"_id": ObjectId(workout_id)}, submit)
        flash("Workout Updated")
        return redirect(url_for("get_workouts"))

    workout = mongo.db.workouts.find_one({"_id": ObjectId(workout_id)})
    exercises = mongo.db.exercises.find().sort("exercise_type", 1)
    return render_template(
        "edit_workout.html", workout=workout, exercises=exercises)


# Delete workout
@app.route("/delete_workout/<workout_id>")
def delete_workout(workout_id):
    mongo.db.workouts.remove({"_id": ObjectId(workout_id)})
    flash("Workout Deleted")
    return redirect(url_for("get_workouts"))


# 404 error redirect
@app.errorhandler(404)
def page_not_found_404(e):
    return render_template("404.html"), 404


# 500 error redirect
@app.errorhandler(500)
def page_not_found_500(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
