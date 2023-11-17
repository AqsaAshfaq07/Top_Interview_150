class Solution:
    def set_zeroes(self, matrix):
        ''' Do not return anything, modify matrix in-place instead. '''
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            matrix[i] = [0] * cols        
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
