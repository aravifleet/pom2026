#auth/utils.py

import re

# Password validation function
def validate_password(password):
    """ Validate password length and other requirements (e.g., minimum 6 characters). """
    if len(password) < 6:
        return False
    return True
