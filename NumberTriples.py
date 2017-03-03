a=raw_input()
a=map(int,a.split())
d={}
d1={}
d2={}
p=[]
for i in range(0,a[0]):
	a1=raw_input()
	a1=map(int,a1.split())
	d[(a1[0],a1[2])]=a1[1] #edge dictionary
	d[(a1[2],a1[0])]=a1[1] #edge dictionary
	if a1[0] not in d1.keys():
		d1[a1[0]]=9999999 #Shortest path dictionary
		d2[a1[0]]=0	#Visited nodes dictionary
	if a1[2] not in d1.keys():
		d1[a1[2]]=9999999
		d2[a1[2]]=0
p=p+d.keys() #all edges 
q={}
d1[a[1]]=0
d2[a[1]]=1
for i in range(0,len(p)):
	if a[1]==p[i][0]:
		q[p[i]]=d[p[i]]
		d1[p[i][1]]=d[p[i]] 
while(len(q)>0):
	k=min(q,key=q.get)
	k1=q[k]
	for i in range(0,len(p)):
		if k[1]==p[i][0] and d1[p[i][1]]>d[(p[i][0],p[i][1])]+k1 and d2[p[i][1]]!=1:
			d1[p[i][1]]=d[(p[i][0],p[i][1])]+k1
			q[p[i]]=d1[p[i][1]]
	d2[k[1]]=1
	del q[k]
if(a[2] in d1.keys()):
	print "YES"
	print d1[a[2]]
else:
	print "NO"

			
