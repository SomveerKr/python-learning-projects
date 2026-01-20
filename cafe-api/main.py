
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
app = Flask(__name__)
TopSecretAPIKey="mkneu4yjedu8734uioefi893489"
# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def convert_to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)


    # json_cafe = jsonify(cafe = {
    #     'id': random_cafe.id,
    #     'name': random_cafe.name,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'seats': random_cafe.seats,
    #     'has_toilet':random_cafe.has_toilet,
    #     'has_wifi':random_cafe.has_wifi,
    #     'has_sockets':random_cafe.has_sockets,
    #     'can_take_calls':random_cafe.can_take_calls,
    #     'coffee_price': random_cafe.coffee_price
    # })
    cafe = random_cafe.convert_to_dict()
    return jsonify(cafe)

@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafes = []
    for cafe in all_cafes:
        cafes.append(cafe.convert_to_dict())
    return jsonify(cafes)

@app.route('/search')
def search_cafe():
    location = request.args.get('loc')
    results = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = results.scalars().all()
    if not all_cafes:
        return jsonify(error= {
                "Not Found": "Sorry, we don't have cafe at that location."
            }), 404
    return jsonify(cafes = [cafe.convert_to_dict() for cafe in all_cafes])



# HTTP POST - Create Record
@app.route('/add-cafe', methods=['POST'])
def add_cafe():
    def convert_to_bool(response):
        if response == 'True' or response == 'true':
            return True
        return False
    new_cafe = Cafe(
        name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'],
        location = request.form['location'],
        seats = request.form['seats'],
        has_toilet= convert_to_bool(request.form['has_toilet']),
        has_wifi= convert_to_bool(request.form['has_wifi']),
        has_sockets= convert_to_bool(request.form['has_sockets']),
        can_take_calls = convert_to_bool(request.form['can_take_calls']),
        coffee_price = request.form['coffee_price']
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "Success": "Cafe added successfully to the database.",
    })

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    user_api_key = request.args.get("api_key")
    if user_api_key == TopSecretAPIKey:
        cafe = db.session.get(entity=Cafe, ident=cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Successfully deleted the cafe.")
        else:
            return jsonify(error={
                "Not Found": "Sorry a cafe with that id was not found in the database.",
            }), 404
    else:
        return jsonify(error="Sorry that's not allowed, make sure that you have correct API key."), 403
if __name__ == '__main__':
    app.run(debug=True)
