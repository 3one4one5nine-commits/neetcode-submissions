class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        finList=[]
        pairs=dict1.items()
        for _ in range(k):
            a=max(pairs, key=lambda x:x[1])[0]
            dict1.pop(a)
            finList.append(a)
        return finList
