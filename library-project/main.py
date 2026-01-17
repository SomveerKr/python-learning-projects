from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, Integer, String

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books_rating.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str]= mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # ------------------getting all record
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()

    return render_template("index.html", books=all_books, books_empty = len(all_books) == 0)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Book(
             title=  request.form.get("book_name"),
             author=  request.form.get("author"),
             rating= int(request.form.get("rating"))
         )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["POST", "GET"])
def edit():
    id = request.args.get("id")
    matched_book = db.get_or_404(Book, id)
    if request.method == "POST":
        new_rating = float(request.form.get("new_rating"))
        print(new_rating)
        matched_book.rating = new_rating
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=matched_book)

if __name__ == "__main__":
    app.run(debug=True)

