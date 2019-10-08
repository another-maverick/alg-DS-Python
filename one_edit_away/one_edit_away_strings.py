#!/usr/bin/env python3

import unittest

def one_edit_away_strings(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        print('difference in length is more than 1')
        return False

    num_of_dissimilarities = 0
    list1 = list(str1)
    list2 = list(str2)

    for i in range(min(len(list1), len(list2))):
        if num_of_dissimilarities < 2:
            if ord(list1[0]) == ord(list2[0]):
                list1.pop(0)
                list2.pop(0)
            else:
                list1.pop(0)
                if ord(list2[0]) != ord(list1[0]):
                    list2.pop(0)
                num_of_dissimilarities += 1

    if num_of_dissimilarities <= 1:
        print("The strings are one edit away")
        return True

    print("The strings are NOT one edit away")
    return False


# one_edit_away_strings("pale","bake")

class Test(unittest.TestCase):
    set_of_strings = [("pale", "ple", True), ("pales", "pale", True), ("pale", "bale", True), ("pale", "bake", False)]

    def test_one_edit_away(self):
        for each_test in self.set_of_strings:
            res = one_edit_away_strings(each_test[0],each_test[1])
            self.assertEqual(res, each_test[2])


if __name__ == '__main__':
    unittest.main()


