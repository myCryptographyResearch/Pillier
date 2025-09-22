import math
import random
class Pillier:
    def __init__(self):
        self.key_gen()
        print("Pillier cryptographi cinstructore is called...")

    def public_key_generator(self):
        n = self.p * self.q
        g = random.randint(0, n * n)

        self.public_key = {
            "n": n,
            "g": g
        }

    def get_public_key(self):
        return self.public_key

    def private_key_generator(self):
        public_key = self.public_key
        n = public_key['n']
        g = public_key['g']

        lmbda = math.lcm(self.p - 1, self.q - 1)
        mu = pow(self.lx(pow(g, lmbda, n * n)), -1, n)

        self.private_key = {
            "lmbda": lmbda,
            "mu": mu
        }

    def get_private_key(self):
        return self.private_key

    def key_gen(self):
        self.p = 13
        self.q = 17
        self.phi = (self.p - 1) * (self.q - 1)

        self.public_key_generator()
        self.private_key_generator()

    def lx(self, x):
        public_key = self.public_key
        n = public_key['n']
        y = (x - 1) / n
        return int(y)

    def encrypt(self, m, r):
        assert math.gcd(r, self.n) == 1
        c = (pow(self.g, m, self.n * self.n) * pow(r, self.n, self.n * self.n)) % (self.n * self.n)
        return c

    def decrypt(self, c):
        p = (self.lx(pow(c, self.lmbda, self.n * self.n)) * self.mu) % self.n
        return p


class Server:
    def __init__(self, servername):
        self.servername = servername
        print("Server {} is created successfuly!".format(self.servername))
