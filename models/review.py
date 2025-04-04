from utils.db import db
from bson import ObjectId

class Review:
    def __init__(self, user_id, title, message):
        self.user_id = user_id
        self.title = title
        self.message = message

    @staticmethod
    def create(data):
        return db.reviews.insert_one(data)

    @staticmethod
    def get_all():
        return list(db.reviews.find())

    @staticmethod
    def update(review_id, data):
        return db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": data})

    @staticmethod
    def delete(review_id):
        return db.reviews.delete_one({"_id": ObjectId(review_id)})
