from flask import Blueprint, request, jsonify
from models.review import Review

review_routes = Blueprint('review_routes', __name__)

@review_routes.route('/reviews', methods=['POST'])
def add_review():
    data = request.json
    Review.create(data)
    return jsonify({"message": "Review added successfully"}), 201

@review_routes.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.get_all()
    return jsonify(reviews), 200

@review_routes.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    result = Review.update(review_id, data)
    if result.modified_count:
        return jsonify({"message": "Review updated successfully"}), 200
    return jsonify({"message": "Review not found"}), 404

@review_routes.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    result = Review.delete(review_id)
    if result.deleted_count:
        return jsonify({"message": "Review deleted successfully"}), 200
    return jsonify({"message": "Review not found"}), 404
