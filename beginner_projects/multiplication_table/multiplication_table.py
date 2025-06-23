def table():
    while True:
        try:
            num = float(input("Input the number you want the table of: "))
            break
        except ValueError:
            print("\033[31mInvalid value\033[0m")
            print()

    print()


    while True:
        try:
            last = float(input(("Length of table (max 500): ")))
            if not last.is_integer():
                print("\033[31mValue must be a whole number\033[0m\n")
                continue
            last = int(last)
            if last > 500:
                print("\033[31mValue cannot be greater than 500\033[0m")
                print()
                continue
            if last < 0:
                print("\033[31mValue cannot be negative\033[0m")
                print()
                continue
            break
        except ValueError:
            print("\033[31mInvalid value\033[0m")
            print()

    for i in range(last + 1):
        print(f"{num} X {i} = \033[32m{num * i}\033[0m")


while True:
    table()
    restart = input("Do you want to run the program again?\ny/n: ").lower()
    if restart == "y":
        print()
        continue
    elif restart == "n":
        print("\n\033[35mThank you for using the program!\033[0m")
        break
    else:
        print("\033[33mInvalid input. Please type y or n.\033[0m\n")