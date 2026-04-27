# Railway Reservation System

total_seats = 50
available_seats = 50
bookings = {}
booking_id_counter = 1


def check_availability():
    print("\nAvailable seats:", available_seats)


def book_ticket():
    global available_seats, booking_id_counter

    if available_seats == 0:
        print("\nNo seats available")
        return

    name = input("Enter name: ")
    age = input("Enter age: ")

    booking_id = booking_id_counter
    booking_id_counter += 1

    seat_number = total_seats - available_seats + 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    available_seats -= 1

    print("\nTicket booked successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_number)


def view_ticket():
    bid = int(input("\nEnter Booking ID: "))

    if bid in bookings:
        print("\nBooking Details:")
        print("Name:", bookings[bid]["name"])
        print("Age:", bookings[bid]["age"])
        print("Seat:", bookings[bid]["seat"])
    else:
        print("\nBooking not found")


def cancel_ticket():
    global available_seats

    bid = int(input("\nEnter Booking ID to cancel: "))

    if bid in bookings:
        del bookings[bid]
        available_seats += 1
        print("\nTicket cancelled successfully")
    else:
        print("\nInvalid Booking ID")


# Main Menu
while True:
    print("\n===== Railway Reservation System =====")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        print("\nThank you for using the system!")
        break
    else:
        print("\nInvalid choice. Please try again.")
