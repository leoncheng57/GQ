from flask import Flask, render_template, request, redirect, session, url_for
import os.path, google, urllib2, bs4, re
import questions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods=["GET","POST"])
@app.route('/search/', methods=["GET","POST"])
def search():
    q = request.args.get('search').strip()
    text = None
    message = None
    error = False
    if q:
        url = google.search(q, num = 5, start = 0, stop = 5).next()
        page = google.get_page(url)
        soup = bs4.BeautifulSoup(page)
        for elem in soup(['script', 'style']):
            elem.extract()
        text = soup.get_text(' ', strip=True)
        if re.match('[Ww][Hh][Oo]', q):
            message = "Identified this as a WHO question!"
            if re.search('([Ii][Ss]|[Ww][Aa][Ss])\s[A-Z][a-z]+\s[A-Z][a-z]+', q):
                message += "<br>Determined that you're looking for information about " + re.search('[A-Z][a-z]+\s[A-Z][a-z]+', q).group(0) + "..."
            else:
                message += "<br>Giving you information about the person who \"" + re.match('.*(?=\?)', re.search('(?<=[Ww][Hh][Oo][\s]).*', q).group(0)).group(0) + "\""
                text = questions.get_names(text)
        else:
            message = "<span style=\"color:red;\">Sorry, we don't recognize this question.<br>\
Are you sure that you put a WHO at the beginning?</span>"
    return render_template("index.html", text=text, message=message)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "34 98pqat a98l2 4 63yuge"
    app.run(host='0.0.0.0',
        port=(8080 if os.path.isfile('cloudy') else 8000)
    )
