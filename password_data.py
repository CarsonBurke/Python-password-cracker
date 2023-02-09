class PasswordData():
    def __init__(self, iterations, success, password, time) -> None:
        self.iterations = iterations
        self.success = success
        self.password = password
        self.time = time
    def __repr__(self) -> str:
        
        msg = '   '

        if self.success:
            msg += 'Successfully cracked "{}" in '.format(self.password)
        else:
            msg += 'Failed to crack "{}" in '.format(self.password)

        msg += '{} iterations and {} time'.format(self.iterations, self.time)

        return msg