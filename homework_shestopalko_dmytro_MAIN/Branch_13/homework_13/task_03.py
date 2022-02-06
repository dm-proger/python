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
            if identifier_type == "name":
                if identifier == i.name:
                    i.price -= i.price * percent / 100
            else:
                if identifier == i.type:
                    i.price -= i.price * percent / 100


    def sell_product(self, product: Product, amount:int):
        try:
            if product in self.products:
                self.products[product] -= amount
                self.income = amount * product.price
            else:
                print("Item is not available")
            return self.products
        except NameError:
            print("There is no such an item")


    def get_income(self):
        print(self.income)
        return self.income


    def get_all_products(self):
        if self.products:
            return self.products
        else:
            print("Store is empty")


    def get_product_info(self, product_name: str):
        for item, item_info in self.products.items():
            if item.name == product_name:
                print(item.name, item_info)
                return item.name, item_info
        print("The product is not found")


def main():
    product_01 = Product("sport", "football T-shirt", 10)
    product_02 = Product("food", "ramen", 1.5)
    store = ProductStore({product_01: 50, product_02: 5})
    store.add(Product("food", "bananas", 7), 5)
    store.add(Product("food", "apples", 10), 9)
    store.add(product_02, 5)
    store.set_discount("bananas", 10)
    print(store)
    store.sell_product(product_02, 2)
    store.get_income()
    print(store)


if __name__ == "__main__":
    main()
