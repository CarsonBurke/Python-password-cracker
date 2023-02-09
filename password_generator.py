import random
from constants import *
from timeit import default_timer as timer

class PasswordGenerator:

    iterations = 0

    def __init__(self, ) -> None:

        self.target_password = self.generate_password()

    def run(self) -> None:

        self.time = timer()
        self.generate_passwords()
        self.time = timer() - self.time

    def generate_passwords(self) -> bool:

        while self.iterations < max_password_amount:

            self.iterations += 1

            password = self.generate_password()

            if password == self.target_password:
                return True
        
        return False
    
    
    def generate_password(self) -> str:

        password = ''
        while len(password) < required_password_len:

            password += random.choice(password_options)
        
        return password