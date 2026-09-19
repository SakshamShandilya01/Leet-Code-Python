class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= (int)s.size()) return s;

        vector<string> rows(numRows);
        int r = 0, step = 1;

        for (char ch : s) {
            rows[r] += ch;
            if (r == 0) step = 1;
            else if (r == numRows - 1) step = -1;
            r += step;
        }

        string ans;
        for (auto& row : rows) ans += row;
        return ans;
    }
};