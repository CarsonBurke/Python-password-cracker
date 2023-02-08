import random
from constants import *

class PasswordGenerator:

    passwords = []
    iterations = 0

    def __init__(self, ) -> None:

        self.target_password = self.generate_password()

    def run(self):

        self.generate_passwords()

    def generate_passwords(self) -> bool:

        while self.iterations < max_password_amount:

            self.iterations += 1

            password = self.generate_password()
            self.passwords.append(password)

            if password == self.target_password:
                return True
        
        return False
    
    
    def generate_password(self):

        password = ''
        while len(password) < required_password_len:

            password += random.choice(password_options)
        
        return password