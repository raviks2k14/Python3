bicycles = ['trek', 'cannonable', 'redline', 'specialized']

print(bicycles)

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

print(bicycles[-1]) # By asking for the item at index -1, Python always returns the last item in the list
print(bicycles[-2]) # By asking for the item at index -2, Python always returns the 2nd item from the end of the list
print(bicycles[-3]) # By asking for the item at index -3, Python always returns the 3rd item from the end of the list
print(bicycles[-4]) # BBy asking for the item at index -4, Python always returns the 4th item from the end of the list

print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

#Changing, Adding, Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)