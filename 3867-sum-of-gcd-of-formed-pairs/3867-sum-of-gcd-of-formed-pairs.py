from math import gcd

class Solution(object):
    def gcdSum(self, nums):
        arr = []
        maxi = 0
        ans = 0

        for num in nums:
            if num > maxi:
                maxi = num
            arr.append(gcd(num, maxi))

        arr.sort()

        for i in range(len(arr)//2):
            ans += gcd(arr[i], arr[len(arr)-1-i])

        return ans