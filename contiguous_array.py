def f(l):
	s,ans=0,0
	hash_table={0:-1}
	for j,i in enumerate(l):
		if(i==1):
			s=s+1
		else:
			s=s-1
		#print(s)
		try:
			ans=max(ans,j-hash_table[s])
		except:
			hash_table[s]=j
	return ans

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        a=f(nums)
        return a
        