class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        li=[]
        p=[]
        for i in trust:
            p.append(i[0])
            li.append(i[1])   
        for i in range(1,n+1):
            if li.count(i)==n-1 and i not in p:
                return i
        return -1    