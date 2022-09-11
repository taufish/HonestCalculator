phrase = input().split()
s_list = []
for i in phrase:
    if i[-1] == "s":
        s_list.append(i)
    else:
        pass
new_list = "_".join(s_list)
print(new_list)
