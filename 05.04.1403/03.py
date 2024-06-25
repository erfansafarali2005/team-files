import time
from datetime import date


class CarShop:
    name = 'safaralimobile'
    location = 'azar washeignot'
    cars_list = {}
    motor_list = {}
    boat_list = {}
    clients_list = {}

    @staticmethod
    def about_us():
        print('its our informations ...')
        time.sleep(1)
        print(f"its {CarShop.name} carshop in {CarShop.location} with {len(CarShop.cars_list)} number of cars")


class Vehicle:

    def __init__(self, v_name, v_created_date, v_age, v_color, v_cylinder_count, v_price):
        self.vehicle_name = v_name
        self.vehicle_created_date = v_created_date
        self.vehicle_color = v_color
        self.vehicle_cylinder_count = v_cylinder_count
        self.vehicle_age = v_age
        self.vehicle_rented = False
        self.vehicle_price = v_price

    @classmethod
    def init(cls, i_name, i_created_date, i_color, i_cylinder_count, i_price):
        i_age = date.today().year - i_created_date
        return cls(i_name, i_created_date, i_age, i_color, i_cylinder_count, i_price)

    def is_rented(self):
        return self.vehicle_rented

    def vehicle_info(self):
        if self.vehicle_name in CarShop.boat_list:
            print(CarShop.boat_list[self.vehicle_name])
        elif self.vehicle_name in CarShop.cars_list:
            print(CarShop.cars_list[self.vehicle_name])
        elif self.vehicle_name in CarShop.motor_list:
            print(CarShop.motor_list[self.vehicle_name])
        else:
            print("the requested vehicle is not in the shop ...")


class MotorCycle(Vehicle):

    def __init__(self, im_name, im_created_date, im_color, im_cylinder_count, im_price):
        print("registering your motorcycle")
        time.sleep(2)
        vehicle = Vehicle.init(im_name, im_created_date, im_color, im_cylinder_count, im_price)
        self.vehicle_name = vehicle.vehicle_name
        self.vehicle_created_date = vehicle.vehicle_created_date
        self.vehicle_color = vehicle.vehicle_color
        self.vehicle_cylinder_count = vehicle.vehicle_cylinder_count
        self.vehicle_age = vehicle.vehicle_age
        self.vehicle_rented = vehicle.vehicle_rented
        self.vehicle_price = vehicle.vehicle_price
        CarShop.motor_list.update({
            im_name: {
                'creation_date': im_created_date,
                'color': im_color,
                'cylinder_count': im_cylinder_count,
                'price': im_price
            }
        })


class Car(Vehicle):

    def __init__(self, im_name, im_created_date, im_color, im_cylinder_count, im_price):
        print("registering your car")
        time.sleep(2)
        vehicle = Vehicle.init(im_name, im_created_date, im_color, im_cylinder_count, im_price)
        self.vehicle_name = vehicle.vehicle_name
        self.vehicle_created_date = vehicle.vehicle_created_date
        self.vehicle_color = vehicle.vehicle_color
        self.vehicle_cylinder_count = vehicle.vehicle_cylinder_count
        self.vehicle_age = vehicle.vehicle_age
        self.vehicle_rented = vehicle.vehicle_rented
        self.vehicle_price = vehicle.vehicle_price
        CarShop.cars_list.update({
            im_name: {
                'creation_date': im_created_date,
                'color': im_color,
                'cylinder_count': im_cylinder_count,
                'price': im_price
            }
        })


class Boat(Vehicle):

    def __init__(self, im_name, im_created_date, im_color, im_cylinder_count, im_price):
        print("registering your boat")
        time.sleep(2)
        vehicle = Vehicle.init(im_name, im_created_date, im_color, im_cylinder_count, im_price)
        self.vehicle_name = vehicle.vehicle_name
        self.vehicle_created_date = vehicle.vehicle_created_date
        self.vehicle_color = vehicle.vehicle_color
        self.vehicle_cylinder_count = vehicle.vehicle_cylinder_count
        self.vehicle_age = vehicle.vehicle_age
        self.vehicle_rented = vehicle.vehicle_rented
        self.vehicle_price = vehicle.vehicle_price
        CarShop.boat_list.update({
            im_name: {
                'creation_date': im_created_date,
                'color': im_color,
                'cylinder_count': im_cylinder_count,
                'price': im_price
            }
        })


class Client:

    rented_cars = []

    def __init__(self, i_name, i_lname, i_phone, i_wallet):
        print('registering the client ...')
        time.sleep(1)

        self.client_name = i_name
        self.client_lname = i_lname
        self.client_phone = i_phone
        self.client_wallet = i_wallet

        print('registered successfully ...')

    def rent(self, obj):
        print('renting your vehicle ...')

        if obj.is_rented():
            print("this vehicle is already rented ...")
        elif self.client_wallet < obj.vehicle_price:
            print(f"Insufficient funds to rent {obj.vehicle_name}. Required: {obj.vehicle_price}, Available: {self.client_wallet}")
        else:
            self.rented_cars.append(obj)
            obj.vehicle_rented = True
            self.client_wallet -= obj.vehicle_price
            time.sleep(1)
            print(f"{obj.vehicle_name} is now rented ...")

    def withdraw(self, obj):
        print('returning your vehicle ...')

        if not obj.is_rented():
            print("this vehicle is not rented ...")
        else:
            self.rented_cars.remove(obj)
            obj.vehicle_rented = False
            time.sleep(1)
            print(f"{obj.vehicle_name} is now returned ...")


car1 = Car('benz cls', 2022, 'white', 12, 500)
car2 = Car('bmw i8', 2020, 'black', 14, 400)
car3 = Car('nissan gtr', 2012, 'red', 10, 300)
car4 = Car('zantia e400', 2024, 'blue', 8, 600)

motorcycle1 = MotorCycle('yamaha r1', 2019, 'blue', 4, 150)
motorcycle2 = MotorCycle('ducati panigale', 2021, 'red', 4, 200)

boat1 = Boat('sunseeker', 2018, 'white', 8, 1000)
boat2 = Boat('yachtmaster', 2022, 'black', 12, 1500)

client1 = Client('mamad', 'gholi', '09373260257', 450)
client2 = Client('ali', 'reza', '09123456789', 1000)
client3 = Client('zahra', 'ahmadi', '09876543210', 2000)
client4 = Client('sara', 'hosseini', '09198765432', 100)

print("\nCars available in the shop:")
for k, v in CarShop.cars_list.items():
    print(f'{k} : {v}')

print("\nMotorcycles available in the shop:")
for k, v in CarShop.motor_list.items():
    print(f'{k} : {v}')

print("\nBoats available in the shop:")
for k, v in CarShop.boat_list.items():
    print(f'{k} : {v}')

client1.rent(car1)
client1.rent(car2)
client1.withdraw(car2)

client2.rent(motorcycle1)
client2.rent(motorcycle2)
client2.withdraw(motorcycle1)

client3.rent(boat1)
client3.rent(boat2)
client3.withdraw(boat1)

client4.rent(car1)
client4.rent(motorcycle2)
client4.rent(boat1)

print(f"\n{client1.client_name} now has {client1.client_wallet} in the wallet.")
print(f"{client2.client_name} now has {client2.client_wallet} in the wallet.")
print(f"{client3.client_name} now has {client3.client_wallet} in the wallet.")
print(f"{client4.client_name} now has {client4.client_wallet} in the wallet.")
