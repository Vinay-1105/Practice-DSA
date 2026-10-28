class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    #first transpose the matrix by swapping rows with columns, and reverse eachrow.
        row=len(matrix)
        col=len(matrix[0])

        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for k in range(row):
            matrix[k].reverse()