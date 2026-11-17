# ==========================================
# Problem Name: Move Zeroes
# LeetCode Number: 283
# Difficulty: Easy
# Topic: Array
# Approach: Using Extra Array
#
# Problem Description:
# Given an integer array nums, move all zeroes
# to the end of the array while maintaining
# the relative order of non-zero elements.
#
# The original array must be modified.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================

class Solution():
    def moveZeroes(self, nums):
        new_arr=[]
        for i in range(len(nums)):
            if(nums[i]!=0):
                new_arr.append(nums[i])
        count= nums.count(0)
        for j in range(count):
            new_arr.append(0)

        return new_arr
obj=Solution()
nums=[0,1,0,3,0,12]
r=obj.moveZeroes(nums)
print(r)

