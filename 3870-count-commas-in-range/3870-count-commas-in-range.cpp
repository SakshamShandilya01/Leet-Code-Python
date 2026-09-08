class Solution {
public:
    int countCommas(int n) {
        long long ans = 0;
        long long lo = 1, hi = 9; // 1-digit range
        int digits = 1;

        while (lo <= n) {
            long long rangeHi = min((long long)n, hi);
            long long count = rangeHi - lo + 1;   // how many numbers have this digit length
            int commasPerNum = (digits - 1) / 3;
            ans += count * commasPerNum;

            digits++;
            lo = hi + 1;
            hi = hi * 10 + 9;
        }

        return (int)ans;
    }
};