# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()


'''
if __name__ == "__main__" is new but doesn't seem to change anything. Everything looks like v3

if __name__ == "__main__":
    app.debug = True
    app.run()

This code block is run twice
'''
