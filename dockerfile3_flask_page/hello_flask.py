from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    return f'<p>Hello, World.  The current datetime is {current_time}</p><p>Another paragraph</p>'
