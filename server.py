from operator import truediv
from pyexpat.errors import messages

from flask import Flask, request, render_template, redirect, url_for, make_response
from datetime import datetime
from database import mongo_client
from authentication.login_auth import login_user
from authentication.register_auth import register_user
from authentication.token_auth import validate_token

# This is the users database
auth_db = mongo_client["auth-db"]
user_credentials = auth_db["users"]

# This database stores user feedback
feedback_db = mongo_client["feedback-db"]
feedback_collection = feedback_db["feedback"]

app = Flask(__name__, template_folder="public")

@app.get("/feedback")
def feedback():
    token = request.cookies.get("auth_token")

    if not validate_token(token):
        return redirect(url_for("login_page"))

    return render_template("feedback.html")

@app.post("/submit")
def submit():
    text = request.form.get("text", "").strip()

    token = request.cookies.get("auth_token")
    if not validate_token(token):
        return redirect(url_for("login_page"))

    if text :
        feedback_collection.insert_one({"text": text, "ts": datetime.utcnow()})
    return redirect(url_for("submissions"), code=303)

@app.get("/submissions")
def submissions():
    token = request.cookies.get("auth_token")

    if not validate_token(token):
        return redirect(url_for("login_page"))

    items = list(feedback_collection.find({}, {"_id": 0}).sort("ts", -1).limit(10))
    return render_template("submissions.html", items=items)


@app.get("/register")
def register_page():
    return render_template("register.html")

@app.post("/register")
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm password")

    status_code, response_message = register_user(username, email, password, confirm_password)

    if status_code == 200:
        return redirect(url_for("login"))

    return render_template("register.html", error=response_message), status_code

@app.get("/")
@app.get("/login")
def login_page():
    return render_template("login.html")

@app.post("/login")
def login():
    username = request.form.get("username").lower()
    password = request.form.get("password")

    status_code, response_message, cookie = login_user(username, password)

    if status_code != 200:
        return render_template("login.html", error=response_message), status_code

    cookie_vals = cookie.get("auth_token").split('; ')
    max_age = 315360000
    http_only = False


    if "HttpOnly" in cookie_vals:
        http_only = True
    max_ages = [directive for directive in cookie_vals if directive.startswith("Max-Age=")]
    if len(max_ages) == 1:
        max_age = int(max_ages[0].split("=")[1])

    if status_code == 200:
        res = make_response(redirect(url_for("feedback"), code=303))
        res.set_cookie("auth_token", cookie_vals[0], httponly=http_only, max_age=max_age)

        return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
