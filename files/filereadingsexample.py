# with open('learning_python.txt') as file_object:
#     contents = file_object.read()
#
# print(contents)

# with open('learning_python.txt') as file_object:
#     for line in file_object:
#         print(line)

# with open('learning_python.txt') as file_object:
#     line_contents = file_object.readlines()
#
# for line_content in line_contents:
#     print(line_content.strip().replace('Python', 'C'))

# filename = 'guest.txt'
#
# with open(filename, 'w') as file_object:
#     guest_name = input("Please enter your name")
#     file_object.write(guest_name)

# filename = 'guest_book.txt'
#
# with open(filename, 'a') as file_object:
#     while True:
#         guest_name = input("Please enter your name (y/n)")
#         if guest_name != 'n':
#             print(f"Welcome {guest_name}")
#             file_object.write(f"{guest_name}\n")
#         else:
#             break

filename = 'polling.txt'

with open(filename, 'a') as file_object:
    while True:
        polling = input("Why do you like programming? (y/n)")
        if polling != 'n':
            print(f"Polling reason : {polling}")
            file_object.write(f"{polling}\n")
        else:
            break











