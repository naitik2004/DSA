class Solution {
public:
    bool isSafe(vector<vector<char>>& board, int row, int col, char dig) {
        // Check row
        for (int j = 0; j < 9; j++) {
            if (board[row][j] == dig)
                return false;
        }

        // Check column
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == dig)
                return false;
        }

        // Check 3x3 box
        int srow = (row / 3) * 3;
        int scol = (col / 3) * 3;
        for (int i = srow; i < srow + 3; i++) {
            for (int j = scol; j < scol + 3; j++) {
                if (board[i][j] == dig)
                    return false;
            }
        }

        return true;
    }

    bool helper(vector<vector<char>>& board, int row, int col) {
        if (row == 9) return true;

        int nrow = row;
        int ncol = col + 1;
        if (ncol == 9) {
            ncol = 0;
            nrow++;
        }

        if (board[row][col] != '.') {
            return helper(board, nrow, ncol);
        }

        for (char dig = '1'; dig <= '9'; dig++) {
            if (isSafe(board, row, col, dig)) {
                board[row][col] = dig;
                if (helper(board, nrow, ncol)) return true;
                board[row][col] = '.';
            }
        }

        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        helper(board, 0, 0);
    }
};
