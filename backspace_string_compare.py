class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s,t=S,T
        l,m=[],[]
        for i in s:
            l.append(i)
        for i in t:
            m.append(i)
        i=0
        while(i<len(l)):
            if(l[i]=="#"):
                if(i!=0):
                    l.pop(i)
                    l.pop(i-1)
                    i=i-1
                else:
                    l.pop(i)
            else:
                i=i+1
        i=0
        while(i<len(m)):
            if(m[i]=="#"):
                if(i!=0):
                    m.pop(i)
                    m.pop(i-1)
                    i=i-1
                else:
                    m.pop(i)
            else:
                i=i+1
        if(len(l)==len(m)):
            f1=0
            for i in range(len(l)):
                if(l[i]!=m[i]):
                    f1=1
            if(f1==0):
                #print("q")
                return "true"
        