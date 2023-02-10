import random
import os
from constants import *
from password_data import PasswordData
from password_generator import PasswordGenerator
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Manager:

    password_generators = []
    password_data = []
    total_iterations = 0
    avg_iterations_over_time = []
    avg_iterations = 0
    successful_cracks = 0
    fastest_iterations = float('inf')
    slowest_iterations = 0

    def __init__(self) -> None:
        
        i = 0
        while i < password_tests:
            i += 1

            self.password_generators.append(PasswordGenerator())

    def __repr__(self) -> str:
        
        msg = ''

        msg += 'Meta results:'
        msg += '\n'
        msg += '   Simulations: {}'.format(password_tests)
        msg += '\n'
        msg += '   Avg iterations: {}'.format(self.avg_iterations)
        msg += '\n'
        msg += '   Password length: {}'.format(required_password_len)
        msg += '\n'
        msg += '   Success ratio: {} / {}'.format(self.successful_cracks, password_tests)
        msg += '\n'
        msg += '   Fastest iterations: {}'.format(self.fastest_iterations)
        msg += '\n'
        msg += '   Slowest iterations: {}'.format(self.slowest_iterations)
        msg += '\n'

        return msg

    def visualize(self):

        plt.plot(np.array(self.avg_iterations_over_time))

        plt.title("Avg iterations by simulation")
        plt.xlabel("Simulations")
        plt.ylabel("Avg iterations")

        plt.show()

    def run(self):

        if os.path.exists(passwordsFilePath):
            os.remove(passwordsFilePath)

        self.passwordsFile = open('passwords.txt', 'w')

        self.total_iterations = 0

        i = 0
        for password_generator in self.password_generators:
            i += 1
            password_generator.run()

            success = password_generator.iterations != max_password_amount

            print('Finished simulation {} / {}, resulted in {}'.format(i, password_tests, "success" if success else "failure"))

            if success: 
                self.successful_cracks += 1

                if password_generator.iterations < self.fastest_iterations:
                    self.fastest_iterations = password_generator.iterations

                if password_generator.iterations > self.slowest_iterations:
                    self.slowest_iterations = password_generator.iterations

            self.total_iterations += password_generator.iterations
            self.avg_iterations_over_time.append(self.total_iterations / i)

            self.password_data.append(
                PasswordData(
                    password_generator.iterations,
                    success,
                    password_generator.target_password,
                    password_generator.time,
                )
            )

        self.avg_iterations = round(self.total_iterations / len(self.password_generators))

        self.passwordsFile.write(repr(self))

        self.passwordsFile.write('\n')
        self.passwordsFile.write('Simulation results: \n')

        self.visualize()

        for data in self.password_data:

            self.passwordsFile.write(repr(data))
            self.passwordsFile.write('\n')

        self.passwordsFile.close()

manager = Manager()