import Read

_dict = Read.Read_Details.Display_Database()
Land_no = input("Enter the land number: ")
price = _dict[Land_no][4]
rent_Months = int(input("Enter month you rented for : "))
returned_month = int(input("Enter number of month return : "))
fine_amount = 0  # Initialize fine_amount
fine_rate = 0  # Initialize fine_rate

if rent_Months < returned_month:
    Months_late = returned_month  - rent_Months
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


