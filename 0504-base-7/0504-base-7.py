class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        result = ""

        while num > 0:
            result = str(num % 7) + result
            num = num // 7

        return sign + result
        