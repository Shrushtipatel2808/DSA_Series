# Day 15: Reverse String
# LeetCode Problem: 344
# Difficulty: Easy
# Topic: Strings, Two Pointers
#
# Problem Description:
# Reverse the given array of characters in-place.
# Modify the original array without creating a new array.
#
# Approach:
# 1. Use two pointers (left and right).
# 2. Start from the first and last index.
# 3. Swap the characters at both positions.
# 4. Move towards the center until the pointers meet.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution():
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]

s = ["h", "e", "l", "l", "o","m","y"]
obj=Solution()
obj.reverseString(s)
print(s)