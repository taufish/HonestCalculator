triangle = int(input())
lines = []
pound_count = 1
for i in range(triangle):
    lines.append("#" * pound_count)
    pound_count += 2
for line in lines:
    print(line.center(len(lines[-1])))
