nums = []
a = ""
while a != ".":
    a = input()
    nums.append(a)

nums.remove(".")
fl_nums = [float(x) for x in nums]
new_nums = sorted(fl_nums)
print(new_nums[0])
