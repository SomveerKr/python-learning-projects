from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from tmdb import TMDBClient
movie_client = TMDBClient()


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class= Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)

class Movie(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year:Mapped[int] = mapped_column(Integer, nullable=False)
    description:Mapped[str] = mapped_column(String(500), nullable=False)
    rating:Mapped[float] = mapped_column(Float, nullable=True)
    ranking:Mapped[int] = mapped_column(Integer, nullable=True)
    review:Mapped[str] = mapped_column(String(250), nullable=True)
    img_url:Mapped[str] = mapped_column(String(250), nullable=False)

# CREATE TABLE
with app.app_context():
    db.create_all()


#------ Rate and Review edit page form
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

#------- movie title form
class MovieTitleForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
@app.route("/")
def home():
    result  = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    total_movies = len(all_movies)
    for movie in all_movies:
        movie.ranking = total_movies
        total_movies -=1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    movie_title_form = MovieTitleForm()
    if movie_title_form.validate_on_submit():
        title = movie_title_form.title.data
        #getting data from movie database api client
        movies_res = movie_client.search_movie(title)
        movies_list = movies_res["results"]
        return render_template("select.html", movies=movies_list)
    return render_template("add.html", form=movie_title_form)


@app.route("/get-movie-detail")
def get_movie_detail():
    #getting from database api
    movie_id = request.args.get("id")
    movie_detail = movie_client.get_movie_detail(movie_id)
    #making new movie object for saving to our db
    title = movie_detail["title"]
    img_url = f"https://image.tmdb.org/t/p/original{movie_detail['poster_path']}"
    year = movie_detail["release_date"]
    description = movie_detail["overview"]

    #new movie
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)
    db.session.add(new_movie)
    db.session.commit()
    #after saving item to db, gets its id
    new_movie_id = new_movie.id
    return redirect(url_for("edit", id=new_movie_id))


#--------TO EDIT RATING AND REVIEW
@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    form = RateMovieForm()
    if form.validate_on_submit():
        rating = float(form.rating.data)
        review = form.review.data

        movie_to_update = db.get_or_404(Movie, id)
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
