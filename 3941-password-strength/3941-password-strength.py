class Solution(object):
    def passwordStrength(self, password):
        a = set(password)
        total = 0

        for i in a:
            if i.islower():
                total+=1
            elif i.isupper():
                total +=2
            elif i.isdigit():
                total+=3
            else:
                total+=5
        return total



        