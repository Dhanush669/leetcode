class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured<=1 and query_row!=0 and query_glass!=0:
            return 0.00000
        if poured<=1 and query_row==0 and query_glass==0:
            if poured==1:
                return 1.00000
            return 0.00000
        lis=[[0]*i for i in range(1,query_row+5)]
        lis[0][0]=poured
        for i in range(query_row+1):
            for j in range(i+1):
                q=(lis[i][j]-1)/2
                if q>0:
                    t=lis[i+1][j]
                    t1=lis[i+1][j+1]
                    lis[i+1][j]=t+q
                    lis[i+1][j+1]=t1+q
                    
        print(lis)    
        if lis[query_row][query_glass]>1:
            return 1.00000
        return lis[query_row][query_glass]
        


        