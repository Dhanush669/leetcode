from operator import itemgetter
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cou=0
        intervals=sorted(intervals, key=itemgetter(1))
        cur=intervals[0][1]
        for i in range(1,len(intervals)):
            if cur>intervals[i][0] and cur<=intervals[i][1]:
                cou+=1
            else:
                cur=intervals[i][1]
        return cou        
  

                    
        
        