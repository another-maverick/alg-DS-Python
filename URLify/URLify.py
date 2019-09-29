
import unittest
import copy


def URLify(input_string, content_length):
    complete_length = len(input_string)
    num_of_spaces = 0

    output_string = copy.deepcopy(input_string)

    for i in range(content_length):
        if input_string[i] != " ":
            continue
        else:
            for j in range(content_length - 1 + 2*(num_of_spaces), i + 2*(num_of_spaces), -1):
                output_string[ j + 2 ] =  output_string[j]
            output_string[i + 2*num_of_spaces:i + 2*num_of_spaces + 3] = '%20'
            print(output_string)
            num_of_spaces += 1
    print(output_string)
    return output_string






class Test(unittest.TestCase):
    data = [(list("much ado about nothing      "), 22,list("much%20ado%20about%20nothing"))]

    def test(self):
        for [test_string, length, expected] in self.data:
            actual = URLify( test_string, length )
            self.assertEqual( actual, expected )

if __name__ == '__main__':
    URLify( list( "much ado about nothing      " ), 22)
    URLify(list("hi boy  "),6)
    URLify(list("who am i    "),8)
    unittest.main()


