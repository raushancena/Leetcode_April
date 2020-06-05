class Solution:
    def checkValidString(self, s: str) -> bool:
        l,m=[],[]
        for i in range(len(s)):
            if(s[i]=="("):
                l.append(i)
            elif(s[i]=="*"):
                m.append(i)
            else:
                if(l!=[]):
                    l.pop(-1)
                elif(m!=[]):
                    m.pop(-1)
                else:
                    return False
        if(len(l)<=len(m)):
            while(len(l)!=0):
                if(m[-1]>l[-1]):
                    l.pop(-1)
                    m.pop(-1)
                else:
                    return False
            return True
        return False
        