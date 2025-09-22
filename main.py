from mthods import Server, Pillier
import random

cryptographer = Pillier()

m = 123
n = 13*7
r = random.randint(0, n)

c = cryptographer.encrypt(m, r)
p = cryptographer.decrypt(c)

print(c)
print(p)


server1 = Server("localhost")