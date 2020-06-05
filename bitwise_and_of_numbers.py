def f(m,n):
	a=bin(m).replace("0b","")
	b=bin(n).replace("0b","")
	a1,b1=len(a),len(b)
	if(a1>b1):
		l,m,u=["0"]*a1,["0"]*a1,["0"]*a1
		for i in range(a1):
			l[i]=a[i]
		for i in range(a1-b1,b1):
			m[i]=b[i]
	else:
		l,m,u=["0"]*b1,["0"]*b1,["0"]*b1
		for i in range(b1-a1,a1):
			l[i]=a[i]
		for i in range(b1):
			m[i]=b[i]
	a=-1
	for i in range(len(l)):
		if(l[i]==m[i]):
			a=i
		else:
			break
	for i in range(a+1):
		u[i]=l[i]
	c=""
	for i in u:
		c=c+i

	return (int(c,2))
	
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a=f(m,n)
        return a
        