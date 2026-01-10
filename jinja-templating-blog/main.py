from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts_res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = blog_posts_res.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)


@app.route('/blog/<int:post_id>')
def get_blog(post_id):
    matched_post = {}
    for post in blog_posts:
        if post["id"] == post_id:
            matched_post = post
    return render_template("post.html", post=matched_post)


if __name__ == "__main__":
    app.run(debug=True)
