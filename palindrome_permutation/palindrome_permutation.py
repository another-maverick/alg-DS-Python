
from collections import Counter
import unittest

def permutataion_panlindrome(input_string):
    str_without_spaces = input_string.replace(" " , "")
    non_doubles = 0
    print(str_without_spaces)

    c = Counter(str_without_spaces)
    for each_letter  in c:
        if c[each_letter] % 2 != 0:
            non_doubles += 1
    if non_doubles > 1:
        print( "No!!! The permutations don't result in a Palindrome" )
        return False
    print("Yes!!! The permutations result in a Palindrome")
    return True

#permutataion_panlindrome("taco cat")

class Test(unittest.TestCase):
    set_of_strings = [("malayalam", True),("heeh ollo",True),("Hello", False)]

    def test_palindrome(self):
        for each_test in self.set_of_strings:
            result = permutataion_panlindrome(each_test[0])
            self.assertEqual(result, each_test[1])

if __name__ == '__main__':
    unittest.main()


