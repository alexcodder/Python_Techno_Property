import Operation
import Read


class Main:
    # Display welcome message
    print("--------------------------------------------------------------------")
    print("Welcome to TechnoPropertyNepal")
    print("--------------------------------------------------------------------")

    def main():
        # Main loop (interaction with user)
        while True:
            # loop to check users input and respond accordinglly

            while True:
                try:
                    # Choices for the user
                    print("1. Enter 1 to View the List")
                    print("2. Enter 2 to Rent or Return")
                    print("3. Enter 3 to Exit")
                    # exception checking on error value
                    user_choice = int(input("Enter our choice : "))

                    # conditions to repond on users input
                    if user_choice == 1:
                        Read.Read_Details.Display()  # Display available equipment
                    elif user_choice == 2:
                        Operation.RentReturnInterface.RentOrReturn()
                    elif user_choice == 3:
                        print("Plesaure doing Buisness!!")
                        break
                    else:
                        print(
                            "Input Error. Please enter only from following only(1,2 or 3)"
                        )

                except ValueError:
                    print(
                        "Input Error. Please enter only from following only(1,2 or 3)"
                    )
            break

    main()
