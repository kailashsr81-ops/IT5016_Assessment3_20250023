def staff_info():                                                  #Create a Python function called staff_info which will ask the user to input staff's information
    infomation = input("Enter Printing Information :")               #this one says to print
    date = input("Enter date : ")                                       #this variable ask the user to put the date
    staff_id = input("Enter Staff ID: ")                                # this one for staff_id
    staff_name = input("Enter Staff Name: ")
    
    requisition_counter = 10000
    requisition_counter += 1
    
    print(f"Printing Staff Information : {infomation}")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition ID: {requisition_counter}")
    
            
    return date, staff_id, staff_name, requisition_counter
    
# staff_info()

    


