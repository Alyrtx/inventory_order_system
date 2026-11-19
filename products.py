class Product:
    def __init__(self, product_id, name, price, stock):
        if isinstance(product_id, bool) or not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("Product ID must be a positive integer")
        self._product_id= product_id
        self.name= name
        self.price= price
        self.stock=stock
    @property
    def product_id(self):
        return self._product_id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, string):
        if len(string.strip())==0:
            raise ValueError("name can not be empty")
        self._name=string.strip()
        
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price<=0:
            raise ValueError("price can not be zero or negative")
        self._price=new_price
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, new_stock):
        if new_stock<0:
            raise ValueError("stock can not be negative")
        self._stock=new_stock
    def reduce_stock(self,quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity<=0:
            raise ValueError("your Quantity must be integer positive")
        if quantity>self.stock:
            return False
        self.stock-=quantity
        return True
    def show_info(self):
        print(f"Product ID: {self.product_id} \nProduct Name: {self.name}\nPrice: {self.price}$\nStock: {self.stock}")
        print("*"*30)
    def increase_stock(self, quantity):
        if quantity>0 and isinstance(quantity, int)and not isinstance(quantity, bool):
            self.stock+=quantity
            return True
        return False
def find_product(products,number):
    for product in products:
        if product.product_id==number:
            return product
    return None
def add_product(products,product_id, name, price, stock):
    result=find_product(products,product_id)
    if result is None:
        products.append(Product(product_id, name, price, stock))
        return True
    return False

