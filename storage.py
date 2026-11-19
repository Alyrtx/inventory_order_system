import json
def load():
    with open("products.json", "r", encoding="utf-8") as file:
        data=json.load(file)
    return data
def save(products):
    list_product=[]
    for product in products:
        list_product.append({
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock 
    })
    with open("products.json","w", encoding="utf-8") as file:
        json.dump(list_product, file, indent=4)