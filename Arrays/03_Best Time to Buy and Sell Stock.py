
# ==========================================
# Problem Name: Best Time to Buy and Sell Stock
# LeetCode Number: 121
# Difficulty: Easy
# Topic: Array
# Approach: Brute Force
#
# Problem Description:
# Given an array of prices where prices[i] is
# the price of a stock on the ith day,
# find the maximum profit you can achieve.
#
# You can buy the stock on one day and sell it
# on a future day.
#
# If no profit is possible, return 0.
#
# Time Complexity: O(n^2) - Brute Force
# Space Complexity: O(1)
# ==========================================

class Best:
    def find(self,prices):
        max_profit=0
        for i in range(len(prices)):    # 0,1,2,3,4,5
            for j in range(i+1,len(prices)):    #1,2,3,4,5
                profit=prices[j]-prices[i]
                if(profit>max_profit):
                    max_profit=profit
        return max_profit

obj=Best()
prices=[7,1,5,3,6,4]            
result=obj.find(prices)
print("Maximised profit: ",result)

