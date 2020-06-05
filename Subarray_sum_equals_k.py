def SubsetSum(l,k):
	d,s,ans={},0,0
	for i in range(len(l)):
		s=s+l[i]
		try:
			ans=ans+d[s-k]
		except:
			pass
		if(s==k):
			ans=ans+1
		try:
			d[s]=d[s]+1
		except:
			d[s]=1
	return ans

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a=SubsetSum(nums,k)
        return a
        