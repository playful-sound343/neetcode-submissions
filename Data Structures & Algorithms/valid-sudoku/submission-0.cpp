#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 9 rows, 9 cols, 9 boxes — each tracking numbers 1 through 9
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char cell = board[r][c];
                if (cell == '.') continue; // Skip empty cells

                int num = cell - '1'; // Map char '1'-'9' to index 0-8
                int boxIdx = (r / 3) * 3 + (c / 3);

                // If we've already marked this number true in row, col, or box -> Duplicate!
                if (rows[r][num] || cols[c][num] || boxes[boxIdx][num]) {
                    return false;
                }

                // Mark this number as seen
                rows[r][num] = true;
                cols[c][num] = true;
                boxes[boxIdx][num] = true;
            }
        }
        return true;
    }
};
