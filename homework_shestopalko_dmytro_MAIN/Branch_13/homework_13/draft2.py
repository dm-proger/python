class Product:
    def __init__(self, type_atr: str, name: str, price: int):
        self.type_atr = type_atr
        self.name = name
        self.price = price

    def __repr__(self):
        product_object = product_list
        return product_object

product_01 = Product("sport", "football T-shirt", 100)
product_02 = Product("food", "ramen", 1.5)

product_list = [product_01, product_02]

def main():
    print(f"Here is a category of {product_01.type_atr}, the object is {product_01.name}. The price per piece is {product_01.price}")
    print(repr(product_list[0]))

if __name__ == "__main__":
    main()