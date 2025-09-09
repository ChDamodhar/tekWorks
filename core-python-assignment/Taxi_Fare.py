def calculate_fare(distance):
    base_fare = 50
    per_km_rate = 10
    return base_fare + (distance * per_km_rate)
trips = [5, 10, 3]
total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total_fare}")