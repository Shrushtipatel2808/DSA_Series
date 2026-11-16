# Problem: Two Sum
# LeetCode: 1
# Difficulty: Easy
# Topic: Array
# Approach: Brute Force
# Time Complexity: O(n²)
# Space Complexity: O(1)

# 1.TWO SUM : You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.



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
