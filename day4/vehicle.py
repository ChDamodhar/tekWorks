class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate
        self.__owner_name = owner_name

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print(f"License Plate: {self.__license_plate}, Owner: {self.__owner_name}")

    def cal_parking(self, hours):
        return 0

class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet=True):
        super().__init__(license_plate, owner_name)
        self.helmet = helmet

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet: {self.helmet}")

    def cal_parking(self, hours):
        return 20 * hours

class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def cal_parking(self, hours):
        return 50 * hours

class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel = four_wheel

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Four-Wheel: {self.four_wheel}")

    def cal_parking(self, hours):
        return 70 * hours

class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, load_cap=10000):
        super().__init__(license_plate, owner_name)
        self.load_cap = load_cap

    def display(self):
        print(f"License Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Load Cap: {self.load_cap}")

    def cal_parking(self, hours):
        return 100 * hours
