# ==========================================
# Problem Name: First Unique Character in a String
# LeetCode Number: 387
# Difficulty: Easy
# Topic: String
# Approach: Character Frequency Counting
#
# Problem Description:
# Given a string s, find the first non-repeating
# character and return its index.
#
# If no unique character exists, return -1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================

class Solution():
    def firstUniqChar(self, s):
        for ele in s:
            if s.count(ele)==1:
                return s.index(ele)
        return -1

obj=Solution()
s = "loveleetcode"
result=obj.firstUniqChar(s)
print("Result= ",result)
