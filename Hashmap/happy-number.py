class Solution(object):
    ''' Implementation of the leetcode problem : Happy Number'''
    def isHappy(self, n):
        ''' https://leetcode.com/problems/happy-number/'''
        vals = [n]
        ans = n
        while(ans !=1):
            nunum = 0
            for c in str(ans):
                nunum += int(c)**2
            if nunum in vals: 
                return False
            else: 
                vals.append(nunum)
                ans = nunum
        return True
        