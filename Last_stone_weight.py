#function to search position:-

def f(l,a):
	left,right=0,len(l)-1
	while(left<right):
		mid=left+(right-left)//2
		if(l[mid]==a):
			return mid+1
		elif(l[mid]>a):
			left=mid+1
		elif(l[mid]<a):
			right=mid
	return left
#function to find stone:-

def stone(l):
	l.sort(reverse=True)
	#print(l)
	while(len(l)>1):
		a=l.pop(0)
		b=l.pop(0)
		a=abs(a-b)
		u=f(l,a)
		if(u==len(l)-1):
			if(a<l[-1]):
				l.append(a)
			else:
				l.insert(u,a)

		else:
			l.insert(u,a)
	return l[0]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=stone(stones)
        return a