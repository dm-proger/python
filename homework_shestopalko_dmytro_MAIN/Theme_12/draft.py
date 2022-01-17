class Car():
    def __init__(self, engine: str, cab: str, chassis: str, year: int):
        self.engine = engine
        self.cab = cab
        self.chassis = chassis
        self.year = year

def ride() -> str:
    car_01 = Car("V4", "cab", "back_rolled", 2015)
    print(f"My car Mercedes has {car_01.engine}, fully-equipped {car_01.cab}, {car_01.chassis} chassis. It was made in {car_01.year} ")


if __name__ == "__main__":
    ride()
