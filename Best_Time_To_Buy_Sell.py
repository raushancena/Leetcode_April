class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums=prices[:]
        l=[0]
        for i in range(1,len(nums)):
            a=nums[i]-nums[i-1]
            s=l[i-1]+a
            #print(l[i-1])
            z=max(l[i-1],a,s)
            l.append(z)
        return (l[-1])
        