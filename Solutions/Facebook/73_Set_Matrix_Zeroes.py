class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        flag = False
        len_row = len(matrix)
        len_col = len(matrix[0])

        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0

                    if col == 0:
                        flag = True
                    else:
                        matrix[0][col] = 0

        for row in range(1, len_row):
            for col in range(1, len_col):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(len_col):
                matrix[0][col] = 0

        if flag:
            for row in range(len_row):
                matrix[row][0] = 0

        print(matrix)
