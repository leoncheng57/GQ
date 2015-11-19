from flask import Flask, render_template, request, redirect, session
import os.path, google, urllib2, bs4, re

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index</h1>"

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def gSearch():
    if request.method == "GET":
        return render_template("search.html")
    else:
        q = request.form['search']
        results = google.search(q, num=10,start=0,stop=10)
        rlist = []
        for r in results:
            rlist.append(r)
        url = urllib2.urlopen(rlist[0])
        page = url.read()
        soup = bs4.BeautifulSoup(page,'lxml')
        raw = soup.get_text()
    
        text = re.sub("[ \t\n]+"," ", raw)
        #print text
        return render_template("results.html",result=test)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "34 98pqat a98l2 4 63yuge"
    app.run(host='0.0.0.0',
        port=(8080 if os.path.isfile('cloudy') else 8000)
    )
