class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y={}
        for i in range(len(nums)):
            if nums[i] in y:
                return [y[nums[i]], i]
            y[target-nums[i]]=i