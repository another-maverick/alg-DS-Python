
from collections import Counter
import unittest

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

class Test(unittest.TestCase):
    first_set = (("idea","aeid"),("qwerty","ytrewq"))
    second_set = (("diea","asdasdas"),("qwerty","qweqweqwe"))

    def test_compare_strings(self):
        for each_set in self.first_set:
            result = compare_strings(*each_set)
            self.assertTrue(result)
        for each_set in self.second_set:
            result = compare_strings(*each_set)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()