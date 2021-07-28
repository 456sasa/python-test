# squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
# print (list(squared))


# l = [1,2,3,4,5]
# new_list=filter(lambda x:  x%2==0,l)
# print(list(new_list))


d = {'mike': 10, 'lucy': 2, 'ben': 30}
new_list = sorted(d.items(),key = lambda x:x[1],reverse= True)
print(new_list)