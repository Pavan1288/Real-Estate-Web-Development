from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample database to store user information
users = []

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username is already taken
    if any(user['username'] == username for user in users):
        return 'Username already exists! Please choose a different one.'
    
    # Add the user to the database
    users.append({'username': username, 'password': password})
    
    return redirect('/success')

@app.route('/success')
def success():
    return 'Signup successful!'

if __name__ == '__main__':
    app.run(debug=True)
