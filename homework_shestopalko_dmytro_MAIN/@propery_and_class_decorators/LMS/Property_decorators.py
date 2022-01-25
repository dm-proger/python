class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    @property
    def full_name(self):
        return self.first_name.title() + "" + self.last_name.title()

    @property
    def initials(self):
        return self.first_name[0].upper() + self.last_name[0].upper()

    # @full_name.setter
    # def full_name(self, name):
    #     first, last = name.split(" ")
    #     self.first_name = first.title()
    #     self.last_name = last.title()

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print("deleted")

cj = Person('carl', 'johnson')
print(cj.full_name)
print(cj.initials)
del cj.full_name
# cj.first_name = 'buster karlson'
print(cj.full_name, cj.last_name)
# print(cj.initials)