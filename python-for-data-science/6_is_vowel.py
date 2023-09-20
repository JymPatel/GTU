char1 = 'A'
char2 = 'b'

def alph_type(c):
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        return 'vowel'
    return 'consonant'

print(f"{char1} is {alph_type(char1)}, {char2} is {alph_type(char2)}")