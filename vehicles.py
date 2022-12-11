# 1. Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний
#засіб". Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

# без методів та зміни значень атрибутів, бо не в цьому завдання. Втім для наслідування розділив "пасажирськість"
# та "вантажність" на різні підкласи.
# А так набір атрибутів дуже довільний і не заточений ні на яку кокретну майбутню задачу

class Vehicle:
    model_name = None
    speed_cruise_kmph = 0
    speed_max_kmph = 0
    weight_kg = 0


class VehicleLand(Vehicle):
    length_m = 5
    width_m = 1.8
    weight_kg = 1500


class VehicleFlying(Vehicle):
    span_wings_m = 50
    length_m = 70
    flight_height_max_m = 10000


class VehicleSwimming(Vehicle):
    displacement_ton = 1200
    length_m = 150
    width_m = 20
    draught_max_m = 3.5
    name = None
    home_port = 'Panama'


class PassengerCarrier:
    passengers_load_max = 1


class Freighter:
    freight_load_max_kg = 500


class Car(VehicleLand, PassengerCarrier):
    car_body_type = 'Universal'
    engine_power_hp = 58
    engine_volume_cc = 1500


class Lorry(VehicleLand, Freighter):
    height_m = 2.7
    num_axles = 3


class PickUp(Car, Freighter):
    pass


class PlanePassenger(VehicleFlying, PassengerCarrier):
    pass


class PlaneFreighter(VehicleFlying, Freighter)
    pass


class CruiseLiner(VehicleSwimming, PassengerCarrier):
    pass


class ShipFreighter(VehicleSwimming, PassengerCarrier):
    pass



bmw_6 = Car()
man_1100 = Lorry()
american_truck = PickUp()
an_24 = PlanePassenger()
an_2 = PlaneFreighter()
etoil_du_france = CruiseLiner()
ever_given = ShipFreighter()



