# LeetCode 67: Add Binary
# Difficulty: Easy
# Topic: Strings, Binary Addition
# Day: 18

# Problem:
# Given two binary strings a and b, return their sum
# as a binary string.

# Approach:
# 1. Start adding bits from right to left.
# 2. Initialize carry = 0.
# 3. Add both bits and carry.
# 4. Use total % 2 to get the current value.
# 5. Use total // 2 to calculate the next carry.
# 6. Add the value at the beginning of the result.
# 7. Repeat until both strings and carry are processed.

# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))
class Solution(object):
    def addBinary(self, a, b):
        i=len(a)-1  #3
        j=len(b)-1  #3
        carry=0

        result=""
        while(i>=0 or j>=0 or carry==1):
            total=carry             #total=0, 0 , 1 , 0 ,1
            if(i>=0):
                total+=int(a[i])    #total= 0 , 1 ,1 ,1
                i-=1
            if(j>=0):
                total+=int(b[j])    #total=0 , 2 , 1 , 2
                j-=1
            value=total%2           #value= 1 , 0 , 1 ,0 , 1
            carry=total//2          #carry= 0 , 1 , 0,1, 0
            result=str(value)+result    #result= "10101"
        return result

obj=Solution()
a = "1010"
b = "1011"
ans=obj.addBinary(a,b)
print("Output: ",ans)
