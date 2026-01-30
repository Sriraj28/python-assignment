print("hello world")

#crete a list:
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ["Sriraj",37,"Soc18"]
list3 = [2,5,1,3,6,9,8]

#Accessing list elements using index:
print(list1[4])
print(list2[-3])
print(list2[0])

#Slicing a list
print(list1[4:9])
print(list2[1:3])

#Adding elements to a list
list1.append(11)
list2.append("football")
print(list1,list2)
print(list2)

list1.insert(0,0)
list1.insert(4,1)
list2.insert(4,"basketball")
print(list1,list2)

#removing element in a list
list1.remove(1)
list2.remove("basketball")
print(list1,list2)

list1.pop()
list1.pop(3)
list1.pop(0)
list2.pop(3)
print(list1,list2)

del list1[0]
del list2[1]
print(list1,list2)

list2.clear()
print(list1,list2)

#Sorting List Elements
list3.sort()
print(list3)

list3.reverse()
print(list3)

# reversiing Using slicing technique
print(list1[::-1])





