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
    def __init__(self, type_atr: str, name: str, price: int, quantity: int):
        self.type_atr = type_atr
        self.name = name
        self.price = price
        self.quantity = quantity

product_01 = Product("sport", "football T-shirt", 100, 20)
product_02 = Product("food", "ramen", 1.5, 30)

product_list = [product_01, product_02]


class ProductStore:
    def __init__(self, product_03: str, product_04: str, product_05: str):
        self.product_01 = product_03
        self.product_02 = product_04
        self.product_03 = product_05

    # # add(product, amount) - adds a specified quantity of a single product
    # #       with a predefined price premium for your store(30 percent)
    def add(self):
        ...
    #
    # # set_discount(identifier, percent, identifier_type=’name’) -
    # #   adds a discount for all products specified by input identifiers (type or name).
    #
    # def set_discount(self):
    #     pass
    #
    # # sell_product(product_name, amount) - removes a particular amount of products from the store if available,
    # #        in other case raises an error.
    # def sell_product(self):
    #     ...
    #
    # # get_income() - returns amount of many earned by ProductStore instance.
    # def get_income(self):
    #     ...
    #
    # # get_all_products() - returns information about all available products in the store.
    # def get_all_products(self):
    #     ...
    #
    # # get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
    # def get_product_info(self, product_name: str, ):
    #     ...


def main():
    print(f"Here is a category of {product_01.type_atr}, the object is {product_01.name}. The price per piece is {product_01.price}")


if __name__ == "__main__":
    main()
