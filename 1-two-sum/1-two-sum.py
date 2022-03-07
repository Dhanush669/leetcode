class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op=[]
        for i in range(0,len(nums)):
            ol=[]
            ol=nums[i+1:]
            res=target-nums[i]
            if res in ol:
                op.append(i)
                op.append(nums.index(res,i+1))
                break
        return op            
            
      