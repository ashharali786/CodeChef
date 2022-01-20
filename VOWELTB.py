def is_vowel(ch):
    if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
        return True
    else:
        return False
var = input()[0]
print('Vowel') if is_vowel(var.lower()) else print('Consonant')