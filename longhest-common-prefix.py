class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        strs.sort()
        common_prefix = []
        first_word, last_word = strs[0], strs[-1]
        for i in range(len(first_word)):
            if i < len(last_word) and first_word[i] == last_word[i]:
                common_prefix.append(first_word[i])
            else: break
        return ''.join(common_prefix)