class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redend=0
        whiend=0
        for i in range(len(nums)):
            store=nums[i]
            if nums[i]==0:
                temp=nums[redend]
                nums[redend]=0
                nums[i]=temp
            if nums[i]==1:
                temp=nums[whiend]
                nums[whiend]=1
                nums[i]=temp
            if store==0:
                whiend+=1
                redend+=1
            if store==1:
                whiend+=1
            
