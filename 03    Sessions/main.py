from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s. <a href="/logout">Logout</a>' % escape(session['username'])
        
    return 'You are not logged in <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
# set the secret key. keep this really secret: