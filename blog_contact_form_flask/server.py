from flask import Flask, render_template, request
import requests
from datetime import date
import os
from dotenv import load_dotenv
from send_email import EmailSender
# 1. Load Configuration
load_dotenv()


blog_res = requests.get("https://api.npoint.io/57303010b8ea0f9272e8")
blog_data = blog_res.json()
today = date.today()
author = "Somveer Kumar"


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", blogs=blog_data, author=author, date = today.strftime("%B %d, %Y"), current_year = today.year)

@app.route("/blog/<int:id>")
def get_blog(id):
    matched_post = {}
    for post in blog_data:
        if post["id"] == id:
            matched_post = post
    return render_template("post.html", post= matched_post, author=author, date = today.strftime("%B %d, %Y"), current_year = today.year)

@app.route("/about")
def about():
    return render_template("about.html")
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        full_name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        recipient = "work.somveerk@gmail.com"
        subject_line = full_name
        body_text = f"{email}\n{phone}\n{message}"

        my_email = os.getenv("EMAIL_ID")
        my_password = os.getenv("EMAIL_PASS")

        emailer = EmailSender(sender_email=my_email, password=my_password)
        success = emailer.send(receiver_email=recipient, subject=subject_line, content=body_text)

        if success:
            print("Process finished successfully.")
        else:
            print("Process failed.")
        return render_template("contact.html", hero_txt="Form Submitted successfully!")

    return render_template("contact.html", hero_txt= "Contact Me")





if __name__ == "__main__":
    app.run(debug=True)