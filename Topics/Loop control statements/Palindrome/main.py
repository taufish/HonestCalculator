word = input()
forward_list = list(word)
backward_list = list(reversed(forward_list))

if forward_list == backward_list:
    print("Palindrome")
else:
    print("Not palindrome")
