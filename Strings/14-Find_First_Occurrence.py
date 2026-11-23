# Day 14: Find the Index of the First Occurrence in a String
# LeetCode Problem: 28
# Difficulty: Easy
# Topic: Strings
#
# Problem:
# Find the first occurrence of needle in haystack.
# Return its starting index. If not found, return -1.
#
# Approach:
# 1. Check if needle is empty.
# 2. Iterate through haystack.
# 3. Compare substrings with needle using slicing.
# 4. Return the index if matched, otherwise return -1.
#
# Time Complexity: O(n * m)
# Space Complexity: O(m)
class Solution():
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if(haystack[i: i+len(needle) ]== needle):
                return i
        if needle == "":
                return 0
        return -1
          
obj=Solution()
haystack = "sadbutsad"
needle = "sad"
result=obj.strStr(haystack,needle)
print(result)