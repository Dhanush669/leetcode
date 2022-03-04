class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # lis=[]
        siz=len(nums)
        res=0
        if len(nums)<3:
            return 0
        a1=nums[0]
        inc=1
        po=2
        d=nums[1]-a1
        for i in range(2,len(nums)):
            
#             if nums[i]-nums[i-1] == nums[i+1] - nums[i]:
#                 inc+=1
#                 res+=inc
                
#             else:
#                 inc=0
                
            
            n_1=po
            
            po+=1
            an=a1+(n_1*d)
            print(n_1,"m-1",an,nums[i],res)
            if an==nums[i]:
                res+=inc
                inc+=1
            else:
                s=len(nums[i:])
                #print(nums[i],len(nums[i:]),nums[i:])
                if s<2:
                    
                    break
                if s==2:
                    a1=nums[i-1]
                    d=nums[i]-nums[i-1]
                    inc=1
                    po=2
                    print(a1,d)
                else:    
                    
                    a1=nums[i]
                    d=nums[i+2]-nums[i+1]    
                    inc=0
                    po=1
                    #print(a1,d,po)
                
        # for i in range(0,len(nums)-2)    :
        #     for j in range(len(nums),2,-1):
        #         if len(nums[i:j])>=3:
        #             #lis.append(nums[i:j])
        #             t=nums[i:j]
        #             d=t[1]-t[0]
        #             a1=t[0]
        #             n_1=len(t)-1
        #             an=a1+(n_1*d)
        #             if an==t[-1]:
        #                 res+=1
                    
        # res=0
        # for i in lis:
        #     d=i[1]-i[0]
        #     a1=i[0]
        #     n_1=len(i)-1
        #     an=a1+(n_1*d)
        #     if an==i[-1]:
        #         res+=1       
        return res
        