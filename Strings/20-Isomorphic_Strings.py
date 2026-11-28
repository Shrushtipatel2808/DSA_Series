
# LeetCode 205: Isomorphic Strings
# Difficulty: Easy
# Topic: Strings, Dictionary, Hash Mapping
# Day: 21
#
# Problem:
# Given two strings s and t, determine whether they are
# isomorphic or not.
#
# Two strings are isomorphic if each character in s can be
# mapped to exactly one character in t.
# Every character mapping must be consistent.
#
# Approach:
# 1. Create two dictionaries for mapping.
# 2. First dictionary stores s to t mapping.
# 3. Second dictionary stores t to s mapping.
# 4. Traverse both strings using a loop.
# 5. Check whether existing mappings are consistent.
# 6. If a mapping conflicts, return False.
# 7. Otherwise, return True.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for i in range(len(s)):

            char_s = s[i]
            char_t = t[i]

            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t

            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s

        return True


# Test Cases
obj = Solution()

s = "egg"
t = "add"

result = obj.isIsomorphic(s, t)
print("Output:", result)
