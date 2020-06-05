class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        while(s!=n):
            a=n
            a=str(a)
            u=0
            s=n
            for i in a:
                u=u+(int(i)**2)
            n=u
            if(n==1):
                return True
        return False
            
                
            
            
            
        