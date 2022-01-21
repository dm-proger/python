class Payment():
    def __init__(self, price):
        self.__final_price = price + price*0.05

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self, discount):
        if __name__ == "__main__":
            self.__final_price = self.__final_price - self.__calculate_discount(discount)

    def __calculate_discount(self, discount):
        return self.__final_price * (discount/100)

book = Payment(10)
# book.__calculate_discount(50)#Error
# book.__final_price = 0 # We can not touch this variable. It is not correct.
print(book.get_final_price())
#Public variable is a problem