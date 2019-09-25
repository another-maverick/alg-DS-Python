
from collections import Counter

def compare_strings(str1, str2):
    ctr = Counter()
    for each_letter in str1:
        ctr[each_letter] += 1
    for each_letter in str2:
        if ctr[each_letter] == 0:
            print("strings permutations are not equal")
            return False
        ctr[each_letter] -= 1
    print("string permutations are equal!!!")
    return True

compare_strings("ideasss","sssidea")