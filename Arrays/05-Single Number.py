# ==========================================
# Problem Name: Single Number
# LeetCode Number: 136
# Difficulty: Easy
# Topic: Array
# Approach: To be decided
#
# Problem Description:
# Given a non-empty array of integers, every
# element appears twice except for one.
# Find the element that appears only once.
#
# Time Complexity: To be determined
# Space Complexity: To be determined
# ==========================================

class Solution:
    def find(self,nums):
        result=0
        for elem in nums:
            result=result ^ elem
        return result
obj=Solution()
nums=[4,1,7,2,5,1,2,4,7]
result=obj.find(nums)
print("Result= ",result)

