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
        public_key = self.public_key
        n = public_key['n']
        g = public_key['g']
        assert math.gcd(r, n) == 1
        c = (pow(g, m, n * n) * pow(r, n, n * n)) % (n * n)
        return c

    def decrypt(self, c):
        public_key = self.public_key
        n = public_key['n']
        private_key = self.private_key
        lmbda = private_key['lmbda']
        mu = private_key['mu']
        p = (self.lx(pow(c, lmbda, n * n)) * mu) % n
        return p


class Server:
    def __init__(self, servername):
        self.servername = servername
        self.cryptographer = Pillier()
        self.public_key = self.cryptographer.get_public_key()
        self.private_key = self.cryptographer.get_private_key()
        print("Server {} is created successfuly!".format(self.servername))


class Client:
    def __init__(self, clientname, server):
        self.clientname = clientname
        self.server = server
        self.cryptographer = self.server.cryptographer
        self.public_key = self.cryptographer.get_public_key()
        print("Client {} is created on {} successfuly!".format(self.clientname, self.server.servername))