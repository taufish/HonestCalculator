guests = []
while True:
    name = input()
    if name == ".":
        break
    else:
        guests.append(name)
print(guests)
print(len(guests))
