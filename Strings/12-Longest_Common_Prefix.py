
# ==========================================
# Problem Name: Longest Common Prefix
# LeetCode Number: 14
# Difficulty: Easy
# Topic: String
# Approach: String Comparison
#
# Time Complexity: O(n * m)
# Space Complexity: O(m)
# ==========================================

class Solution():
    def longestCommonPrefix(self, strs):
        first = strs[0]

        for i in range(len(first)):
            for word in strs:
                if i >= len(word) or first[i] != word[i]:
                    return first[:i]

        return first


obj = Solution()
strs = ["apple", "application", "apply"]

result = obj.longestCommonPrefix(strs)
print(result)
