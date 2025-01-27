list = [5,10,15,20]  #square brackets me hoti hai list
print("list[2]:=",list[2])  #list ki indexing 0 se start hoti hai means
                            #2 jo hai vo 3rd element hai list ka

#append()method
list.append(25)  # Adds a single element to the end of the list.
print("after append =",list)

#extend()method
list.extend([25,30,35])  #extend() adds each element of the iterable individually.
print("after extend =",list)

#count()method [how many times an element occurs in a list]
print("how many times element 5 occured =",list.count(25))

#index()method  [finds its position in the list]
print("index of 25 is =",list.index(25))

#insert()method #insert an elemnet to the given list at a given index
list.insert(8,40)
print(list)

#remove()method  #searches for the element in the list and removes
list.remove(40)  #the first matching element
print(list)

#pop()method #removes the item from the list at a given index
list.pop(4)
print(list)

#sort()method  #sort list in ascending order on numbers
list.sort()
print(list)

#reverse()method
list.reverse()
print(list)

#min()method
smallest = min(list)
print(smallest)

#max()method
largest = max(list)
print(largest)