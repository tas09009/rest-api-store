from db import db

class ItemsTags(db.Model):
    __name__ = "items_tags"
    id = db.Column(db.Integer, primary_key=True)
    tags = db.Column(db.Integer, db.ForeignKey("tags.id"))
    items = db.Column(db.Integer, db.ForeignKey("items.id"))