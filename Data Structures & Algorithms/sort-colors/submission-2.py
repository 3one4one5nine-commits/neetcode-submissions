class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redend=0
        whiend=0
        if nums[0]==0:
            whiend+=1
            redend+=1
        if nums[0]==1:
            whiend+=1
        for i in range(len(nums)-1):
            store=nums[i+1]
            if nums[i+1]==0:
                temp=nums[redend]
                nums[redend]=0
                nums[i+1]=temp
            if nums[i+1]==1:
                temp=nums[whiend]
                nums[whiend]=1
                nums[i+1]=temp
            if store==0:
                whiend+=1
                redend+=1
            if store==1:
                whiend+=1
            
