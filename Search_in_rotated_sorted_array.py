#Function to finding minimum element in nums:-

def f(nums,left,right):
	print(nums)
	while(left<right):
		mid=left+(right-left)//2
		if(nums[mid]>nums[right]):
			left=mid+1
		else:
			right=mid
	return left

#Function to find target in nums:-

def bs(nums,left,right,target):
	while(left<=right):
		t,t1=left,right
		mid=left+(right-left)//2
		if(nums[mid]==target):
			return mid
		elif(nums[mid]<target):
			left=mid+1
		else:
			right=mid-1
	return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums)==0):
            return -1
        a=f(nums,0,len(nums)-1)
        if(target>=nums[a] and target<=nums[-1]):
            x=bs(nums,a,len(nums)-1,target)
        else:
            x=bs(nums,0,a,target)
            
        return x

        