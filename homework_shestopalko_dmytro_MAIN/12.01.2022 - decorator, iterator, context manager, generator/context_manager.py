import time


class Programmer:

    # noinspection PyMethodMayBeStatic
    def at_begin(self):
        print(f"Check TODOs`")

    #  noinspection PyMethodMayBeStatic
    def work(self, hours: int):
        time_to_broke = hours // 2

        for hour in range(hours):
            print(f"Working {hour}/{hours} hours.")
            time.sleep(0.5)

            if hour >= time_to_broke:
                raise ValueError("Something wrong")

    #  noinspection PyMethodMayBeStatic
    def at_end(self):
        print(f"Make report")


if __name__ == "__main__":
    programmer = Programmer()
    programmer.at_begin()
    try:
        programmer.work(hours=8)
    finally:
        programmer.at_end()