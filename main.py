# list functions

# we have 2 lists
lucky_numbers = [8,15, 4, 16,23,42]
friends = ["Kevin", "Karen", "Mike", "Oscar", "Jim"]

#we can PRINT a list
print(friends)
#output = ['Kevin', 'Karen', 'Mike', 'Oscar', 'Jim']

#we can EXTEND  a list by attaching another list at the end of a list
friends.extend(lucky_numbers)
print(friends)
#output = ['Kevin', 'Karen', 'Mike', 'Oscar', 'Jim', 4, 8, 15, 16, 23, 42]

#we can APPEND an additional item to an existing list
friends.append("Tung")
print(friends)
#output = ['Kevin', 'Karen', 'Mike', 'Oscar', 'Jim', 'Tung']

#if you want to insert an elemnt in the middle of the list, u use the INSERT function
friends.insert(1,"Oscar")
print(friends)
#output = ['Kevin', 'Oscar', Karen', 'Mike', 'Oscar', 'Jim']

#we can remove an item from a list
friends.remove("Tung")
print(friends)
#output = ['Kevin', 'Karen', 'Mike', 'Oscar', 'Jim']

#we can also remove all elements from a list
friends.clear()
print(friends)

# the pop method removes the last element from a list
friends = ["Gray" , "Mike", "Jim", "Ian", "Henry"]
friends.pop()
print(friends)
#output = ['Gray', 'Mike', 'Jim', 'Ian']

#to find an element in a list
print(friends.index("Mike"))
#output = 1

#to find the number of times an element occurs in a list
friends = ["Gray" , "Mike", "Jim", "Ian", "Henry", "Jim", "Jim"]
print(friends.count("Jim"))
#output = 3

#to sort the list
friends.sort()
print(friends)
#OR
lucky_numbers.sort()
print(lucky_numbers)
# output = ['Gray', 'Henry', 'Ian', 'Jim', 'Jim', 'Jim', 'Mike']
# [4, 8, 15, 16, 23, 42]

#to reverse a list
friends.reverse()
print(friends)
#output = ['Mike', 'Jim', 'Jim', 'Jim', 'Ian', 'Henry', 'Gray']

#to copy a list
friends.reverse()
friends2 = friends.copy()
print(friends2)
#output = ['Gray', 'Henry', 'Ian', 'Jim', 'Jim', 'Jim', 'Mike']