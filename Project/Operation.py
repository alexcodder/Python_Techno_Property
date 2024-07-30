import Read
import Write

user = []  # List to store user details
user_ = []  # List to store return information

class Rent_Return():
    def rent():
        while True:# Land Number
            _dict = Read.Read_Details.Display_Database()
            try:
                # Land number from the user
                Land_no = input("Enter the Land Number: ")

                # Retrieve the dictionary from Display_Database() in Read.py

                # Validating the land number
                while Land_no not in _dict:
                    print("Enter a valid land number")
                    Land_no = input("Enter the land number: ")

                # Retrieve land information based on the input land number
                land_info = _dict[Land_no]
                availability = land_info[5].strip().lower()  # Get the availability status

                # Check if the land is available for rent
                if availability != "available":
                    print("Sorry, the land is not available for rent.")
                    continue  # Ask user for input again if land is not available
                
                break  # Break the loop if land is available

            except ValueError:
                print("Input land number")

        # Accessing the land details using the land number
        land = _dict[Land_no][1]
        _acers = _dict[Land_no][3]
        
        while True:
            try:
                # number of months the user wants to rent the land
                rent_months = int(input("Enter number of months you want to rent " + land + ": "))
                
                # Validate the number of months
                while rent_months < 1:
                    print("Invalid month")
                    rent_months = int(input("Enter number of months you want to rent " + land + ": ")) 
                
                break
            except ValueError:
                print("Invalid input. Please enter a valid months.")
                rent_months = int(input("Enter number of months you want to rent " + land + ": "))
        
        
        # Extract pricing information for the Land
        price = _dict[Land_no][4]
        item_price = price.replace('$', '')        
        
        # Calculate the total price for the rental
        total_price = int(item_price) * int(rent_months)
    
        # Update the stock information
        textfileupdate = Write.Update_Database.update_stock(Land_no)
        
        # Append rental information to the user list
        user.append([land, _acers, price, rent_months, total_price])
        
        # Calculate the grand total for all rentals
        grand_total = 0
        for i in user:
            grand_total = grand_total + int(i[4])

        print("the total price: $" +str(grand_total))
        # Return user and grand total
        return user, grand_total
    
    def Return():
        while True:
            _dict = Read.Read_Details.Display_Database()
            try:
                return_Land = input("Enter the Land Number: ")

                # Validating the land number
                while return_Land not in _dict:
                    print("Enter a valid land number")
                    return_Land = input("Enter the land number: ")
                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")


        Land = _dict[return_Land][1]  # Get the name of the returned Land

        while True:
            try:
                rented_Months = int(input("Enter month you rented " + Land + " for : "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                returned_Months = int(input("Enter number of month return: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        price = _dict[return_Land][4]

        fine_amount = 0  # Initialize fine_amount
        fine_rate = 0  # Initialize fine_rate

        Months_late = returned_Months  - rented_Months
        if Months_late == 0:
            fine_rate = 0 * float(price)
        elif Months_late < 5:
            fine_rate = 0.2 * float(price)  # fine is 20% of the price if the return is late by less than 5 Months
        elif Months_late > 5:
            fine_rate = 0.5 * float(price)  # fine is 50% of the price if the return is late by more than 5 Months
        elif Months_late > 12:
            fine_rate = 0.7 * float(price)  # fine is 70% of the price if the return is late by more than 12 Months
        else:
            fine_rate = 0.9 * price

        print("\nYou have exceeded the return time limit. Please pay the fine amount for " + str(Months_late) + " month \n")
        fine_amount = Months_late + fine_rate
        print("Your Fine amount is :" + str(fine_amount))

        item_return = Write.Update_Database.update_return(return_Land)  # Update stock information

        user_.append([Land, rented_Months, returned_Months, fine_amount])  # Store return information in user_info list

        for i in user_:
            fine_amount = fine_amount + int(i[3])  # Calculate total fine amount

        print("Total fine amount is: $" + str(fine_amount))
        return user_, fine_amount  # Return the updated user_info list and total fine amount

class RentReturnInterface():
    def UserDetails():
        print("PLEASE INPUT YOUR DETAILS FOR BILL CREATION" + "\n")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        address = input("Enter your address: ")
        print("Thank you for your patience, Your bill has been created")
        return name, phone, address
    
    def return_UserDetails():
        print("PLEASE INPUT YOUR DETAILS FOR BILL CREATION"+ "\n")
        return_name = input("Enter your name: ")
        return_phone = input("Enter your phone number: ")
        return_address = input("Enter your address: ")
        print("Thank you for your patience, Your bill is being printed")
        return return_name, return_phone, return_address
    
    def RentOrReturn():
        print("1. Enter 1 to Rent")
        print("2. Enter 2 to Return")
        Rent_or_Return = int(input("Enter your choice : "))
        if Rent_or_Return == 1:
            loop_ = True
            while loop_:
                Read.Read_Details.Display()  # Display available Land
                Rent_Return.rent()  # Initiate the rental process
                continue_ = input("Do you want to rent more Land (Y/N)? ")
                while True:
                    if continue_.upper() != "N" and continue_.upper() != "Y":
                        print("\n")
                        print("Invalid Input!")
                        print("\n")
                        continue_ = input("Do you want to rent more Land (Y/N)? ")
                    else:
                        break
                if continue_.upper() == "N":
                    loop_ = False  # Exit the loop if user doesn't want to rent more
                elif continue_.upper() == "Y":
                    loop_ = True  # Continue renting more Land
                elif Rent_or_Return == 2:
                    print("You choose to open Return window")
            name, phone, address = RentReturnInterface.UserDetails()  # Gather customer details
            # billprinting.bill(name, phone, address, user, grand_total)  # Generate bill

        elif Rent_or_Return == 2:
            loop_ = True
            while loop_:
                Read.Read_Details.Display()  # Display available Land
                Rent_Return.Return()  # Initiate the rental process
                continue_ = input("Do you want to rent more Land (Y/N)? ")
                while True:
                    if continue_.upper() != "N" and continue_.upper() != "Y":
                        print("\n")
                        print("Invalid Input!")
                        print("\n")
                        continue_ = input("Do you want to rent more Land (Y/N)? ")
                    else:
                        break
                if continue_.upper() == "N":
                    loop_ = False  # Exit the loop if user doesn't want to rent more
                elif continue_.upper() == "Y":
                    loop_ = True  # Continue renting more Land
                elif Rent_or_Return == 2:
                    print("You choose to open Return window")
            return_name, return_phone, return_address = RentReturnInterface.return_UserDetails()  # Gather customer details
            # billprinting.return_bill(return_name, return_phone, user_, fine_amount, return_address)  # Generate return bill
            
        else:
            print("Input Error. Please enter only from following only(1 or 2)")
            RentReturnInterface.RentOrReturn()


