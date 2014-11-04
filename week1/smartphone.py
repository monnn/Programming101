class Smartphone(Product):
    def __init__(self, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
print(new_smarthphone.display_size)
