# Vehicle fleet management


class Vehicle:
    def __init__(self, registration_plate, model):
        self.registration_plate = registration_plate
        self.model = model
        self.available = True

    def __str__(self):
        return f'{self.registration_plate} - {self.model} - {"Available" if self.available else "Unavailable"}'


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, registration_plate):
        for vehicle in self.vehicles:
            if vehicle.registration_plate == registration_plate:
                vehicle.available = False
                print(
                    f"\n[+] Renting vehicle: {vehicle.registration_plate} - {vehicle.model}")
                return

    def __str__(self):
        return '\n'.join([f'{vehicle.registration_plate} - {vehicle.model} - {"Available" if vehicle.available else "Unavailable"}' for vehicle in self.vehicles])


if __name__ == '__main__':

    fleet = Fleet()

    fleet.add_vehicle(Vehicle('ABC123', 'Toyota'))
    fleet.add_vehicle(Vehicle('DEF456', 'Ford'))

    print("\n[+] Initial fleet:\n")
    print(fleet)

    fleet.rent_vehicle('ABC123')

    print("\n[+] Fleet after renting a vehicle:\n")
    print(fleet)
