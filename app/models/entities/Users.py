from werkzeug.security import generate_password_hash, check_password_hash

class Users():

    def __init__(self, user_id, user_name, password, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.user_type_id = user_type

    def encrypt_password(password):
        encrypted = generate_password_hash(password)
        
        password_match = check_password_hash(encrypted, password)
        
        return password_match