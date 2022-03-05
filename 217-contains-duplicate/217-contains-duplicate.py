from collections import defaultdict
class Solution:
    def defa(self):
        return 0
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic=defaultdict(self.defa)
        for i in nums:
            dic[i]+=1
        for i in dic:
            if dic[i]>1:
                return True
        return False    
        