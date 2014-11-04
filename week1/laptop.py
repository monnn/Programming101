class Laptop(Product):
    def __init__(self, stock_price, final_price, diskspace, RAM):
        self.diskspace = diskspace
        self.RAM = RAM
        super().__init__(name, stock_price, final_price)