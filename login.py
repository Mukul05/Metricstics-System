# login.py
from exceptions import LoginError

class Login:
    ADMIN_USERNAME = 'admin'
    ADMIN_PASSWORD = 'password'

    @staticmethod
    def verify_login(username, password):
        if username != Login.ADMIN_USERNAME or password != Login.ADMIN_PASSWORD:
            raise LoginError("Invalid username or password")
        return True
