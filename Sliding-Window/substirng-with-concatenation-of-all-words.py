from collections import Counter

class Solution:
    ''' This class contains solution to Leetcode 30 - Substring with Concatenation of All Words'''
    def find_substring(self, s, words):
        ''' This function finds substring with concatenation of all words'''
        if not s or not words: 
            return []

        word_len, word_count = len(words[0]), len(words)
        substr = word_len * word_count
        word_freq = Counter(words)
        result = []

        for i in range(word_len):
            left, right = i, i
            current_freq = Counter()

            while right + word_len <= len(s):
                current_word = s[right: right + word_len]
                right += word_len
                current_freq[current_word] += 1

                while current_freq[current_word] > word_freq[current_word]:
                    current_freq[s[left : left + word_len]] -= 1
                    left += word_len

                if right - left == substr: 
                    result.append(left)
        return result
