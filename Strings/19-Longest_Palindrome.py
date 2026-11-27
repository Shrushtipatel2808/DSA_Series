
# LeetCode 409: Longest Palindrome
# Difficulty: Easy
# Topic: Strings, Dictionary, Hash Table
# Day: 19
#
# Problem:
# Given a string s, find the length of the longest
# palindrome that can be built using its characters.
#
# Approach:
# 1. Create a dictionary to count character frequencies.
# 2. Iterate through all frequency values.
# 3. If frequency is even, add the complete frequency.
# 4. If frequency is odd, add frequency - 1.
# 5. Count odd frequencies.
# 6. If any odd frequency exists, add 1 for the center.
# 7. Return the final result.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution():
    def longestPalindrome(self, s):
        letters={}
        result=0
        odd=0
        for char in s:
            if char not in letters:
                letters[char]=1
            else:
                letters[char]+=1
        for i in letters.values():
            if(i>1):
                if(i%2==0):
                    result+=i
                else:
                    result+=i-1
                    odd+=1
            else:
                odd+=1
        if(odd>1):
            result+=1
        return result

obj=Solution()
s="abccccdd"
result=obj.longestPalindrome(s)
print("Output: ",result)