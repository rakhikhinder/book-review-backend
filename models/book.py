from utils.db import db
from bson import ObjectId

class Book:
    def __init__(self, title, description, image, author_name, votecount=0, unvotecount=0, purchase_link=""):
        self.title = title
        self.description = description
        self.image = image
        self.author_name = author_name
        self.votecount = votecount
        self.unvotecount = unvotecount
        self.purchase_link = purchase_link

    @staticmethod
    def create(data):
        return db.books.insert_one(data)

    @staticmethod
    def get_all():
        return list(db.books.find())

    @staticmethod
    def update(book_id, data):
        return db.books.update_one({"_id": ObjectId(book_id)}, {"$set": data})

    @staticmethod
    def delete(book_id):
        return db.books.delete_one({"_id": ObjectId(book_id)})
