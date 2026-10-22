#jinja -> inject python code into our html template

from flask import Flask,render_template

app = Flask(__name__)
#__ -> special way of declaring python constant

@app.route('/')
def index():
    myName = "leah" #we're going to pretend this is a dynamic variable
    return render_template("pineapple.html", dynamicName = myName)
    #key is a dynamicName and value is myName

@app.route('/pineapple/<name>')
def pineapple(name):
    
    return render_template("pineapple.html", dynamicName = name )
    #key is a dynamicName and value is myName
    #say that I'm doing a portfolio and all my data is in json file 
    #I can load the data in json and fill my template in json data -> have to revisit this part
    #you don't have to hardcode the text in html -> retrieve the data in python
    
#templates folder has to be inside of the flask folder
app.run(debug=True)

#from python, we want to pass the variable to our templates

#css/js/html