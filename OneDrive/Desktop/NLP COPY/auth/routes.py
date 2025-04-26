from flask import Blueprint, request, jsonify
from auth.models import login_user, register_user
from auth.session import create_session
from database import init_app

# Create the auth blueprint
auth_bp = Blueprint('auth', __name__)

# Initialize MongoDB (pass Flask app from main if needed)
mongo = init_app(None)

# Route: /auth/login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    session = {
        "emp_id": data.get("emp_id"),
        "password": data.get("password")
    }

    result = login_user(session, mongo)
    if "session_token" in result:
        return jsonify({
            "message": f"Welcome, {session['emp_id']}! You are logged in as {result['role']}.",
            "session_token": result["session_token"]
        }), 200
    else:
        return jsonify({"message": result["message"]}), 401  # Unauthorized if login fails

# Route: /auth/register
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    session = {
        "emp_id": data.get("emp_id"),
        "password": data.get("password"),
        "role": data.get("role", "user")  # Default role = user
    }

    result = register_user(session, mongo)
    return jsonify({"message": result}), 201
