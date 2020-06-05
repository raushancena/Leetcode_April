def square(l):
	for i in range(len(l)):
		for j in range(len(l[0])):
			l[i][j]=int(l[i][j])
	col_length=len(l[0])+1
	row_length=len(l)
	dp_table=[[0]*col_length for i in range(row_length+1)]
	u=0
	ans=0
	for i in range(row_length):
		u=u+1
		v=1
		for j in range(col_length-1):
			if(l[i][j]==1):
				dp_table[u][v]=min(dp_table[u-1][v-1],dp_table[u-1][v],dp_table[u][v-1])+1
			ans=max(ans,dp_table[u][v])
			v=v+1

	return ans

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        a=0
        if(matrix!=[]):
            a=square(matrix)
        return a*a
        