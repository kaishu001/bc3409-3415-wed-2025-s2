from flask import Flask
from flask import render_template,request

app = Flask(__name__) # confirm that application belongs to u

@app.route("/") # always run the first line first 
def index(): # creates a template
    return(render_template("index.html"))

if __name__ == "__main__": # reconfirm such that permissions are given
    app.run()
