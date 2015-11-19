from flask import Flask
import os.path

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index</h1>"

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "34 98pqat a98l2 4 63yuge"
    app.run(host='0.0.0.0',
        port=(8080 if os.path.isfile('cloudy') else 8000)
    )
