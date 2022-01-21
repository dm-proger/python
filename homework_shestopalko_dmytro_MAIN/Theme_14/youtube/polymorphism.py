# Changing one form to another form
# Different implementation of the same function in different situations

class Language():
    def say_hello(self):
        raise NotImplementedError("Please use say_hello class in child class")


class French(Language): #We are using inheritance to the abstract class
    # def say_hello(self):
    #     print("Bonjur")
    pass


class Chinese(Language):
    def say_hello(self):
        print("Ni Hao")


def intro(lang):
    lang.say_hello()


Maria = French()
Mao = Chinese()

intro(Maria)
intro(Mao)
