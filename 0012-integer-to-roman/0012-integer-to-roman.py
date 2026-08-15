class Solution(object):
    def intToRoman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""

        for i in range(len(val)):
            while num >= val[i]:
                result += symbols[i]
                num -= val[i]

        return result