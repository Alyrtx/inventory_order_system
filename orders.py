import products as pr
class Order:
    def __init__(self,order_id):
        self.order_id=order_id
        self.items=[]
    def add_item(self, product, product_id, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity<=0:
             raise ValueError("Quantity must be a positive integer")
        existing_item=None
        for item in self.items:
            if item["product_id"]==product_id:
                existing_item= item
                break
        if existing_item:
            if (existing_item["quantity"]+quantity)>product.stock:
                return False
            existing_item["quantity"]+=quantity
        else:
            if product.stock<quantity:
                return False
            self.items.append({
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": product.price
            })
        return True
    def calculate_total(self,item):
        total=0
        total+=item["quantity"] * item["unit_price"]
        return total
    def show_order(self):
        print("*"*30)
        total_order_price=0
        for order in self.items:
            price=self.calculate_total(order)
            total_order_price+=price
            print(f"Product ID: {order["product_id"]}\nTotal Price: {price}$\nQuantity: {order["quantity"]}")
            print("*"*30)
        print(f"\nTotal order price: {total_order_price}$")
    def delete_order(self):
        self.items=[]
            
        
