from flask import Flask, render_template
import sys
app = Flask(__name__)

"""Show index page."""
@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)