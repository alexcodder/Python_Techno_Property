import Read

_dict = Read.Read_Details.Display_Database()
class Update_Database:
    # Function to update stock after rental
    def update_stock(Land_no):
        _dict[Land_no][5] = " Not Available"

        # Write updated stock information back to the file
        stock_content = open("Details.txt", "w") 
        values = list(_dict.values())
       
        for i in range(len(values)):
            stock_content.write(",".join(values[i]))
            if i != len(values) - 1:
                stock_content.write("\n")
        stock_content.close()




    # Function to update stock after equipment return
    def update_return(return_Land):
        _dict[return_Land][5] = " Available"

        # Write updated stock information back to the file
        stock_content = open("Details.txt", "w")
        values = list(_dict.values())
        for i in range(len(values)):
            stock_content.write(",".join(values[i]))
            if i != len(values) - 1:
                stock_content.write("\n")
        stock_content.close()