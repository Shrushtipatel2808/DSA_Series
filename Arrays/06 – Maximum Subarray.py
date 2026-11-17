# ==========================================
# Problem Name: Maximum Subarray
# LeetCode Number: 53
# Difficulty: Medium
# Topic: Array
# Approach: To be decided
#
# Problem Description:
# Find the contiguous subarray with the largest sum
# and return that sum.
#
# Time Complexity: To be decided
# Space Complexity: To be decided
# ==========================================

class Solution:
    def maxSubArray(self , nums):
        current_sum=nums[0]
        max_sum=nums[0]

        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_sum=max(current_sum,max_sum)
        return max_sum
obj=Solution()
nums = [5, -2, 4]
result=obj.maxSubArray(nums)
print("Result: ",result)