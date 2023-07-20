from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load the user database from the JSON file
def load_user_database():
    with open('users.json', 'r') as f:
        return json.load(f)

# Check if the provided username and password are valid
def is_valid_credentials(username, password):
    users = load_user_database()
    if username in users and users[username] == password:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if is_valid_credentials(username, password):
            return redirect(url_for('accept'))
        else:
            return redirect(url_for('failure'))
    return render_template('login.html')

# @app.route('/getDetails', methods=['GET', 'POST'])
# def login1():
#         getting the data from db
#         retrunl

@app.route('/success')
def accept():
    return "Login successful!"

@app.route('/failure')
def failure():
    return "Login failed!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
