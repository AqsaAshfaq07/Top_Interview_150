class Solution(object):
    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ctr_s = {}
        ctr_t = {}
        for char1, char2 in zip(s, t):
            if char1 not in ctr_s and char2 not in ctr_t: ctr_s[char1], ctr_t[char2] = char2, char1
            else:
                if ctr_s.get(char1) != char2 or ctr_t.get(char2) != char1: return False

        return True
