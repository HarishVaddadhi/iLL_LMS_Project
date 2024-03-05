from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder='./src/frontend/pages')
app.secret_key = 'your_secret_key'

# Sample user data (replace with your actual database)
users = {
    'student1@college.edu': 'password1',
    'student2@college.edu': 'password2'
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are valid
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/')
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)