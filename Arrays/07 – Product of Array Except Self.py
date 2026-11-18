
# ==========================================
# Problem Name: Product of Array Except Self
# LeetCode Number: 238
# Difficulty: Medium
# Topic: Array
# Approach: Prefix and Suffix Product
#
# Problem Description:
# Given an integer array nums, return an array
# answer such that answer[i] is equal to the
# product of all elements of nums except nums[i].
#
# The solution should not use the division operation.
#
# Time Complexity: O(n)
# Space Complexity: O(1) extra space
# (Output array is not counted)
# ==========================================

class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        result=[1]*n
        prefix=1
        #prefix
        for i in range(n):  #i=0,1,2,3,4    
            result[i]=prefix    #result[0]=  [1  1  2    10  30]
            prefix=prefix*nums[i]        #prefix=1  2   10  30  120
        #suffix
        suffix=1
        for i in range(n-1,-1,-1):
            result[i]=result[i]*suffix
            suffix=suffix*nums[i]
        return result
# Testing
obj = Solution()
nums = [1, 2, 5, 3, 4]

result = obj.productExceptSelf(nums)

print("Result:", result)
