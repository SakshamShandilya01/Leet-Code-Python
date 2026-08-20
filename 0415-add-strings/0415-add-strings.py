class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        i = len(num1) - 1
        j = len(num2) - 1
        ans = []

        carry = 0

        while i>=0 or j>=0 or carry:
            x = int(num1[i]) if i>=0 else 0
            y = int(num2[j]) if j>=0 else 0

            total = x + y + carry

            ans.append(str(total%10))

            carry = total//10

            i -= 1
            j -= 1

        result = ''.join(ans[::-1])
        return result
        