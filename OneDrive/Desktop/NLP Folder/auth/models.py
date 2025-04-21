from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from flask import request, current_app as app

# Register a user
def register_user(session, mongo):
    # Get the data from the request (JSON body)
    session = request.get_json()

    # Hash the password before storing it
    hashed_password = generate_password_hash(session["password"])
    
    user = {
        "emp_id": session["emp_id"],
        "password": hashed_password,
        "role": session["role"],
        "failed_attempts": 0,
        "lockout_time": None
    }

    # Insert the user into the MongoDB database
    app.mongo.db.users.insert_one(user)
    
    return f"User {session['emp_id']} registered successfully!"

# Login a user
def login_user(session, mongo):
    # Get the data from the request (JSON body)
    session = request.get_json()

    # Find user by emp_id
    user = app.mongo.db.users.find_one({"emp_id": session["emp_id"]})

    if not user:
        return "User not found!"

    # Check if the account is locked
    if user.get('lockout_time') and datetime.now() < user['lockout_time']:
        return f"Your account is locked. Try again after {user['lockout_time']}."

    # Check if the password matches
    if not check_password_hash(user["password"], session["password"]):
        # Increment failed attempts
        app.mongo.db.users.update_one(
            {"emp_id": session["emp_id"]},
            {"$inc": {"failed_attempts": 1}}
        )

        # Lock account if 3 failed attempts
        if user["failed_attempts"] + 1 >= 3:
            lockout_time = datetime.now() + timedelta(minutes=5)
            app.mongo.db.users.update_one(
                {"emp_id": session["emp_id"]},
                {"$set": {"lockout_time": lockout_time}}
            )
            return f"Incorrect password entered 3 times. Your account is locked for 5 minutes."

        return "Invalid password!"

    # If login is successful, reset failed attempts
    app.mongo.db.users.update_one(
        {"emp_id": session["emp_id"]},
        {"$set": {"failed_attempts": 0, "lockout_time": None}}
    )

    # If login is successful
    return f"Welcome, {user['emp_id']}! You are logged in as {user['role']}."
