class Solution(object):
    def frequencySort(self, s):
        D = {}
        for i in set(s):
            D[i] = s.count(i)
        
        ans = ''
        for c, f in sorted(D.items(), key = lambda x : x[1], reverse = True):
            ans += c * f
        return ans
        