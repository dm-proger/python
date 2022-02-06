# Write a class Product that has three attributes:
# type
# name
# price

# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:
# The discount must be specified in percentage

# It also increments income if the sell_product method succeeds.

# p = Product("Sport", "Football T-Shirt", 100)
# p2 = Product("Food", "Ramen", 1.5)
# s = ProductStore()
# s.add(p, 10)
# s.add(p2, 300)
# s.sell("Ramen", 10)
# assert s.get_product_info("Ramen") == ("Ramen", 290)

class Product:
    def __init__(self, type_atr: str, name: str, price: float):
        self.type_atr = type_atr
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name


class ProductStore:
    income = 0
    def __init__(self, product_dict: dict = {}):
        self.products = product_dict

    def __repr__(self):
        res = ""
        for i in self.products:
            res += str(i) + ": amount = " + str(self.products[i]) + "; total cost = " + str(i.price * self.products[i]) + "\n"
        return res


    def add(self, product: Product, amount: int):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount
        return self.products


    def set_discount(self, identifier: str, percent: float, identifier_type:str = "name"):
        for i in self.products:
            # if identifier_type == "name":
            #     if identifier == i.name:
            #         i.price -= i.price * percent / 100
            # else:
            #     if identifier == i.type:
            #         i.price -= i.price * percent / 100
            if getattr(i, identifier_type) == identifier:
                i.price -= i.price * percent / 100


    def sell_product(self, product: Product, amount:int):
        try:
            if product in self.products:
                self.products[product] -= amount
                self.income = amount * self.price
            else:
                print("Item is not available")
            return self.products
        except NameError:
            print("There is no such an item")


    def get_income(self):
        return self.income

        # if product in self.products:
            # product_price = self.products[product][2]
            # product_quantity = self.products[1]
            # total_income = product_price * product_quantity
            # total_income = price * self.products[]
            # return total_income

            # dict_pairs = self.products.items()
            # pairs_iterator = iter(dict_pairs)
            # first_pair = next(pairs_iterator)
            # product_amount = first_pair[1]
            # print(first_pair)
            # print(product_amount)

            # product_amount = next(iter(self.products.items()))[1]
            # total_income = product_amount * price
            # print(product_amount)
            # print(total_income)


    def get_all_products(self):
        if self.products:
            return self.products
        else:
            print("Store is empty")
        #- returns information about all available products in the store.
        # if product in self.products:
        #     price = self.products[product][2]
        #     amount = store[product_01]
        #     sold_items = price * amount
        #     print(sold_items)
        # else:
        #     print("error")


#
# # get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
    def get_product_info(self, product_name: str):
        for item, item_info in self.products.items():
            if item.name == product_name:
                print(item.name, item_info)
                return item.name, item_info
        print("The product is not found")


def main():
    product_01 = Product("sport", "football T-shirt", 10)
    product_02 = Product("food", "ramen", 1.5)
    # print(f"Here is a category of {product_01.type_atr}, the object is {product_01.name}. "
    #       f"The price per piece is {product_01.price}")

    store = ProductStore({product_01: 50, product_02: 5})
    store.add(Product("food", "bananas", 7), 5)
    store.add(Product("food", "apples", 10), 9)
    store.add(product_02, 5)
    store.set_discount("bananas", 10)
    print(store)

    store.get_income()
    print(f"the income from sold items is: " + str({store}))


if __name__ == "__main__":
    main()
