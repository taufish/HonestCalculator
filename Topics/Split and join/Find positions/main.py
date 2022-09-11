nums = input().split()
target = input()
en_nums = list(enumerate(nums))
positions = []

for x in en_nums:
    if x[1] == target:
        positions.append(x[0])
    else:
        pass
if len(positions) >= 1:
    print(*positions, sep=" ")
else:
    print("not found")
