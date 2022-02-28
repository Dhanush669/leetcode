# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    
    def level(self,root,dic,l,posi):
        if root==None:
            return
        # if root.left==None:
        #     if root.right==None:
        #         pass
        #     else:
        #         dic[l+1].append(0)
        # if root.right==None:
        #     if root.left==None:
        #         pass
        #     else:
        #         dic[l+1].append(0)
        dic[l].append(posi)        
        self.level(root.left,dic,l+1,posi*2)
        self.level(root.right,dic,l+1,(posi*2+1))
        return dic
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic=defaultdict(list)
        dic=self.level(root,dic,1,1)
        maxi=0
        for i in dic:
            t=(max(dic[i])-min(dic[i]))+1
            if t>maxi:
                maxi=t
        return maxi        
            
        
#         maxi=0
#         prev=0
#         queue=[(1,root)]
#         lis=[]
        
#         while queue:
#             posi,node=queue.pop()
#             if node.left!=None:
#                 queue.append((posi*2,node.left))
#             else:
                
                
#             if node.right!=None:
#                 queue.append(((posi*2)+1,node.right))
#             # if (posi-prev)>maxi:    
#             #     maxi=(posi-prev)
#             prev=posi
                  
#         return maxi        



#         dic=self.level(root,dic,0)
#         m=0
#         for i in dic:
#             print(i,dic[i])
#         # print(len(dic))    

#         for i in dic:
#             val=0
#             if i< (len(dic)-1):
#                 if dic[i][0]!=0 and dic[i][-1]!=0:
#                     val=2**i
#                     # if val!=len(dic[i]):
#                     #     val=len(dic[i])
#                     print(val,"v1")
#                 else:
#                     if dic[i][0]!=0 and dic[i][-1]==0:
#                         t=dic[i]
#                         t=t[::-1]
#                         #print(t,dic[i])
#                         cp=0
#                         for i in range(0,len(t)):
#                             if t[i]>0:
#                                 cp=i
#                                 break
#                         #print(cp)        
#                         if cp!=0:        
#                             tp=((len(t)-cp)+1)-1
#                             t=t[::-1]
#                             t=t[:tp]
                                
#                             val=len(t)
#                             print(val,"v2",t,tp)
#                     else:
#                         if dic[i][-1]!=0:
#                             xp=0
#                             for x in range(0,len(dic[i])):
#                                 if dic[i][x]>0:
#                                     xp=x
#                                     break
#                             tem=dic[i]        
#                             te=tem[xp:]
#                             val=len(te)
#                             print(val,"v3")
#                         else   :
#                             xp=0
#                             for x in range(0,len(dic[i])):
#                                 if dic[i][x]>0:
#                                     xp=x
#                                     break
#                             if xp!=0:        
#                                 tem=dic[i] 

#                                 t=dic[i]
#                                 t=t[::-1]
#                                 p=t.index(0)
#                                 cp=(len(t)-p)+1
#                                 t=t[xp:cp]
#                                 val=len(t)
#                                 print(val,"v4")
            
#                 if val>m:
#                     #print(i,dic[i],val,m)
#                     m=val
                    
#         return m

        