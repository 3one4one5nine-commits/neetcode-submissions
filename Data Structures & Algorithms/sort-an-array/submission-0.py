class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a=[]
        while len(nums)!=0:
            a.append(nums.pop(nums.index(min(nums))))
        return a