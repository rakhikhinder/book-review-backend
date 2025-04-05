
# Book Review API

## Technology Stack
This application uses the following technologies:

- **Backend:** Python Flask
- **Database:** MongoDB
- **Password Hashing:** bcrypt
- **API Testing:** Postman (or other API testing tools)
- **Deployment:** Heroku

---

## Data Flow Diagram (DFD)

The Data Flow Diagram (DFD) represents the flow of data in the system, covering entities like `User`, `Book`, and `Review`:

- **User:** Represents the person interacting with the system. They can register, login, and interact with books and reviews.
- **Book:** Books are added by users and can be voted or unvoted. Books have attributes such as title, description, author, etc.
- **Review:** Users can add reviews for books. Reviews are connected to both users and books.

### Levels:
1. **Level 0**: System overview showing interaction with the User, Book, and Review entities.
2. **Level 1**: Detailed interactions and processes such as adding books, reviews, and handling votes.

---

## API Introduction

The API allows interactions with the book review system. Here are the key features:

- **User Routes:**
  - `/users`: Add, get, update, or delete users.
  - `/login`: User login using email and password.
  - `/users/reset_password`: Reset password functionality.
  
- **Book Routes:**
  - `/books`: Add a book, get all books, or delete a book.
  - `/books/<user_id>`: Get books by a specific user.
  - `/books/<book_id>`: Get, update, or delete a specific book.
  - `/books/<book_id>/vote`: Vote for a book.
  - `/books/<book_id>/unvote`: Unvote a book.

- **Review Routes:**
  - `/reviews`: Add, get, update, or delete reviews.
  - `/reviews/<user_id>/<book_id>`: Get reviews by a specific user and book.

---

## How to Test the API

You can test the API using **Postman** or any other API testing tool:

1. **Install Postman:** [Download Postman](https://www.postman.com/downloads/)
2. **Import the Collection:** 
   - Open Postman.
   - Click on the "Import" button and upload the collection file (if provided).
3. **Test Endpoints:** 
   - Make POST, GET, PUT, DELETE requests to the appropriate API endpoints.
   - Example: To add a new user, make a `POST` request to `/users` with a JSON body.

Example of a POST request to `/users`:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "password": "password123"
}
```

4. **View Responses:** Postman will show the response status and message for each request.

---

## Why Use .env File

The `.env` file is used to store environment variables, such as configuration settings, API keys, and database credentials, in a secure and organized way. This keeps sensitive information out of the codebase and ensures better management of different environments (development, staging, production).

 Example .env file:

```
MONGO_URI=mongodb://your-mongodb-uri
SECRET_KEY=your-secret-key
PORT=5000
```

- **Mongo URI:** The URI for connecting to MongoDB.
- **Secret Key:** A secret key used for signing tokens (if implementing authentication).
- **Port:** The port on which the Flask app will run.

**How to Use .env File:**
1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```
2. Add `from dotenv import load_dotenv` at the top of your application and `load_dotenv()` to load the environment variables.

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Deployment Setup on Heroku

To deploy this Flask application to **Heroku**, follow these steps:

1. **Install Heroku CLI:** [Download Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. **Initialize Git Repository:**
   If your project is not already a Git repository, initialize it:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

3. **Create a Heroku App:**
   Log in to Heroku and create a new app:

   ```bash
   heroku login
   heroku create your-app-name
   ```

4. **Add MongoDB Add-on (Optional):**
   If you want to use Heroku's MongoDB service, use the mLab add-on (or another MongoDB provider):

   ```bash
   heroku addons:create mongolab:sandbox
   ```

5. **Create Procfile:**  
   The `Procfile` tells Heroku how to run your app. Create a file called `Procfile` (without any extension) and add the following content:

   ```
   web: python app.py
   ```

6. **Push to Heroku:**

   ```bash
   git push heroku master
   ```

7. **Set Environment Variables on Heroku:**
   You can set environment variables directly on Heroku:

   ```bash
   heroku config:set MONGO_URI=your-mongo-uri
   heroku config:set SECRET_KEY=your-secret-key
   ```

8. **Access Your Application:**  
   After deployment, open the app using:

   ```bash
   heroku open
   ```

---

## Conclusion

This API enables users to interact with books and reviews through a simple and efficient Flask application, backed by MongoDB. The project covers essential topics like user authentication, vote handling, and review management, providing a foundation for further enhancements.
