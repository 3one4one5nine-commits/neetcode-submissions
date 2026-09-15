class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i,j in enumerate(nums):
            if j in a:
                return True
            a[j]=i
        return False