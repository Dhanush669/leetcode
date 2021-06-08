class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        le=0
        fullis=[]
        sorful=[]
        val=0
        if len(nums1)>len(nums2):
            le=len(nums1)
        else:
            le=len(nums2)
        for i in range(0,le):
            if i<len(nums1):
                fullis.append(nums1[i])
            if i<len(nums2):
                fullis.append(nums2[i])
        fullis.sort()
        val=len(fullis)//2
        if len(fullis)%2==0:
            median=(fullis[val]+fullis[val-1])/2
        
        else:
            median=fullis[val]
        return float(median)