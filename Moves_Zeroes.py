class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for i in nums:
            if(i!=0):
                l.append(i)
        s=len(nums)-len(l)
        for i in range(s):
            l.append(0)
        for i in range(len(l)):
            nums[i]=l[i]
       # nums[0]=l[0]
            
        