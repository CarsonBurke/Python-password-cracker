import string

# How many password cracking simulations to run
password_tests = 100
# The length of the password to guess for
required_password_len = 2
# The max iterations a password crack attempt can take
max_password_amount = 100000000000
# Possible characters in a password
password_options = string.ascii_letters + string.digits
# Where to write the results to
passwordsFilePath = 'passwords.txt'