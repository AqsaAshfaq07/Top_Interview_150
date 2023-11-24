class Solution(object):
    ''' https://leetcode.com/problems/valid-anagram/'''
    def is_anagram(self, s, t):
        ''' Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
        if len(s) != len(t): 
            return False

        prc, prc2 = list(s), list(t)
        prc.sort()
        prc2.sort()

        return prc2 == prc
