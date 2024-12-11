#Question 1
'''

l1 = list(input("Enter elements of the first list (separated by space): "))
l2 = list(input("Enter elements of the second list (separated by space): "))


cl = l1 + l2

maximum = max(cl)
indexmax = cl.index(maximum)

if indexmax < len(l1):
    list_num = 1
    index_in_list = indexmax
else:
    list_num = 2
    index_in_list = indexmax - len(l1)

print("Maximum element is ", indexmax)
print("Index in list", list_num, ":", index_in_list)


'''

#Question 2:
'''

n = int(input("Enter number of students"))
nl = []

for i in range(n):
    name = (input(f"Enter element : "))
    nl.append(name)
    
nlt = tuple(nl)
find = input("Enter name")

for i in nlt:

    if i == find:
        print("Name found")
        break
        
    else:
        print("No results found")
        
        
'''
#Question 3 
'''

n = int(input("Enter number of elements"))
l=[]

for i in range(n):
    ip = input("Enter element number " + str(i) + ': ')
    l.append(ip)
    
print(l)

r = input("Enter item to be removed")

for i in l:
    if i == r:
        l.remove(i)

print(l)

'''
# Question 4

'''



n = int(input("Enter number of students"))
sd = {}
for i in range(n):
    name = input("Enter Student name")
    rollno = int(input("Enter Student's Roll no "))
    marks = int(input("Enter student marks"))
    
    sd[name] = {'Roll number': rollno,"marks": marks}

for i in sd:
    if sd[i]['marks'] > 75:
        print(i,' has aquired more than 75')



'''

#Question 5

'''

l = eval(input("Enter list"))


print(l)

for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
        else:
            continue
        
print (l)


'''




        
