
class Pillier:
    def __init__(self):
        print("Pillier cryptographi cinstructore is called...")

    def key_gen(self):
        self.p = 13
        self.q = 7
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)



class Server:
    def __init__(self, servername):
        self.servername = servername
        print("Server {} is created successfuly!".format(self.servername))
