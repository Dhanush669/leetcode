class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        fSum=nums[0]
        lSum=nums[0]
        if len(nums)==2:
            return max(sum(nums),nums[0],nums[1])
        prev=0
        
        for i in range(1,len(nums)):
            lSum=max(lSum+nums[i],nums[i])
            if lSum>fSum:
                fSum=lSum    
        print(lSum,fSum)        
        return max(lSum,fSum,sum(nums))                
                
        