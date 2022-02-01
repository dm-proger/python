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
    def __init__(self, type_atr: str, name: str, price: int|float):
        self.type_atr = type_atr
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name


class ProductStore:
    def __init__(self, product_dict: dict):
        self.products = product_dict

    def __repr__(self):
        res = ""
        for i in self.products:
            res += str(i) + ": amount = " + str(self.products[i]) + "; total cost = " + str(i.price * self.products[i]) + "\n"
        return res

# # add(product, amount) - adds a specified quantity of a single product
# #       with a predefined price premium for your store(30 percent)
    def add(self, product: Product, amount: int):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount
        return self.products
#
# # set_discount(identifier, percent, identifier_type=’name’) -
# #   adds a discount for all products specified by input identifiers (type or name).
#
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


#
# # sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# #        in other case raises an error.
    def sell_product(self):
        ...
#
# # get_income() - returns amount of many earned by ProductStore instance.
    def get_income(self):
        ...
    #
# # get_all_products() - returns information about all available products in the store.
    def get_all_products(self):
        ...
#
# # get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
    def get_product_info(self, product_name: str, ):
        ...


def main():
    product_01 = Product("sport", "football T-shirt", 100)
    product_02 = Product("food", "ramen", 1.5)
    print(
        f"Here is a category of {product_01.type_atr}, the object is {product_01.name}. The price per piece is {product_01.price}")

    store = ProductStore({product_01: 3, product_02: 5})
    store.add(Product("food", "bananas", 7), 5)
    store.add(product_02, 5)

    store.set_discount("bananas", 10)


    print(store)

if __name__ == "__main__":
    main()
