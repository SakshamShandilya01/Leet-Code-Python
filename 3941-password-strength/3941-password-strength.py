class Solution(object):
    def passwordStrength(self, password):
        lower = set()
        upper = set()
        special = set()
        digit = set()
        special_char = "!@#$"

        for i in password:
            if i.islower():
                lower.add(i)
            elif i.isupper():
                upper.add(i)
            elif i.isdigit():
                digit.add(i)
            elif i in special_char:
                special.add(i)

        strength = len(lower)*1 + len(upper)*2 + len(digit)*3 + len(special)*5
        return strength


        