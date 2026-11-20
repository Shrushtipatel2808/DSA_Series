class Solution():
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        for char in s:
            if s.count(char)!=t.count(char):
                return False
        return True
obj=Solution()
s = "aabb"
t = "ababt"
print(obj.isAnagram(s, t))