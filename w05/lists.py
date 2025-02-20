clients = []

clients.append("John")
clients.append("Mary")

new_client = input("Enter a new client: ")
clients.append(new_client)

while new_client != "quit":
    new_client = input("Enter a new client: ")
    clients.append(new_client)

print(clients)

for client in clients:
    print(client)
    
# index

colors = ["red", "green", "blue"]
print(colors[0])
print(colors[1])

for color in colors:
    print(color)
    
for i in range(len(colors)):
    color = colors[i]
    print(color)