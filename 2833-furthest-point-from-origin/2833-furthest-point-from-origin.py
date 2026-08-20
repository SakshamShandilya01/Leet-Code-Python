class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
         R = moves.count('R')
         L = moves.count('L')
         blanks = moves.count('_')
         return abs(R - L) + blanks
        