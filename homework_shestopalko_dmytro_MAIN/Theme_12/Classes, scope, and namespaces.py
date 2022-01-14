class Car():

    # This variable belongs to the class, not to the particular instance!
    total_number_of_cars = 0

    def __init__(self, brand, model, year, color):
        # Methods
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0
        Car.total_number_of_cars += 1

    # Instance of this class with arguments
    # Methods

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

# Now I will create an instance of the Class:

my_car = Car("Volvo", "V90", "2017", "black")
print(my_car.brand)
print(my_car.model)
print(my_car.year)
print(my_car.color)

# print(my_car.color)
# my_car.repaint("green")
# print(my_car.color)
# print(my_car.total_driven_km)
# my_car.drive(1000)
# print(my_car.total_driven_km)

# Multiple instances of the same class:

car1 = Car("Volvo", "v90", 2016, "white")
print(Car.total_number_of_cars)
car2 = Car("Ford", "Focus", 2014, "grey")
print(Car.total_number_of_cars)
# print(type(car1))
# print(type(car2))

# print("car1 is of brand " + car1.brand)
# print("car2 is of brand " + car2.brand)



