class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        if not s or not t: return ""
        
        target_chars, required_chars = Counter(t), len(target_chars)
        window_chars, formed_chars, left = {}, 0, 0
        min_len, min_window = float('inf'), ""
        
        for right in range(len(s)):
            char = s[right]
            window_chars[char] = window_chars.get(char, 0) + 1
            if char in target_chars and window_chars[char] == target_chars[char]: formed_chars += 1            
            while formed_chars == required_chars and left <= right:
                current_len = right - left + 1                
                if current_len < min_len:
                    min_len = current_len
                    min_window = s[left:right+1]                
                left_char = s[left]
                window_chars[left_char] -= 1                
                if left_char in target_chars and window_chars[left_char] < target_chars[left_char]: formed_chars -= 1
                left += 1
        return min_window