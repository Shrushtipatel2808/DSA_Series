
# ==========================================
# Problem Name: Valid Palindrome
# LeetCode Number: 125
# Difficulty: Easy
# Topic: String
# Approach: Two Pointers / String Filtering
#
# Problem Description:
# Given a string s, check whether it is a
# palindrome after converting uppercase letters
# to lowercase and removing all non-alphanumeric
# characters.
#
# Return True if it is a palindrome,
# otherwise return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==========================================


# Alphanumeric: A-Z, a-z ,0-9   
class Solution(object):
    def isPalindrome(self, s):
        new_str=""
        for char in s:
            if char.isalnum():
                new_str= new_str + char.lower()
        if new_str==new_str[::-1]:
            return True
        else:
            return False
obj=Solution()
s = "A man, a plan, a canal: Panama"
result=obj.isPalindrome(s)
print("Result= ",result)
