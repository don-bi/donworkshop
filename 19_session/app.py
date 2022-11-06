'''
Rice Explosion: Nakib Abedin, Donald Bi, Wilson Mach
SoftDev
K19 -- working w/ sessions
2022-11-04
time spent: .7
'''
from flask import Flask,render_template,request,session

app = Flask(__name__)



app.secret_key = b'\x95m-o\xdb\xbct\xe8\x04+\x1c\xab\x9e\xa5\x1f}\xba\xd8l\x03\x9e(\xf0\xd5\x8dp\xf2\xef\x0e\xb8\xd8x'
correct_username = "troll"
correct_password = "troll123"

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        print(session['username'])
        return render_template('response.html', username = session['username'])
    return render_template('login.html') #for rendering login page intially
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #for login form submission
        username = request.form['username']   
        password = request.form['password']

        if username == correct_username: #checks for correct username
            if password == correct_password: #checks for correct password
                session['username'] = username #makes cookie for username
                #print(session['username']) #testing
                return render_template('response.html', username = username, password = password)
            return render_template('login.html', error = 'wrong password')
        return render_template('login.html', error = 'wrong username')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()