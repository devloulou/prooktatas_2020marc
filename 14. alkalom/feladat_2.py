# Palindrome: görög, indul a görög aludni
# paraméterben kapott szóról eldönti, hogy palindrome e

# első karaktert az utolsóval és így tovább

from audioop import reverse
import math

def is_palindrome(word):
    # görög
    # 0 - -1
    # 1 - -2
    # 2 - -3

    # pap
    # 0 - -1
    # 1 - -2

    iter_num = math.ceil(len(word)/2)
    
    cnt = 0
    for idx, item in enumerate(range(iter_num)):
        cnt -= 1
        if word[idx] == word[cnt]:
            pass
        else:
            return False
            
    return True

def is_palindrom_reverse(word):
     return word == word[::-1]


def is_palindrom_sentence(sentence):
    temp1 = sentence.replace(' ', "")
    temp1 = [char for char in sentence if char != ' ']
    
    return temp1 == temp1[::-1]



if __name__ == '__main__':
    #print(is_palindrome('sssz'))
    #print(is_palindrom_reverse('indul a görög aludni'))
    print(is_palindrom_sentence("was it a car or a cat i saw"))