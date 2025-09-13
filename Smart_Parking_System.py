#SMART PARKING SYSTEM

from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self,vehicle_id,license_plate,owner_name):
        self.__vehicle_id = vehicle_id
        self.__license_plate=license_plate
        self.__owner_name= owner_name

    def get_owner_name(self):
        return self.__owner_name
    
    def get_license_plate(self):
        return self.__license_plate
    
    def display(self):
        pass

    def cal_parking_fee(self,hrs):
        pass

        
class Bike(Vehicle):
    def __init__(self,vehicle_id,license_plate,owner_name,helmet_required):
        super().__init__(vehicle_id,license_plate,owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Owner:{self.get_owner_name()}\nLisense plate:{self.get_license_plate()}\nhelmet_requiered:{self.helmet_required}")
    
    def cal_parking_fee(self, hours):
        return 20 * hours
    
class Car(Vehicle):
    def __init__(self,vehicle_id,license_plate,owner_name,seats):
        super().__init__(vehicle_id,license_plate,owner_name)
        self.seats = seats
    
    def display(self):
        print(f"Owner:{self.get_owner_name()}\nLisense plate:{self.get_license_plate()}\nSeats:{self.seats}")
    
    def cal_parking_fee(self,hrs):
        fee=hrs*50
        return fee   

class SUV(Vehicle):
    def __init__(self,vehicle_id,license_plate,owner_name,four_wheel_drive):
        super().__init__(vehicle_id,license_plate,owner_name)
        self.four_wheel_drive= four_wheel_drive
    
    def display(self):
        print(f"Owner:{self.get_owner_name()}\nLisense plate:{self.get_license_plate()}\nFour_wheel_drive:{self.four_wheel_drive}")
    
    def cal_parking_fee(self,hrs):
        fee=hrs*70
        return fee
        
class Truck(Vehicle):
    def __init__(self,vehicle_id,license_plate,owner_name,max_load_capacity):
        super().__init__(vehicle_id,license_plate,owner_name)
        self.max_load_capacity= max_load_capacity
    
    def display(self):
        print(f"Owner:{self.get_owner_name()}\nLisense plate:{self.get_license_plate()}\nmax_load_capacity:{self.max_load_capacity}")  
    
    def cal_parking_fee(self,hrs):
        fee=hrs*100
        return fee



class ParkingSpot:
    SIZE_MAPPING = {
        "S": ["Bike"],
        "M": ["Bike", "Car"],
        "L": ["Bike", "Car", "SUV"],
        "XL": ["Bike", "Car", "SUV", "Truck"]
    }

    def __init__(self, spot_id, size):
        self.__spot_id = spot_id
        self.__size = size
        self.__vehicle = None  

    def get_spot_id(self):
        return self.__spot_id

    def get_size(self):
        return self.__size

    def get_vehicle(self):
        return self.__vehicle

    def is_empty(self):
        return self.__vehicle is None

    def assign_vehicle(self, vehicle):
        vehicle_type = type(vehicle).__name__
        if not self.is_empty():
            print(f"Spot {self.__spot_id} is already occupied.")
            return False
        if vehicle_type in self.SIZE_MAPPING[self.__size]:
            self.__vehicle = vehicle
            print(f"{vehicle_type} ({vehicle.get_license_plate()}) assigned to Spot {self.__spot_id} ({self.__size})")
            return True
        else:
            print(f"{vehicle_type} cannot fit into Spot {self.__spot_id} ({self.__size})")
            return False

    def remove_vehicle(self):
        if self.is_empty():
            print(f"Spot {self.__spot_id} is already empty.")
            return None
        vehicle = self.__vehicle
        self.__vehicle = None
        print(f"{type(vehicle).__name__} ({vehicle.get_license_plate()}) removed from Spot {self.__spot_id}")
        return vehicle

    def display(self):
        if self.is_empty():
            print(f"Spot {self.__spot_id} ({self.__size}): Empty")
        else:
            v = self.__vehicle
            print(f"Spot {self.__spot_id} ({self.__size}): Occupied → {type(v).__name__} ({v.get_license_plate()})")



class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)
        print(f"Added Spot {spot.get_spot_id()} of size {spot.get_size()}")

    def show_spots(self):
        print("Parking Status:")
        for spot in self.spots:
            spot.display()
        print()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_empty() and type(vehicle).__name__ in ParkingSpot.SIZE_MAPPING[spot.get_size()]:
                if spot.assign_vehicle(vehicle):
                    return
        print(f"No available spot for {type(vehicle).__name__} ({vehicle.get_license_plate()})")

    def unpark_vehicle(self, vehicle, hours, payment_method):
        for spot in self.spots:
            if not spot.is_empty() and spot.get_vehicle() == vehicle:
                removed_vehicle = spot.remove_vehicle()
                fee = removed_vehicle.cal_parking_fee(hours)
                print(f"Parking Fee = ₹{fee}")
                payment_method.pay(fee)
                return
        print(f"Vehicle {vehicle.get_license_plate()} not found in the parking lot.")


class Payment(ABC):
    @abstractmethod
    def pay(self, amt):
        pass

class CashPayment(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} in cash")

class CardPayment(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} using credit/debit card")

class UPIPayment(Payment):
    def pay(self, amt):
        print(f"Paid Rs.{amt} using UPI")



def main():
    print("---Step 1: Create Parking Lot and Spots---")
    lot = ParkingLot("CityMall Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "M"))
    lot.add_spot(ParkingSpot(4, "L"))
    lot.add_spot(ParkingSpot(5, "XL"))
    print(f"Parking Lot Created: {lot.name} | Total Spots Added: {len(lot.spots)}\n")

    print("---Step 2: Create Vehicles---")
    bike1 = Bike("B101", "TS01AB1234", "Rishi", True)
    car1 = Car("C201", "TS05CD5678", "Harika", 5)
    suv1 = SUV("S301", "TS09EF9012", "Rishika", True)
    truck1 = Truck("T401", "TS11XY4455", "Akhil", 12)

    print("Vehicles Created:")
    for vehicle in [bike1, car1, suv1, truck1]:
        vehicle.display()
    print()

    print("---Step 3: Park Vehicles---")
    lot.park_vehicle(bike1)
    lot.park_vehicle(car1)
    lot.park_vehicle(suv1)
    lot.park_vehicle(truck1)
    print()
    lot.show_spots()

    print("---Step 4: Unpark a Vehicle + Payment---")
    # Example: Unpark car1 for 3 hours
    hours = 3
    print(f"Unparking Car ({car1.get_license_plate()}) after {hours} hours")
    print("Select Payment Method: 1. Cash 2. Card 3. UPI")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        payment_method = CashPayment()
    elif choice == "2":
        payment_method = CardPayment()
    elif choice == "3":
        payment_method = UPIPayment()
    else:
        print("Invalid choice, defaulting to CashPayment.")
        payment_method = CashPayment()

    lot.unpark_vehicle(car1, hours, payment_method)
    print()

    print("---Step 5: Final Status---")
    lot.show_spots()


if __name__ == "__main__":
    main()
