def staff_info():                                                  #Create a Python function called staff_info which will ask the user to input staff's information
    infomation = input("Enter Printing Information :")               #this one says to print
    date = input("Enter date : ")                                       #this variable ask the user to put the date
    staff_id = input("Enter Staff ID: ")                                # this one for staff_id
    staff_name = input("Enter Staff Name: ")                            # it ask the user to input staff_name
    
    requisition_counter = 10000                                            #requisition_counter to create a unique id
    requisition_counter += 1                                                #this will add +1 everytime we create a unique id
    
    print(f"Printing Staff Information : {infomation}")                        #to print information
    print(f"Date: {date}")                                                        #print date
    print(f"Staff ID: {staff_id}")                                                #print staff_id
    print(f"Staff Name: {staff_name}")                                            #print staff_name
    print(f"Requisition ID: {requisition_counter}")                            #this one to print requisition id
    
            
    return date, staff_id, staff_name, requisition_counter                           #return variables so they can be imported in task 2
    
# staff_info()                                                                        #this is just a comment

    



