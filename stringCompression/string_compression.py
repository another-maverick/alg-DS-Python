#!/usr/bin/env python3
# This function performs string compression. For example, aabbccc is a2b2c3
# returns the smaller of original string or the compressed string

import unittest

def string_compression(input_string):
    count_chars = []
    char_count = 0
    input_list = list(input_string)

    for i in range(len(input_list)):
        if i !=0 and input_list[i] != input_list[i - 1]:
            count_chars.append(input_list[i-1] + str(char_count))
            char_count = 0
        char_count += 1

    #last char
    count_chars.append(input_list[-1] + str(char_count))

    return min(input_string, ''.join(count_chars), key=len )


print(string_compression("aabbccddeeeeeeee"))

class Test(unittest.TestCase):
    input_data = [('aabbccddee','aabbccddee' ),('aaabbbcccddd','a3b3c3d3')]

    def test_string_compression(self):
        for each_test in self.input_data:
            result = string_compression(each_test[0])
            self.assertEqual(result, each_test[1])


if __name__ == '__main__':
    unittest.main()





