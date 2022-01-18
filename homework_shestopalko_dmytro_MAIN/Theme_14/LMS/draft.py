# class User:
#     pass
#
# user1 = User()
# user1.first_name = "Dave"
# user1.last_name = "Bowman"
#
# # print(user1.first_name)
# #
# # print(user1.last_name)
#
# first_name = "Arthur"
# last_name = "Clarke"
#
# # print(first_name, last_name)
#
# user2 = User()
# user2.first_name = "Frank"
# user2.last_name = "Poole"
#
# print(first_name, last_name)
# print(user1.first_name, user1.last_name)
# print(user2.first_name, user2.last_name)
#
# user1.age = 37
# user2.favorite_book = "2001: A Space Odyssey"
#
# print(user1.age)
# print(user2.age)
# # print(user2.favorite_book)


# self is a reference to a new object that has been created
class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

user = User("Dave Bowan", 19970309)
# print(user.name)
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)





