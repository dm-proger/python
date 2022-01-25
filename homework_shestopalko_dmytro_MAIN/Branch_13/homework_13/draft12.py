CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.count_number = 0
        self.turned_channel = channels[self.count_number]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, number):
        try:
            self.count_number = (number + 1)
            self.turned_channel = self.channels[self.count_number]
            return self.turned_channel

        except IndexError("There is no such a channel") as executed:
            print(executed)

        except TypeError("Please, enter a number on the remote control") as executed:
            print(executed)

    def next_channel(self):
        if self.count_number == len(self.channels) - 1:
            self.count_number = 0
        else:
            self.count_number += 1
            self.turned_channel = self.channels[self.count_number]
        return self.turned_channel

    def previous_channel(self):
        if self.count_number == 0:
            self.count_number == len(self.channels) - 1
        else:
            self.count_number += 1
        self.turned_channel = self.channels[self.count_number]
        return self.turned_channel

    def current_channel(self):
        return self.turned_channel

    def is_exist(self, channel: int | str):
        try:
            if type(channel) == int and self.channels[channel - 1]:
                print("Yes")

            elif type(channel) == str:
                if channel in self.channels:
                    print("Yes")
                else:
                    print("No")

        except IndexError:
            print("No")

    def main():
        controller = TVController(CHANNELS)
        print(controller.first_channel)
        print(controller.last_channel())
        print(controller.turn_channel(1))
        print(controller.next_channel())
        print(controller.previous_channel())
        print(controller.current_channel())
        controller.is_exist(4)
        controller.is_exist("BBC")

    if __name__ == "__main__":
        main()
