from task1 import staff_info

def requisitions_total():
    date, staff_id, staff_name, requisition_counter = staff_info()
    sum = 0
    while True:
        item_needed = input("Enter the name of the product (or type 'done' to finish): ") 
        
        if item_needed.lower() == "done":  
            break
        
        price_item = int(input(f"Enter the price of {item_needed}: $")) 
        sum += price_item   
    
    print("Total price of all products is:", sum)
    return  date, staff_id, staff_name, requisition_counter, sum, item_needed, price_item
    
# requisitions_total()







