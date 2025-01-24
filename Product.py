class Product:
    def __init__(self, pid, sid, pname, category, price, inventory):
        self.product_id = pid
        self.seller_id = sid
        self.pname = pname
        self.category = category
        self.price = price
        self.inventory = inventory
        
    def __str__(self):
        return f"Product ID: {self.product_id}\tSeller ID: {self.seller_id}\tProduct Name: {self.pname}\tCategory: {self.category}\tPrice: {self.price}\tInventory: {self.inventory}\n"