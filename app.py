from flask import Flask
from routes.book_routes import book_routes
from routes.user_routes import user_routes
from routes.review_routes import review_routes
from config import Config
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
app.register_blueprint(book_routes, url_prefix='/api')
app.register_blueprint(user_routes, url_prefix='/api')
app.register_blueprint(review_routes, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Bookstore API"

if __name__ == "__main__":
    app.run(port=Config.PORT)
