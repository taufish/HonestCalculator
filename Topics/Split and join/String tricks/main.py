random_numbers = [1, 22, 333, 4444, 55555]
str_num = str(random_numbers).replace("[", "").replace("]", "").split(", ")
print("\n".join(str_num))
