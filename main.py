from mthods import Server, Client
import random

"""cryptographer = Pillier()

m = 123
n = 13*7
r = random.randint(0, n)

c = cryptographer.encrypt(m, r)
p = cryptographer.decrypt(c)

print(c)
print(p)"""


server1 = Server("localhost")
if type(server1).__name__ == 'Server':
    print("hi")

client1 = Client("Telescope1", server1)
client2 = Client("Telescope2", server1)
client3 = Client("Telescope3", server1)