from task2 import requisitions_total

def requisition_approval():
    date, staff_id, staff_name, requisition_counter, sum, item_needed, price_item  = requisitions_total()
    status = "pending"
    approval_ref = "None"

    if sum < 500:
        status = "Approved"
        last_three = str(requisition_counter)[-3:]
        approval_ref = staff_id + last_three
    else:
        status = "Pending"
        approval_ref = "None"
        print("Total :", sum)
        print("Status :", status)
    if approval_ref == "None":
        print("Approval refernece number :", approval_ref)
    return date, staff_id, staff_name, requisition_counter, sum, item_needed, price_item, status, approval_ref
# requisition_approval()    








