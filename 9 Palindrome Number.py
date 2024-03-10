class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=x
        if(x<0):
            return False
        else:
            c=0
            res=0
            while(x>0):
                n=x%10
                x=x//10
                if(c>=1):
                    res=res*10 + n
                else:
                    res = n
                c=c+1
            if(res==x1):
                return True
            else:
                return False