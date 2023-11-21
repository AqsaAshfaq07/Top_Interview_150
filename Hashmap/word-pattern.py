class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_counter = {}
        words_counter = {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            if pattern_counter.get(pattern[i]) != words_counter.get(words[i]):
                return False
            pattern_counter[pattern[i]] = words_counter[words[i]] = i

        return True
        