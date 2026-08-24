class Solution:
    def frequencySort(self, s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        n = len(s)
        buckets = [[] for _ in range(n + 1)]  

        for ch, count in freq.items():
            buckets[count].append(ch) 

        result = []
        for count in range(n, 0, -1):
            for ch in buckets[count]:
                result.append(ch * count)

        return "".join(result)