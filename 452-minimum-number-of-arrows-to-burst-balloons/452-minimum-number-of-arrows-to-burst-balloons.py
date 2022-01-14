from operator import itemgetter

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        completed=[]
        bursted=set([])
        start=0
        end=start+1
        points = sorted(points, key=itemgetter(1))
        minV=points[0][0]
        maxV=points[0][1]
        
        while start<len(points):
            if end==len(points):
                if start not in completed:
                    bursted.add(start)
                completed.append(start)   
                start+=1
                end=start+1
            
                if start<len(points):
                    minV=points[start][0]
                    maxV=points[start][1]
            if end==len(points) or start==len(points):
                break
            
            if len(completed)==len(points):
                break
            
            st=points[start]
            en=points[end]
            if st[1]>=en[0] and st[1]<=en[1]:
                print(start,end)
                bursted.add(start)
                completed.append(end)
                if en[0]>minV:
                    minV=en[0]
                if en[1]<maxV:
                    maxV=en[1]
            else:
                completed.append(start)
                bursted.add(start)
                start=end
            end+=1     
        print(points,bursted,completed)
        return len(bursted)