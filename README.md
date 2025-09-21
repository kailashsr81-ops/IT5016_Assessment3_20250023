# IT5016_Assessment3_20250023
Summary

It is a tiny Python application created as a reservation system. Despite the fact that it is not a highly advanced project, it illustrates the implementation of the class and object functions of Python. The program works in the same manner as the booking service of a ferry which permits the clients to provide their personalities, the services to choose and the books to be approved or rejected by the manager.

The main objectives of this code are to do the object-oriented program and to understand the fundamental principles of software programming, such as DRY (Don't repeat yourself) and KISS (Keep it simple stupid). It has been composed in a simple form where the simplest person can understand how the application works.

Qualities
Customer information
The system can store the name of the passenger, ticket ID, and ID number. It also can display the details by printing them.

Ferry service
The user has the ability of keying in the service he or she wants to buy and the cost of the same. The application will sum up all the prices until the user enters the word done. The total is then printed.

The approval manager can make decisions like approved, not approved, and pending. An approval reference number will also be generated in the system once it is accepted.

Data
The system can count the number of total bookings, authorized, unapproved, and pending bookings as well.
How it operates

The Booking_System class is used in the code. The functions (also referred to as methods) within the class are many. Each method must be useful in some matter.

The initiator of the constructor, (the booker), prepares everything to start with zero and starts the booking with the details of the passenger.

customer information: show the information of the traveler and the reservation.

ferry_service_details: takes in requests and price of services by the user and add on till completion.

Booking approval: update counter and consult the manager.

display_booking_info: well wrapped printed booking information.

print_static: print out the total, authorized, pending and not approved statistics.

The program is run using these methods after a single object customer has been created at the end of the file.
Principles applied

KISS: The program follows KISS because it is very simple and has limited complexities. All of the methods are short and accomplish one task. This enables understanding.

DRY: If the same logic is not repetition, it also has some resemblance to DRY. An example is that approvals are only registered in one method and not in other methods.

In conclusion

This reservation system is just an experimental project. These can be improved in many ways including proper error handling, file storage, and the use of global variables should be avoided. Nevertheless, it also shows how to adhere to the KISS and DRY principles of a project and use class in the beginner style and utilize methods and objects.
