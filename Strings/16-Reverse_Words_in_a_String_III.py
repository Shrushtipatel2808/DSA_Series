# Day 16: Reverse Words in a String III
# LeetCode Problem: 557
# Difficulty: Easy
# Topic: Strings, Two Pointers
#
# Problem Description:
# Given a string s, reverse the characters of each word
# while preserving the original word order and whitespace.
#
# Approach:
# 1. Use split(" ") to divide the sentence into words.
# 2. Empty strings represent consecutive spaces.
# 3. Convert each word into a list of characters.
# 4. Use Two Pointers to swap characters.
# 5. Join the reversed characters back into a string.
# 6. Join all elements without adding extra spaces.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        result = []

        for word in words:
            if word == "":
                result.append("")
            else:
                chars = list(word)

                for i in range(len(chars)//2):
                    chars[i], chars[len(chars)-1-i] = chars[len(chars)-1-i], chars[i]

                result.append("".join(chars))

        return " ".join(result)


s = "Let's take   LeetCode   contest"
obj = Solution()
op = obj.reverseWords(s)

print(f"The Output is: {op}")