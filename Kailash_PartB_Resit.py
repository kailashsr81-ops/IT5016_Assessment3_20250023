Ticket_ID = 20000                                # Global Ticket_ID initialized to 20000               

# Define the Booking_System class
class Booking_System():
    def __init__(self, name, id_number, status):        
        global Ticket_ID
        self.name = name                        # Passenger name
        self.id = id_number                     # ID number of the passenger
        self.status = status                    # Booking status
        self.total = 0                          # Total cost of ferry services
        self.total_submitted = 0                # Counter for how many bookings submitted
        self.approved = 0                       # Counter for approved bookings
        self.not_approved = 0                   # Counter for not approved bookings
        self.pending = 0                        # Counter for pending bookings
        self.approval_reference_number = 0      # Approval reference number
        self.Tic_ID = Ticket_ID + 1             # Assign a unique ticket ID by increasing the global one 

    # Method to print customer information
    def customer_info(self):
        print("Printing booking")
        print(f"Id number: {self.id}")
        print(f"Passenger name: {self.name}")
        print(f"Ticket ID: {Ticket_ID}")        
        print(f"Total: {self.total}")
        print(f"Status: {self.status}")
        print(f"Approval reference number: {self.approval_reference_number}")

    # Method for entering ferry service and price
    def ferry_service_details(self):
        while True:
            price = input("Which service you want (or type 'done' to finish): ")
            
            if price.lower() == "done":  
                break

            #Price for the service you want
            price_service = int(input(f"Enter the price of service $ {price}: ")) 
            self.total += price_service  # Add price to total
    
        print("Total price of all products is:", self.total)

    # Method for manager to approve/reject/pending the booking
    def booking_approval(self):
        decision = input("The manager's decision (approved / not approved / pending): ")

        # If booking is approved
        if decision == "approved":
            self.total_submitted += 1
            self.approved += 1
            self.last_three = str(self.Tic_ID)[-3]                       # Get the last 3rd digit from Ticket ID
            self.approval_reference_number = self.id + self.last_three  # Create a custom approval reference number

        # If booking is not approved
        elif decision == "not approved":
            self.total_submitted += 1
            self.not_approved += 1
            self.approval_reference_number = "Not available"

        # If booking is pending
        elif decision == "pending":
            self.total_submitted += 1
            self.pending += 1
            self.approval_reference_number = "Not available"

    # Display the details of the booking
    def display_booking_info(self):
        print("Information of booking system")
        print("Id number:", self.id)
        print("Passenger name:", self.name)
        print("Ticket id:", self.Tic_ID)
        print("Total:", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number)

    # Display booking statistics
    def print_static(self):
        print(f"The total no of bookings submitted: {self.total_submitted}")
        print(f"The approved bookings: {self.approved}")
        print(f"The no of not approved bookings: {self.not_approved}")
        print(f"The pending bookings are: {self.pending}")

# Create an object of Booking_System
customer1 = Booking_System("Kailash", "PAX123", "Approved")

# Get ferry service details (loop for user input)
customer1.ferry_service_details()

# Ask manager for approval decision
customer1.booking_approval()

# Display booking info
customer1.display_booking_info()

# Print booking statistics
customer1.print_static()
