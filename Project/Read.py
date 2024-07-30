class Read_Details:
    def Display_Database():
        LandDetails_Database = open("Details.txt", "r")
        LandDetails_display = LandDetails_Database.read()
        
        LandDetails_split = LandDetails_display.split("\n")

        d = {} # empty dictionary

        # Looping through the data lines
        for line in LandDetails_split:
            # Splitting and storing each values in the dictionary
            land_info = line.strip().split(",")
            land_number = land_info[0]  #land number From first element of database
            d[land_number] = land_info

        LandDetails_Database.close()
        return d
    
    
    def Display():
        # Open file in read mode to access information
        LandDetails = open("Details.txt", "r")
        
        # Check file data and file import status
        if LandDetails:
            print("--------------------------------------------------------------------------------------------------------")
            print("Land No  \t Location\t\t Direction  \tSize \t\t Price \t      Availability")
            print("--------------------------------------------------------------------------------------------------------")
            
            # Iterate through each line in the file
            for line in LandDetails:
                # Format and print equipment details along with the serial number
                print(line.replace(",", "\t\t"))
                
            print("--------------------------------------------------------------------------------------------------------")
        else:
            print("Database not found. Please check with owner and try again.")
        
        # Close the file to release system resources
        LandDetails.close()
