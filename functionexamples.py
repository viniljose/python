def searchForVowels():
    vowels = set('aeiou')
    word = input("please provide a word to search for vowels")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
def search4Vowels(word:str) -> set:
    """Return any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
