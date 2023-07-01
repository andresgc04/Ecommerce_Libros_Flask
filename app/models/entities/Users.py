from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(UserMixin):

    def __init__(self, user_id, user_name, password, user_type):
        self.id = user_id
        self.user_name = user_name
        self.password = password
        self.user_type_id = user_type

    @classmethod
    def verify_password(self, password_encrypted, password):

        return check_password_hash(password_encrypted, password)