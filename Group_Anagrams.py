class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nums=strs[:]
        d={}
        for i in nums:
            l=sorted(i)
            l=str(l)
            try:
                d[l].append(i)
            except:
                d[l]=[i]
        f=[]
        for i in d:
            f.append(d[i])
        return (f)