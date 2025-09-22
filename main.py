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

client1 =