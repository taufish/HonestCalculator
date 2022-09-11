phrase = input()
vowels = list("aeiou")
consonants = list("abcdfghjklmnpqrstvwxyz")

for n in phrase:
    if n in vowels:
        print("vowel")
    elif n in consonants:
        print("consonant")
    else:
        break
