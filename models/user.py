from utils.db import db
from bson import ObjectId
import bcrypt
from utils.db import db
from bson import ObjectId

class User:
    def __init__(self, name, email, image, phone, password, _id=None):
        self._id = _id
        self.name = name
        self.email = email
        self.image = image
        self.phone = phone
        self.password = password

    @staticmethod
    def create(data):
        return db.users.insert_one(data)

    @staticmethod
    def get_all():
        return list(db.users.find())

    @staticmethod
    def find_one(query):
        return db.users.find_one(query)

    @staticmethod
    def get_by_email(email):
        return db.users.find_one({"email": email})

    @staticmethod
    def update(user_id, data):
        return db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        return db.users.delete_one({"_id": ObjectId(user_id)})
    
    @staticmethod
    def get_by_email(email):
         try:
                user = db.users.find_one({"email": email})
                if user:
                  # Convert ObjectId to string for JSON compatibility
                    user["_id"] = str(user["_id"])
                return user
                return None
         except Exception as e:
                    print(f"Error fetching user by email: {str(e)}")
                    return None
    @staticmethod
    def update_password(user_id, new_password):
        # Encrypt the new password
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # Update the password in the database
        return db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"password": hashed_password.decode('utf-8')}}
        )




