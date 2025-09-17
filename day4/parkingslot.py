import time
from vehicle import Bike, Car, SUV, Truck

class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__is_occupied = False
        self.__vehicle = None
        self.__start_time = None

    def is_available(self):
        return not self.__is_occupied

    def assign_vehicle(self, vehicle):
        if self.is_available() and self._fits(vehicle):
            self.__vehicle = vehicle
            self.__is_occupied = True
            self.__start_time = time.time()
            print(f"Vehicle {vehicle.get_license_plate()} parked at Spot {self.spot_id}")
            return True
        return False

    def remove_vehicle(self):
        if self.__is_occupied:
            end_time = time.time()
            hours = max(1, int((end_time - self.__start_time) // 3600) + 1)
            fee = self.__vehicle.cal_parking(hours)
            vehicle = self.__vehicle
            self.__vehicle = None
            self.__is_occupied = False
            self.__start_time = None
            return vehicle, fee
        return None, 0

    def _fits(self, vehicle):
        if isinstance(vehicle, Bike) and self.size in ["S", "M", "L", "XL"]:
            return True
        if isinstance(vehicle, Car) and self.size in ["M", "L", "XL"]:
            return True
        if isinstance(vehicle, SUV) and self.size in ["L", "XL"]:
            return True
        if isinstance(vehicle, Truck) and self.size == "XL":
            return True
        return False

    def __str__(self):
        status = "Occupied" if self.__is_occupied else "Available"
        return f"Spot {self.spot_id} ({self.size}) - {status}"

class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            print(spot)

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return True
        print(f"No suitable spot available for {vehicle.get_license_plate()}")
        return False

    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            v, fee = spot.remove_vehicle()
            if v and v.get_license_plate() == vehicle.get_license_plate():
                print(f"Vehicle {v.get_license_plate()} unparked. Fee: ₹{fee}")
                return fee
        print(f"Vehicle {vehicle.get_license_plate()} not found.")
        return 0
