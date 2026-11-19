from products import Product , find_product
from orders import Order
from storage import save , load
data=load()
products= []
for item in data:
    products.append(
        Product(item["product_id"], item["name"], item["price"], item["stock"])
     )
order=Order(1001)
for product in products:
    product.show_info()

while True:
    try:
      user_input= int(input("\nEnter Product ID: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    data_of_product=find_product(products,user_input)
    if  not data_of_product :
        print("Please enter an ID that exists.")
        continue
    while True:
        try:
            user_quantity= int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if user_quantity <=0:
            print("Please enter an positive number!.")
            continue
        break
    add_items=order.add_item(data_of_product,user_input,user_quantity)
    if  not add_items:
         print("please enter a number that we can sell it to you. ")
         continue
    exit_code=input("If you want to exit from order enter 0: ")
    if exit_code=='0':
        break
print("\nYour Purchase Invoice is here.") 
order.show_order()
confirmed=False
while True:
    confrim=input("Do you confirm? Yes or No: ") 
    if confrim.lower()=="no":   
        order.delete_order()
        break
    elif confrim.lower()=="yes":
        confirmed=True
        break
# stock_available = True
# for item in order.items:
#         product_id=item["product_id"]
#         quantity=item["quantity"]
#         product=find_product(products,product_id)
#         if product.stock<quantity:
#             stock_available=False
#             break
if confirmed:
    for item in order.items:
        product_id=item["product_id"]
        quantity=item["quantity"]
        product=find_product(products,product_id)
        inventory_reduction=product.reduce_stock(quantity)
    print("Your purchase was successful.")
else:
    print("Your purchase failed.")
for product in products:
    product.show_info()
save(products)
    