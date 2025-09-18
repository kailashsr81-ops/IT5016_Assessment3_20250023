from task3 import requisition_approval


def display_requisitons():
    date, staff_id, staff_name, requisition_counter, sum, item_needed, price_item, status, approval_ref = requisition_approval()
    print("Printing Requisitions:\n")
    print("Date:", date)
    print("Requisition ID:", requisition_counter)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $", sum)
    print("Status:", status)
    print("Approval Reference Number:", approval_ref)
    return item_needed, price_item




display_requisitons()



    

    
