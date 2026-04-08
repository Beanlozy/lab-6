from spaceship import Spaceship

ship = Spaceship("SpaceX", "Falcon")
ship.power()
print(ship)

fuel = int(input("How much fuel is left in the tank? "))
ship.set_fuel(fuel)
print("Remaining Fuel:", ship.get_fuel())

count = 0
while count < 60:
    ship.increase_speed()
    count = count + 1

print("Speed:", ship.get_speed())
print("Too fast! Lowering the speed.")

while ship.get_speed() > 0:
    ship.decrease_speed()

print("Speed:", ship.get_speed())

ship.set_fuel(0)
print("Remaining Fuel:", ship.get_fuel())
print("Oh no, the spaceship ran out of fuel... Now how will I get to space?")


new_ship = Spaceship("NASA", "Explorer")
new_ship.power()
print(new_ship)

fuel2 = int(input("How much fuel is left in the tank? "))
new_ship.set_fuel(fuel2)

count = 0
while count < 20:
    new_ship.increase_speed()
    count = count + 1

print("Speed:", new_ship.get_speed())
print("Remaining Fuel:", new_ship.get_fuel())
