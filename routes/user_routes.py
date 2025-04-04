from bson import ObjectId
from flask import Blueprint, request, jsonify
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from utils.json_util import serialize_document
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
@user_routes.route('/users', methods=['POST'])
def add_user():
    data = request.json
    email = data.get('email')

    # Check if a user with the given email already exists
    existing_user = User.get_by_email(email)
    if existing_user:
        return jsonify({"message": "User with this email already exists"}), 409

    if 'password' in data:
        # Encrypt the password before saving
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed_password.decode('utf-8')

    User.create(data)
    return jsonify({"message": "User added successfully"}), 201


@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify(serialize_document(users)), 200

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    result = User.update(user_id, data)
    if result.modified_count:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = User.delete(user_id)
    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find the user based on email
    user = User.find_one({"email": email})

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return jsonify({"message": "Login successful", "user_id": str(user["_id"])}), 200

    return jsonify({"message": "Invalid email or password"}), 401

@user_routes.route('/users/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')

    # Find the user based on email
    user = User.get_by_email(email)

    if not user:
        return jsonify({"message": "User not found"}), 404

    # Update the user's password
    result = User.update_password(user["_id"], new_password)

    if result.modified_count:
        return jsonify({"message": "Password reset successfully"}), 200
    return jsonify({"message": "Password reset failed"}), 500


    data = request.json

    # Check if the user exists
    user = User.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Optional: Update password if provided
    if 'password' in data:
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed_password.decode('utf-8')

    # Update user details
    result = User.update(user_id, data)

    if result.modified_count:
        return jsonify({"message": "Profile updated successfully"}), 200
    return jsonify({"message": "No changes made or update failed"}), 304



