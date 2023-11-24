class Solution(object):
    ''' https://leetcode.com/problems/group-anagrams/'''
    def group_anagrams(self, strs):
        ''' Given an array of strings strs, group the anagrams together. You can return the answer in any order.'''
        counter = dict(list)
        for word in strs:
            counter[tuple(sorted(word))].append(word)
        return counter.values()
        