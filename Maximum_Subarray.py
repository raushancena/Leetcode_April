def kadanes(A):
    table=[float('-inf')]*(len(A)+1)
    for i in range(1,len(A)+1):
        table[i]=max(A[i-1],(table[i-1]+A[i-1]))
    #print(table)
    return max(table)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=kadanes(nums)
        return ans