class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # pre=0
        # f=0
        # for i in s:
        #     if i not in t:
        #         return False
        #     if pre==0:
        #         pre=t.index(i)
        #     else:
        #         pre=t.index(i)+f
        #     f+= len(t[:t.index(i)])  +1
        #     if f<pre:
        #         return False
        #     t=t[t.index(i)+1:]
        # return True    
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return True if subsequence >= len(s) else False
        