
# ==========================================
# Problem Name: Find Pivot Index
# LeetCode Number: 724
# Difficulty: Easy
# Topic: Array
# Approach: Prefix Sum
#
# Problem Description:
# Given an array of integers nums, calculate
# the pivot index of this array.
#
# The pivot index is the index where the sum
# of all the numbers strictly to the left of
# the index is equal to the sum of all the
# numbers strictly to the right of the index.
#
# Return the leftmost pivot index.
# If no such index exists, return -1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================

class Solution():
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            left_sum=0
            right_sum=0

            for j in range(i):
                left_sum=left_sum+nums[j]

            for j in range(i+1,len(nums)):
                right_sum=right_sum+nums[j]

            if(left_sum==right_sum):
                return i
        return -1

obj=Solution()
nums = [1, 17, 3, 6, 5, 16]
result=obj.pivotIndex(nums)
print("Pivot index= ",result)



