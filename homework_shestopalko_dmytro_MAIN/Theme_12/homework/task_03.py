# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1,
# not from 0.
# next_channel() - turns on the next channel.
# If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one,
# turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
#
# CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():

    channels = ["BBC", "Discovery", "TV1000"]

    def __init__(self, first_channel, last_channel, turn_channel, next_channel, previous_channel, current_channel, is_exist):
        self.first_channel = first_channel
        self.last_channel = last_channel
        self.turn_channel = turn_channel
        self.next_channel = next_channel
        self.previous_channel = previous_channel
        self.current_channel = current_channel
        self.is_exist = is_exist


class Buttons(TVController):

    def __init__(self, channel_01, channel_02, channel_03):
        self.channel_01 = channel_01
        self.channel_02 = channel_02
        self.channel_03 = channel_03

watch_tv = Buttons("BBC", "Discovery", "TV1000")

def main_menu():
    print(f"The following channels are available: 1 - {watch_tv.channel_01}, "
      f"2 - {watch_tv.channel_02}, 3 - {watch_tv.channel_03}")
main_menu()

remote_menu = input("Please, make your choice: ")
def menu_bar(remote_menu):
    if remote_menu == 1:
        print(f"You are watching {watch_tv.channel_01}")
    elif remote_menu == 2:
        print(f"You are watching {watch_tv.channel_02}")
    elif remote_menu == 3:
        print(f"You are watching {watch_tv.channel_03}")
    else:
        watch_tv_restart = input("Press 0 to return to the main menu: ")
        if watch_tv_restart == 0:
            main_menu()
        else:
            exit()
menu_bar(remote_menu)



