class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    return True
            else:
                return False        

obj=Solution()
nums=[1,2,3,4,10]
result=obj.containsDuplicate(nums)
print("Answer: ",result)