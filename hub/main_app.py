from flask import Flask, render_template, session, request, redirect, url_for
import sys
app = Flask(__name__)

"""Show index page."""
@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('private/index.html')
    return render_template('public/index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['password'] == 'theMasterIsPresent':
        session['logged_in'] = True
        return redirect(url_for('index'))
    return render_template('private/login.html')


app.secret_key = b'k\x9a\xb0\xc1\xbc\x02gR\xd1\x8f\x00\x15\xcb\x169\x002SJ\x8b3\xb0\xd3\xc5'
if __name__ == '__main__':
    app.run(debug=True)