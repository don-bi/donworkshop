"""
Dual Ducks: Donald Bi, Brian/Paul Yang, Faiyaz Rafee
SoftDev
K11 -- Flask/html forms
2022-10-14
time spent: .5 hrs
"""
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/" , methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #prints name of the Flask module
    print("***DIAG: request obj ***")
    print(request) #Shows the page link
    print("***DIAG: request.args ***")
    print(request.args) #prints dictionary with the user's input on the webpage
    #print("***DIAG: request.args['username']  ***") #nothing showing up in the terminal
    #print(request.args['username']) #Uncommenting it results in a failure becuase a username isn't given
    print("***DIAG: request.headers ***")
    print(request.headers) #Browser and OS of the user
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) #works in authenticate() because username is given
    print("***DIAG: request.headers ***")
    print(request.headers)
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
