cafe_list = {}

while True:
    cafe = input()
    if cafe == "MEOW":
        break
    else:
        cafe = cafe.split()
        cafe_list[int(cafe[1])] = cafe[0]

print(cafe_list[max(cafe_list)])
