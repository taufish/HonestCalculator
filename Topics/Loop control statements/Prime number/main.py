num = int(input())
non_prime = 0

if num >= 2:
    for n in range(2, (round(num ** 0.5) + 1)):
        if num % n == 0:
            non_prime += 1
        else:
            pass

    if non_prime > 0:
        print("This number is not prime")
    else:
        print("This number is prime")
else:
    print("This number is not prime")
