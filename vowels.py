vowels = ['a','e','i','o','u']
words = "Target is a company"
vowelsFound = []
for letter in words:
    if letter in vowels:
        if letter not in vowelsFound:
            vowelsFound.append(letter)
for vowel in vowelsFound:
    print(vowel)       
