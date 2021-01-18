person_name = "Greeshma"
print(person_name)

message = f"Hello {person_name}, Would you like to learn some python today?"
print(message)
print(person_name.upper())
print(person_name.lower())
print(person_name.title()) 

print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')

famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new"'
print(message)

person_name = '                  Ravikumar Shankarappa   '
print(f"\t{person_name}")
print(f"\n{person_name}")
print(f"{person_name.rstrip()}")
print(f"{person_name.lstrip()}")
print(f"{person_name.strip()}")

#Notes
#f - stands for format. To print any variable content inside a string, it should be written within {} brackets.
#strip() - Removes whitespaces from the String.
#lstrip() - Removes whitespaces from the left side of the string.
#rstrip() - Removes whitespaces from the right side of the string.