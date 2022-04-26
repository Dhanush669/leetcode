from collections import defaultdict
class Solution:
    def defa(self):
        return 0
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic=defaultdict(self.defa)
        for i in nums:
            if dic[i]>=1:
                return True
            dic[i]+=1
        # for val in dic:
        #     if dic[val]>1:
        #         return True
        return False    