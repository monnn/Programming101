class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = self.final_price - self.stock_price
        return profit

new_product = Product('HP HackBook', 1000, 1243)
print(new_product.profit())  # 243


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        self.diskspace = diskspace
        self.RAM = RAM
        super().__init__(name, stock_price, final_price)

class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
print(new_smarthphone.display_size)

class Store():
    def __init__(self, name):
        self.name = name
new_store = Store('Laptop.bg')

