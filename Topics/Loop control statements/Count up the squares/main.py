integers = []

while len(integers) < 1 or sum(integers) != 0:
    integers.append(int(input()))

sq_integers = []
for n in integers:
    sq_integers.append(n ** 2)

print(sum(sq_integers))
