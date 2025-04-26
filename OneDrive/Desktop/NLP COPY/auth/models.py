from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
from flask import request, current_app as app
from auth.session import create_session

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
        return {"message": "User not found!"}

    # Check if the account is locked
    if user.get('lockout_time') and datetime.now() < user['lockout_time']:
        return {"message": f"Your account is locked. Try again after {user['lockout_time']}."}

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
            return {"message": f"Incorrect password entered 3 times. Your account is locked for 5 minutes."}

        return {"message": "Invalid password!"}

    # If login is successful, reset failed attempts
    app.mongo.db.users.update_one(
        {"emp_id": session["emp_id"]},
        {"$set": {"failed_attempts": 0, "lockout_time": None}}
    )

    # Create a session token
    user_id = session["emp_id"]  # Using emp_id as user_id for session
    session_token = create_session(user_id)["session_token"]
    
    # Return the session token with the success message
    return {"session_token": session_token, "role": user["role"]}
