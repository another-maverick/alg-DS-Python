#!/usr/bin/env python3

import unittest


def rotate(inpMatrix):
    l = len(inpMatrix)
    outmatrix = []
    outMatrix_temp = []

    for i in range(len(inpMatrix)):
        outMatrix_temp = []
        for j in reversed(range(len(inpMatrix))):
            print(str(i) +" ==== " + str(j))
            outMatrix_temp.append(inpMatrix[j][i])
            print(outMatrix_temp)
        outmatrix.append(outMatrix_temp)
    return outmatrix


'''
if __name__ == '__main__':
    inpMatrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    res = rotate(inpMatrix)
    print(res)
'''
class Test(unittest.TestCase):
    test_data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate(self):
        for [test_case, test_res] in self.test_data:
            res = rotate(test_case)
            self.assertEqual(res, test_res)

if __name__ == '__main__':
    unittest.main()