class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        val=str(x)
        if val==val[::-1]:
            return True
        return False
        