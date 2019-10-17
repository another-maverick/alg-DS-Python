#!/usr/bin/env python3
import unittest

def zero_out_array(inpMatrix):
    outer_len = len(inpMatrix)
    inner_length = len(inpMatrix[0])

    rows_to_nullify = set()
    cols_to_nullify = set()


    for i in range(outer_len):
        for j in range(inner_length):
            if inpMatrix[i][j] == 0:
                rows_to_nullify.add(i)
                cols_to_nullify.add(j)
    print(rows_to_nullify)
    print(cols_to_nullify)
    for x in rows_to_nullify:
        zero_row(inpMatrix, x)

    for y in cols_to_nullify:
        zero_col(inpMatrix, y)

    print(inpMatrix)
    return inpMatrix


def zero_row(inpMatrix, row):
    x = len(inpMatrix[0])
    for i in range(x):
        inpMatrix[row][i] = 0

def zero_col(inpMatrix, col):
    x = len(inpMatrix)
    for i in range(x):
        inpMatrix[i][col] = 0


class Test(unittest.TestCase):

    test_data = [([[1,2,3,4,5],[1,0,3,5,6],[8,7,6,5,6],[23,11,0,11,56],[77,8,4,2,1]],
                 [[1,0,0,4,5],[0,0,0,0,0],[8,0,0,5,6],[0,0,0,0,0],[77,0,0,2,1]])]

    def test_zero_out_array(self):
        for each_test, each_result in self.test_data:
            res = zero_out_array(each_test)
            self.assertEqual(res, each_result)


if __name__ == '__main__':
    unittest.main()