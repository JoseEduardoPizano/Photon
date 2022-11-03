def common_elements(l1,l2):
	l3=[]
	n = 0
	for list in l1:
		for list2 in l2:
			if list == list2:
				l3.insert(n,list2)
				n = n+1
	return l3

l1 = [1,2,3,4,5]
l2=[1,5,6]
l3 = common_elements(l1,l2)
print(l3)
