from flask import Flask, request, render_template

app = Flask(__name__)
list = []
user1 = user()
user2 = user()


@app.route("/")
def mainPage():
    return render_template("home.html")

@app.route("/login")
def loginPage():
    return render_template("login.html")

@app.route("/registration")
def registrationPage():
    return render_template("registration.html")

@app.route("/user")
def userPage():
    return render_template("user.html")

@app.route("/update")
def userupdatePage():
    return render_template("userupdate.html")


@app.route("/home", methods=["POST", "GET"])
def test():
    if request.method == "GET":
        print("Get")
    else:
        print("Post")
        return f"<p>Your username is {request.form.get("username")}</p><p>Your age is {request.form.get("age")}</p>"
