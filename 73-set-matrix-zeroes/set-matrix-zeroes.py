class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             for col in range(n):
        #                 if matrix[i][col] != 0:
        #                     matrix[i][col] = -1
        #             for row in range(m):
        #                 if matrix[row][j] != 0:
        #                     matrix[row][j] = -1
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == -1:
        #             matrix[i][j] = 0

        m = len(matrix) # no. of rows
        n = len(matrix[0]) # no. of columns

        row = [0] * m
        col = [0] * n

        # 1. mark rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                # If element is zero, mark its row and column
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # 2. set cells to zero based on markers
        for i in range(m):
            for j in range(n):
                # If the row or column is marked, set cell to zero
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
