from flask import Blueprint, request, jsonify
from models.book import Book
from utils.json_util import serialize_document

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.json
    Book.create(data)
    return jsonify({"message": "Book added successfully"}), 201

@book_routes.route('/books', methods=['GET'])
def get_books():
    books = Book.get_all()
    return jsonify(serialize_document(books)), 200

@book_routes.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    result = Book.update(book_id, data)
    if result.modified_count:
        return jsonify({"message": "Book updated successfully"}), 200
    return jsonify({"message": "Book not found"}), 404

@book_routes.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = Book.delete(book_id)
    if result.deleted_count:
        return jsonify({"message": "Book deleted successfully"}), 200
    return jsonify({"message": "Book not found"}), 404
