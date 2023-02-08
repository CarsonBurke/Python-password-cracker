import random
import os
from constants import *
from password_generator import PasswordGenerator

class Manager:

    password_generators = []
    iterations = 0

    def __init__(self) -> None:
        
        i = 0
        while i < password_tests:
            i += 1

            self.password_generators.append(PasswordGenerator())

    def run(self):

        if os.path.exists(passwordsFilePath):
            os.remove(passwordsFilePath)

        self.passwordsFile = open('passwords.txt', 'w')

        for password_generator in self.password_generators:
            password_generator.run()
            self.passwordsFile.write(password_generator.passwords.to)
            self.passwordsFile.write('\n')

        self.passwordsFile.write('Generated passwords to find "{}": \n')

        self.passwordsFile.close()

    def generate_passwords(self) -> bool:

        while self.iterations < self.max_password_amount:

            self.iterations += 1

            password = self.generate_password()
            self.passwordsFile.write('\n')
            self.passwordsFile.write(password)

            if password == self.target_password:
                return True
        
        return False
    
    
    def generate_password(self):

        password = ''
        while len(password) < self.required_password_len:

            password += random.choice(self.password_options)
        
        return password

manager = Manager()