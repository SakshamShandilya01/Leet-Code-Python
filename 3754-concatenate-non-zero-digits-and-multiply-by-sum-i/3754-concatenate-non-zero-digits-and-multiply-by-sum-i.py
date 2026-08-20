class Solution(object):
    def sumAndMultiply(self, n):

        if n == 0:
            return 0

        digits = []
        count = 0


        while n > 0:
            digit = n%10

            if digit != 0:
                count += digit
                digits.append(str(digit))

            n //=10
        digits.reverse()
        number = int("".join(digits))

        return number * count

        
        
                

        

        


        