class Solution:
    def romanToInt(self, s):
        # numbers are written left to right

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        n = len(s)
        i = 0

        while i < n:
            if i != n-1 and roman[s[i]] < roman[s[i+1]]:
                integer += roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                integer += roman[s[i]]
                i += 1

        return integer