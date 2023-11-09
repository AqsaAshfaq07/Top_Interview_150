class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        curr = 0
        for ch in t:
            if ch == s[curr]: 
                curr += 1
                if curr == len(s): return True 

        return False