class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i=0
        # j=0
        # k=0
        # lis=nums1[:m]
        # while i<m and j<n:
        #     if lis[i]<=nums2[j]:
        #         nums1[k]=lis[i]
        #         i+=1
        #         k+=1
        #     else:
        #         nums1[k]=nums2[j]
        #         j+=1
        #         k+=1
        # print(i,j,m,n,nums1)        
        # if j<n:
        #     x=0
        #     for i1 in range(j,n):
        #         nums1[k]=nums2[i1]
        #         k+=1
        # if i<m:
        #     x=0
        #     for i1 in range(i,m):
        #         nums1[k]=lis[i1]
        #         k+=1        
        i=m-1
        j=n-1
        k=i+j+1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
        print(nums1)        
        if j>=0:
            for x in range(j,-1,-1):
                nums1[x]=nums2[x]
        #if i>0:
            
          
        