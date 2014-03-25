from flask import Flask, render_template, session, request, redirect, url_for, make_response
import sys
app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    if 'logged_in' in session and session['logged_in']:
        return render_template('private/index.html')
    elif request.cookies.get('login_attempt') == 'yes':
        return redirect(url_for('login'))
    return render_template('public/index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """Show login form."""
    if request.method == 'POST' and request.form['password'] == 'theMasterIsPresent':
        session['logged_in'] = True
        resp = make_response( redirect(url_for('index')) )
        resp.set_cookie('login_attempt', "yes")
        return resp
    return render_template('private/login.html')


app.secret_key = b'k\x9a\xb0\xc1\xbc\x02gR\xd1\x8f\x00\x15\xcb\x169\x002SJ\x8b3\xb0\xd3\xc5'
if __name__ == '__main__':
    app.run(debug=True)