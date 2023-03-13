import os
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import csv


from db import db
from models import StoreModel
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):

    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}

@blp.route("/store")
class StoreList(MethodView):

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting the item")
        return store

@blp.route("/bookshelf")
class BookShelf(MethodView):

    @blp.response(200)
    def get(self):
        bookshelf = generate_dewey_categories_blueprint()
        return bookshelf

# -------
def generate_dewey_categories_blueprint():
    bookshelf_data = {
        "name": "Bookshelf",
        "children":[],
    }

    categories_json = {}
    file_name = 'externalFiles/dewey_classifications/DDSGORun{file}.csv'
    for i in range(0,3):
        file_path = file_name.format(file=str(i))
        print(os.path.isfile(file_path))
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            data_str_keys = dict(reader)
            data = {int(key): val for key, val in data_str_keys.items()}
            categories_json[str(i)] = data

    # populate ten categories
    for key, val in categories_json['0'].items():
        level_ten = {"name": f"{key}: {val}", "children": []}
        bookshelf_data["children"].append(level_ten)

    book1 = {"name": "Trust", "size": 2074},
    book2 = {"name": "Nothing to See Here", "size": 2074},
    bookshelf_data["children"][0]["children"].append(book1)
    bookshelf_data["children"][0]["children"].append(book2)

    return bookshelf_data
