"""if __name__ == '__main__'"""
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
ops = ["+", "-", "*", "/"]


def num_check(a):
    try:
        float(a)
        return True
    except ValueError:
        print(msg_1)
        return False


def ops_check(a):
    if a in ops:
        return True
    else:
        print(msg_2)
        return False


def zero_check(a, b):
    if a == "/" and b == "0":
        print(msg_3)
        return False
    else:
        return True


def is_one_digit(v):
    if 10 > v > -10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        print(msg_9 + msg)


c = "y"
memory = 0
while c == "y":
    print(msg_0)
    calc = input().split()

    if calc[0] == "M":
        calc[0] = memory
    if calc[2] == "M":
        calc[2] = memory

    try:
        num_1 = float(calc[0])
        num_2 = float(calc[2])
        check(num_1, num_2, calc[1])
    except ValueError:
        pass

    if num_check(calc[0]) and num_check(calc[2]) and ops_check(calc[1]) and zero_check(calc[1], calc[2]) is True:
        if calc[1] == ops[3] and calc[2] == 0:
            print(msg_3)
        else:
            if calc[1] == ops[0]:
                result = num_1 + num_2
                print(result)
            elif calc[1] == ops[1]:
                result = num_1 - num_2
                print(result)
            elif calc[1] == ops[2]:
                result = num_1 * num_2
                print(result)
            elif calc[1] == ops[3]:
                result = num_1 / num_2
                print(result)
            recall = input(msg_4)
            if recall == "y":
                if is_one_digit(result) is True:
                    a = input(msg_10)
                    if a == "y":
                        b = input(msg_11)
                        if b == "y":
                            c = input(msg_12)
                            if c == "y":
                                memory = result
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    memory = result
            c = input(msg_5)
