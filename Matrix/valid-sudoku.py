class Solution:
    '''This class presents solution for a famous leetcode problem Valid Sudoku'''
    def is_valid_sudoku(self, board):
        '''This function is the actual implementation of Valid Sudoku problem'''
        for i in range(9):
            row_set = set()
            col_set = set()
            board_set = set()

            for j in range(9):
                row_box = board[i][j]
                col_box = board[j][i]
                board_box = board[3* (i // 3) + (j // 3)][3* (i%3) + (j%3)]

                if row_box != '.':
                    if row_box in row_set: 
                        return False
                    row_set.add(row_box)
                if col_box != '.':
                    if col_box in col_set: 
                        return False
                    col_set.add(col_box) 
                if board_box != '.':
                    if board_box in board_set: 
                        return False
                    board_set.add(board_box)

        return True
    