# LeetCode 58 - Length of Last Word
# Difficulty: Easy
# Topic: String

# Given a string s, return the length of the last word.
# A word is a sequence of non-space characters.

# Approach:
# 1. Remove starting and ending spaces using strip().
# 2. Start traversing the string from right to left.
# 3. If the character is not a space, increase count.
# 4. If a space is found after counting characters, stop the loop.
# 5. Return the count.

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution():
    def lengthOfLastWord(self, s):
        s=s.strip()
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                count+=1
            else:
                if count>0:
                    break
        return count
obj=Solution()
s = "   fly me   to   the moon  "
ans=obj.lengthOfLastWord(s)
print("Output is: ",ans)
