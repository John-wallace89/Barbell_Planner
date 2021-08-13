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


@app.route("/")
@app.route("/get_workouts")
def get_workouts():
    workouts = mongo.db.workouts.find()
    return render_template("index.html", workouts=workouts)

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check username
        existing_member = mongo.db.users.find_one(
            {'username': request.form.get("username").lower()})

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
            "my_workouts", username=session["user"]))
    
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists
        existing_member = mongo.db.users.find_one(
            {'username': request.form.get("username").lower()})
        
        if existing_member:
            # ensure password matched username
            if check_password_hash(
                    existing_member["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "my_workouts", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# User profile
@app.route("/my_workouts/<username>", methods=["GET", "POST"])
def my_workouts(username):
    # grab member username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("my_workouts.html", username=username)
    
    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
