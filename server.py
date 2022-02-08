from flask import Flask, render_template, request, redirect, url_for
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)

@app.route("/new")
def new_user():
    return render_template("create.html")

@app.route("/read/<int:id>")
def show_user(id):
    data = {'id':id}
    return render_template("read.html", user=User.get_user(data))
   

@app.route('/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # first way of doing this. I like the passing request.form better.
    # data = {
    #     "fname": request.form["first_name"],
    #     "lname" : request.form["last_name"],
    #     "email" : request.form["email"]
    # }
    res = User.save(request.form)
    print(f"res is {res}")
    return redirect(url_for('show_user', id = res))#('/read/{res}')

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {'id':id}
    return render_template("edit.html", user=User.get_user(data))
   
@app.route("/update", methods=["POST"])
def update_user():
    User.update(request.form)
    return redirect('/')

@app.route("/remove/<int:id>")
def remove(id):
    data = {'id':id}
    User.remove(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)