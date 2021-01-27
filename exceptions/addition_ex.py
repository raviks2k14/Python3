def add_two_numbers(no_1, no_2):
    while True:
        no_1 = input("Enter number 1 , (y/n)")
        no_2 = input("Enter number 2, (y/n)")
        try:
            if no_1 != 'q':
                no_1 = int(no_1)
                no_2 = int(no_2)
                total = no_1 + no_2
            else:
                break
        except ValueError:
            print("There was problem with the user input")
            pass
        else:
            print(total)


add_two_numbers(1, 2)
