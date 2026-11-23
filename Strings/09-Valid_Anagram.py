# ==========================================
# Problem Name: Valid Anagram
# LeetCode Number: 242
# Difficulty: Easy
# Topic: String
# Approach: Character Frequency Counting
#
# Problem Description:
# Given two strings s and t, determine whether
# t is an anagram of s.
#
# An anagram contains the same characters
# with the same frequency, but in a different
# order.
#
# Return True if t is an anagram of s,
# otherwise return False.
#
# Time Complexity: O(n²) 
# Space Complexity: O(1)
# ==========================================

class Solution():
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        for char in s:
            if s.count(char)!=t.count(char):
                return False
        return True
obj=Solution()
s = "aabb"
t = "ababt"
print(obj.isAnagram(s, t))