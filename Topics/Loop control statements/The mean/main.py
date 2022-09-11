nums = []
while True:
    a = input()
    if a == ".":
        break
    else:
        nums.append(int(a))

print(sum(nums) / len(nums))
