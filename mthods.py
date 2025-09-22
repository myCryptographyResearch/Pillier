import math
import random
class Pillier:
    def __init__(self):
        print("Pillier cryptographi cinstructore is called...")


    def key_gen(self):
        self.p = 13
        self.q = 7
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        self.g = random.randint(0, self.n * self.n)
        self.lmbda = math.lcm(self.p - 1, self.q - 1)
        self.mu = pow(self.lx(pow(self.g, self.lmbda, self.n * self.n)), -1, self.n)

    def lx(self, x):
        y = (x - 1) / self.n
        return int(y)


class Server:
    def __init__(self, servername):
        self.servername = servername
        print("Server {} is created successfuly!".format(self.servername))
