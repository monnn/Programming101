class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = self.final_price - self.stock_price
        return profit


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


class Store():
    laptop_list = {}
    smartphone_list = {}

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        self.product = Product
        if product is Laptop:
            self.laptop_list.update({product: count})
        if product is Smartphone:
            self.smartphone_list.update({product: count})

    def list_products(self, product_class):
        if product_class == 'Laptop':
            return self.laptop_list
        elif product_class == 'Smartphone':
            return self.smartphone_list


new_product = Product('HP HackBook', 1000, 1243)
print(new_product.profit())
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
print(new_smarthphone.display_size)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)
new_store.load_new_products(new_laptop, 10)
print(new_store.list_products(Laptop))
