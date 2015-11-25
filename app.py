from flask import Flask, render_template, request, redirect, session
import os.path, google, urllib2, bs4, re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods=["GET","POST"])
@app.route('/search/', methods=["GET","POST"])
def search():
    q = request.args.get('search')
    text = None
    if q:
        url = google.search(q, num=1, stop=1).next()
        page = google.get_page(url)
        soup = bs4.BeautifulSoup(page, 'lxml')
        for elem in soup(['script', 'style']):
            elem.extract()
        text = soup.get_text(' ', strip=True)
    return render_template("index.html", text=text)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "34 98pqat a98l2 4 63yuge"
    app.run(host='0.0.0.0',
        port=(8080 if os.path.isfile('cloudy') else 8000)
    )
