class Solution:
    def sumGame(self, num):
        n = len(num)
        cnt1 = cnt2 = 0
        sum1 = sum2 = 0
        
        for i in range(n // 2):
            if num[i] == '?':
                cnt1 += 1
            else:
                sum1 += int(num[i])
        
        for i in range(n // 2, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                sum2 += int(num[i])
        
        cnt = cnt1 + cnt2
        diff = sum1 - sum2
        
        if cnt % 2 == 1:
            return True  
        
        return diff != (cnt2 - cnt1) * 9 // 2