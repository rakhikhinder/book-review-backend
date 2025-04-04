from utils.db import db
from bson import ObjectId
from bson import ObjectId

from bson import ObjectId

class Book:
    def __init__(self, user_id, title, description, image, author_name, votecount=0, unvotecount=0, purchase_link=""):
        self.user_id = user_id
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

    @staticmethod
    def get_by_user(user_id):
        return list(db.books.find({"user_id": user_id}))

    @staticmethod
    def vote(book_id):
        return db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$inc": {"votecount": 1}}
        )

    @staticmethod
    def unvote(book_id):
        return db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$inc": {"unvotecount": 1}}
        )

    @staticmethod
    def get_by_id(book_id):
        return db.books.find_one({"_id": ObjectId(book_id)})



