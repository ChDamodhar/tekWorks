def book_seat(total_seats, booked_seats, seat):
    if seat < 1 or seat > total_seats:
        print("Invalid seat number.")
    elif seat in booked_seats:
        print(f"Seat {seat} already booked.")
    else:
        booked_seats.append(seat)
    return booked_seats

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        print(f"Seat {seat} not booked.")
    return booked_seats

total_seats = 10
booked_seats = [2, 5, 7]
booked_seats = book_seat(total_seats, booked_seats, 3)
booked_seats = cancel_seat(booked_seats, 5)
available_seats = [s for s in range(1, total_seats+1) if s not in booked_seats]

print("Available seats:", available_seats)
