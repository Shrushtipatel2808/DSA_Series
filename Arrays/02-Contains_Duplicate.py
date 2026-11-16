
# Problem Name: Contains Duplicate
# LeetCode Number: 217
# Difficulty: Easy
# Topic: Array
# Approach: Brute Force (Nested Loops)
#
# Problem Description:
# Given an integer array nums, check whether
# any value appears at least twice.
# Return True if duplicate exists,
# otherwise return False.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def containsDuplicate(self, nums):

        for i in range(len(nums)):

            for j in range(len(nums)):

                if i != j and nums[i] == nums[j]:
                    return True

        return False


# Function Call
obj = Solution()

nums = [1, 2, 3, 4, 10]

result = obj.containsDuplicate(nums)

print("Answer:", result)
