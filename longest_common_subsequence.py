def f(a,b):
	dp_table=[[0]*(len(a)+1) for i in range(len(b)+1)]
	u=0
	for i in range(len(b)):
		u=u+1
		v=1
		for j in range(len(a)):
			if(b[i]==a[j]):
				dp_table[u][v]=dp_table[u-1][v-1]+1
			else:
				dp_table[u][v]=max(dp_table[u-1][v],dp_table[u][v-1])
			v=v+1
	return dp_table[-1][-1]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a=f(text1,text2)
        return a
        