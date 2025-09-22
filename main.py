from mthods import Server, Client



server1 = Server("localhost")
if type(server1).__name__ == 'Server':
    print("hi")

client1 = Client("Telescope1", server1)
client2 = Client("Telescope2", server1)
client3 = Client("Telescope3", server1)

m = 123
c = client1.encryptor(m)
p = server1.decryptor(c)

print(m)
print(c)
print(p)