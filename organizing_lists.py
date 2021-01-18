#list.sort() - Permanently sorts the list in chronological order
#list.sort(reverse=True) - Permanently sorts the list in reverse chronological order
#sorted(list) - Temporarily sorts the list in chronological order. Original list order has not effect
#sorted(list, reverse=True) - Temporarily sorts the list in reverse chronological order. Original list order has not effect
#list.reverse() - Reverses the list but doesn't sort

countries = ['india', 'america', 'poland', 'scotland', 'malaysia']
print("Here is the original list")
print(countries)

print("\nHere is the sorted list which doesn't affect the original list order")
print(sorted(countries))

print("\nThe Original list order still remains as the same after using sorted() method")
print(countries)

print("\nUsing sorted() method to print the list reversely sorted")
print(sorted(countries, reverse=True))

print("\nThe Original list order still remains as the same after using sorted() method")
print(countries)

print("\nReversing the list")
countries.reverse()
print(countries)
countries.reverse()
print(countries)

print("\nSorting the list in alphabetical order Permanently")
countries.sort()
print(countries)

print("\nPriting the reverse order of the list sorted alphabetically")
countries.sort(reverse=True)
print(countries)






