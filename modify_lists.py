#del list[index] - Removes the element at the index permanently
#list.pop() - Gets the top most element from the list. Removes the element permanently. 
#This method can be used if we need the element for any other operation
#list.insert(index, 'element') - Inserts a element at the particular index. 
#The previous element which was at that index and the subsequent elements to its right will be moved to the right
#len() - gives the number of elements in the list
guest_list = ['tom', 'arun', 'nag']

print(f"I'm inviting {len(guest_list)} members to the dinner party")

print(f"\nHello {guest_list[0].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[1].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[2].title()}, You are invited to the dinner today")

print(f"\nSorry to say this, {guest_list[1].title()} can't make it to the dinner today")

del guest_list[1] #Delete the item from the list permanently
print(guest_list)

guest_list.insert(1, 'anuj') #Insert an item into the list at a particular index
print(guest_list)

print(f"\nHello {guest_list[0].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[1].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[2].title()}, You are invited to the dinner today")

print("\nHello Prati, Greeshu, Pavan, I have found a bigger dinner table. U guys hurry up for the dinner.")

guest_list.insert(0, 'prati')
guest_list.insert(2, 'greeshu')
guest_list.append('pavan') #Inserts an item to the end of the list

print(f"\nHello {guest_list[0].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[2].title()}, You are invited to the dinner today")
print(f"Hello {guest_list[-1].title()}, You are invited to the dinner today")

print(guest_list)

print("\nYuck!!!, We don't have the place for all the people for the dinner. Only two can occupy it. So, I can invite only two people for the dinner now.")

people_to_remove = guest_list.pop()
print(f"\nHello {people_to_remove}, You are removed from the dinner invite list")
people_to_remove = guest_list.pop()
print(f"Hello {people_to_remove}, You are removed from the dinner invite list")
people_to_remove = guest_list.pop()
print(f"Hello {people_to_remove}, You are removed from the dinner invite list")
people_to_remove = guest_list.pop()
print(f"Hello {people_to_remove}, You are removed from the dinner invite list")

print(f"\nHey {guest_list[0].title()}, You are still invited to the dinner party")
print(f"Hey {guest_list[1].title()}, You are still invited to the dinner party")

del guest_list[1]
del guest_list[0]
print(guest_list)
