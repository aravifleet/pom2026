import uuid
import hashlib
import time

# Session creation logic
def create_session(user_id):
    # Generate a unique session token using uuid
    session_token = str(uuid.uuid4())
    return {"session_token": session_token}
