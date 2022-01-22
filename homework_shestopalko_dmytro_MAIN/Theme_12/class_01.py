class Car():

    total_number_of_cars = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0
        Car.total_number_of_cars += 1

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

car1 = Car("Volvo", "V90", "2017", "black")
print(Car.total_number_of_cars)
car2 = Car("Ford", "Focus", 2014, "grey")
print(Car.total_number_of_cars)
car2 = Car("Ford", "Focus", 2014, "grey")
print(Car.total_number_of_cars)
# # print(my_car.brand)
# # print(my_car.model)
# # print(my_car.year)
# print(my_car.color)
# my_car.repaint("green")
# print(my_car.color)
# print(my_car.total_driven_km)
# my_car.drive(1000)
# print((my_car.total_driven_km))