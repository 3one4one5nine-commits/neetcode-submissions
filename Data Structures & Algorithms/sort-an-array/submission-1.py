class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(dalist):
            if len(dalist)<=1:
                return dalist
            r=len(dalist)//2
            left=mergeSort(dalist[:r])
            right=mergeSort(dalist[r:])
            return merge(left, right)
        
        def merge(left, right):
            i=j=0
            dalist2=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    dalist2.append(left[i])
                    i+=1
                else:
                    dalist2.append(right[j])
                    j+=1
            dalist2+=left[i:]
            dalist2+=right[j:]
            return dalist2
        
        return mergeSort(nums)