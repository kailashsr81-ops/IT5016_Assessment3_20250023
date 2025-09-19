Ticket_ID = 20000          

class Booking_System():
    def __init__(self, name, id_number, status):
        global Ticket_ID
        # self.Ticket_ID += 1 
        self.name = name
        self.id = id_number
        self.status = status
        self.total = 0
        self.total_submitted = 0
        self.approved = 0
        self.not_approved = 0
        self.pending = 0
        self.approval_reference_number = 0
        self.Tic_ID = Ticket_ID + 1

    def customer_info(self):
        print("Printing booking")
        print(f"Id number: {self.id}")
        print(f" Passanger name: {self.name}")
        print(f"ticket ID: {Ticket_ID}")
        print(f"Total: {self.total}")
        print(f"Status: {self.status}")
        print(f"Approval reference number :{self.approval_reference_number}")
        

    def ferry_service_details(self):
        while True:
            price = input("Which service you want(or type 'done' to finish): ")
            
            if price.lower() == "done":  
                break
            
            price_service = int(input(f"Enter the price of service $ {price}: ")) 
            self.total += price_service  
    
        print("Total price of all products is:", self.total)

    def booking_approval(self):
        decision = input("The manager's decision (approved / not approved/ pending): ")
        if decision == "approved":
            self.total_submitted += 1
            self.approved += 1
            self.last_three = str(self.Tic_ID)[-3]
            self.approval_reference_number = self.id + self.last_three
        elif decision == "not approved":
            self.total_submitted += 1
            self.not_approved += 1
            self.approval_reference_number = "Not available"
        elif decision == "pending":
            self.total_submitted += 1
            self.pending += 1
            self.approval_reference_number = "Not available"

    def display_booking_info(self):
        print("Information of booking system")
        print("Id number:", self.id)
        print("Passanger name:", self.name)
        print("Ticket id:", self.Tic_ID)
        print("Total:", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number)

    def print_static(self):
        print(f"The total no of bookings submitted: {self.total_submitted}")
        print(f"The approved bookings: {self.approved}")
        print(f"The no of not approved bookings:, {self.not_approved}")
        print(f"The pending bookings are: {self.pending}")

customer1 = Booking_System("Kailash", "PAX123", "Approved")

#customer1.customer1()
customer1.ferry_service_details()
customer1.booking_approval()
customer1.display_booking_info()
customer1.print_static()

        

