import os
from flask import (Flask, flash, render_template, 
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# grab database name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# configure connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
#grab secret key
app.secret_key = os.environ.get("SECRET_KEY")

# set up instance of PyMongo. app is flask app from line 9
mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    # generate data from tasks collection on mongodb
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks = tasks)
    # first tasks is what template will use. 
    # second tasks is defined variable above


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host = os.environ.get("IP"),
            port = int(os.environ.get("PORT")), 
            debug = True)