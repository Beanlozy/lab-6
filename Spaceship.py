class Spaceship:
    # Constructor to create an instance of a Spaceship
    def __init__(self, make, model):
        self.MAKE = make
        self.MODEL = model
        self.power_on = False
        self.remaining_fuel = 110
        self.speed = 0

    def set_fuel(self, remaining_fuel):
        self.remaining_fuel = remaining_fuel

    def get_fuel(self):
        return self.remaining_fuel

    def power(self):
        self.power_on = not self.power_on

    def increase_speed(self):
        self.speed = self.speed + 1

    def decrease_speed(self):
        self.speed = self.speed - 1

    def get_speed(self):
        return self.speed

    def get_make(self):
        return self.MAKE

    def get_model(self):
        return self.MODEL

    def __str__(self):
        if self.power_on:
            return "A " + self.MAKE + " " + self.MODEL + " has been turned on"
        else:
            return "A " + self.MAKE + " " + self.MODEL + " has been turned off"
