# Problem Name: Two Sum
# LeetCode Number: 1
# Difficulty: Easy
# Topic: Array
# Approach: Brute Force (Nested Loops)
#
# Problem Description:
# Given an array of integers nums and an integer
# target, return the indices of two numbers
# whose sum equals the target.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
                num1 = nums[i]
                num2 = target - num1

                for j in range(len(nums)):
                    if i != j and nums[j] == num2:
                        return [i, j]


# Function call
obj = Solution()

nums = [2, 7, 11, 15]
target = 22

result = obj.twoSum(nums, target)

print("Answer:", result)
