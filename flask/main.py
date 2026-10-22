from flask import Flask
# flask is the package Flask is the class
app = Flask(__name__)
# instance of the flask class
# in python you can make instance of the classes
# everything in the flask one folder is relevant 
# the variable can be called what you want > you can call whatever you want but do recommend calling it app
# the point of this app > to be able to serve something to our client
@app.route("/")
def index():
    return ' Hello CART 351!'

@app.route("/about")
def about():
    return '<h1 style = "color:purple"> About CART 351!</h1>'

@app.route("/user/<name>") 
# within the angle brackats > variables

def user_profile(name):
    return f"<h2> this is <span style = 'color:orange'>{name}'s</span>"


@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    # we will use templates sooN!
    return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"
app.run(debug = True)


# equivalent of hello world
# when do you want your function to be called 
# when does index.html open? > the default wrapped website
# we need to let flask know what the user is going to type
# app is a flask function > parenthesis is argument
# they automatically go together due to @ < decorator function: 
# you can think of it as an in-built function that can take an argument of a string(route) and the index function is also part of that >
# event callback > when this key is pressed run this function

# activation python flask/main.py in terminal

# to have a multiple route
