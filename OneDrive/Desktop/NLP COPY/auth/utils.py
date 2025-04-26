# utils.py
from flask import request, jsonify
from auth.session import create_session  # Assuming this handles session token logic

# Password validation function
def validate_password(password):
    """ Validate password length and other requirements (e.g., minimum 6 characters). """
    if len(password) < 6:
        return False
    return True

# Session verification function
def is_authenticated():
    session_token = request.headers.get("Authorization")  # Assume token is sent in the headers
    if not session_token:
        return False
    # You can extend this to verify the token against your session storage (database)
    # In this case, we'll assume the token is valid if it's present.
    return True
