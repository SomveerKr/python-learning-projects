from flask import Flask, render_template
import requests
from datetime import date
app = Flask(__name__)

blog_res = requests.get("https://api.npoint.io/57303010b8ea0f9272e8")
blog_data = blog_res.json()
today = date.today()
date = today.strftime("%B %d, %Y")
author = "Somveer Kumar"
@app.route("/")
def hello_world():
    return render_template("index.html", blogs=blog_data, author=author, date = date, current_year = today.year)

@app.route("/blog/<int:id>")
def get_blog(id):
    matched_post = {}
    for post in blog_data:
        if post["id"] == id:
            matched_post = post
    return render_template("post.html", post= matched_post, author=author, date = date, current_year = today.year)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)