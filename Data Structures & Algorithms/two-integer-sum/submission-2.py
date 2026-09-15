class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker={}
        for i,j in enumerate(nums):
            if j in checker:
                return [checker[j], i]
            checker[target-j]=i