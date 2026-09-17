class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for k in nums:
            d[k]+=1
        return max(d.items(), key=lambda x: x[1])[0]