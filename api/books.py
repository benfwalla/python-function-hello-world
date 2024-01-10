import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example books data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genres": ["Dystopian", "Political Fiction"]},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genres": ["Classic", "Coming-of-Age"]},
]

@app.route('/api/books', methods=['GET'])
def get_books():
    # Retrieve the API key from the request headers
    # client_api_key = request.headers.get('X-API-KEY')

    # # Your stored API key
    # server_api_key = os.environ.get('API_KEY')

    # # Verify the API key
    # if client_api_key != server_api_key:
    #     return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

    # Return the books data
    return jsonify(books)

if __name__ == '__main__':
    app.run()
