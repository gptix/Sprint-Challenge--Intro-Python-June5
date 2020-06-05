# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# This is the base class.
class Vehicle:
    pass


# Immediate subclasses of Vehicle
class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass


# Immediate subclasses of FlightVehicle
# Subsubclasses of Vehicle
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass


# Immediate subclasses of GroundVehicle
# Subsubclasses of Vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

