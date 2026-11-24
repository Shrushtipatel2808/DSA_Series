
class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        result=[]
        for word in words:
            chars=list(word)
            for i in range(len(chars)//2):
                chars[i],chars[len(chars)-1-i]=chars[len(chars)-1-i],chars[i]
            result.append("".join(chars))
        return " ".join(result)
s = "Let's take LeetCode contest"
obj=Solution()
op=obj.reverseWords(s)
print(f"The Output is: {op}")


