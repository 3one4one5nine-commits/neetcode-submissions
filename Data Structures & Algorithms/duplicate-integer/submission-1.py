class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=[]
        for i in nums:
            if a.count(i)!=0:
                return True
            a.append(i)
        return False