def staff_info():
    infomation = input("Enter Printing Information :")
    date = input("Enter date : ")
    staff_id = input("Enter Staff ID: ")
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

    

