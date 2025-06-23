def grading_system():
    while True:
        try:
            total_marks = float(input("Enter total marks: "))
            if total_marks <= 0:
                print("\033[31mTotal marks cannot be zero or negative\033[0m")
                print()
                continue
            break

        except ValueError:
            print("\033[31mInvalid value\033[0m")
            print()
    while True:
        try:
            print()
            obtained_marks = float(input("Enter obtained marks: "))
            if obtained_marks > total_marks or obtained_marks < 0:
                print("\033[31mObtained marks cannot be higher than total marks or negative\033[0m")
                print()
                continue

            percentage = obtained_marks / total_marks * 100
            print()
            print(f"\033[36mYour percentage is {round(percentage, 2)}%\033[0m")
            if 100 >= percentage >= 95:
                print("Your grade is A++")
                print("\033[32mYou have passed the exam!\033[0m")


            elif 95 > percentage >= 90:
                print("Your grade is A+")
                print("\033[32mYou have passed the exam!\033[0m")


            elif 90 > percentage >= 85:
                print("Your grade is A")
                print("\033[32mYou have passed the exam!\033[0m")


            elif 85 > percentage >= 80:
                print("Your grade is B++")
                print("\033[32mYou have passed the exam!\033[0m")


            elif 80 > percentage >= 75:
                print("Your grade is B+")
                print("\033[32mYou have passed the exam!\033[0m")


            elif 75 > percentage >= 70:
                print("Your grade is B")
                print("\033[32mYou have passed the exam!\033[0m")

            elif 70 > percentage >= 60:
                print("Your grade is C")
                print("\033[32mYou have passed the exam!\033[0m")

            elif 60 > percentage >= 50:
                print("Your grade is D")
                print("\033[32mYou have passed the exam!\033[0m")

            elif 50 > percentage >= 40:
                print("Your grade is E")
                print("\033[32mYou have passed the exam!\033[0m")

            else:
                print("Your grade is F")
                print("\033[31mYou have failed the exam!\033[0m")
            print()
            break
        except ValueError:
            print("\033[31mInvalid value\033[0m")
            print()

while True:
    grading_system()
    while True:
        restart = input("Do you want to restart the program?\ny/n: ").lower()
        if restart == "y":
            print("\n")
            break
        elif restart == "n":
            print("\n\033[35mThank you for using the program!\033[0m")
            exit()
        else:
            print("\033[33mInvalid input. Please type y or n.\033[0m\n")

