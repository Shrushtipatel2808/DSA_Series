
# ==========================================
# Problem Name: Valid Parentheses
# LeetCode Number: 20
# Difficulty: Easy
# Topic: String, Stack
# Approach: Stack
#
# Problem Description:
# Given a string containing brackets,
# check whether they are valid or not.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================

class Solution:
    def isValid(self, s):
        stack=[]
        pairs={
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in pairs:
                if not stack or stack[-1] !=pairs[char]:
                    return False
                stack.pop()
        return len(stack)==0
            

obj = Solution()

s ="{[]}"

result = obj.isValid(s)

print(result)
