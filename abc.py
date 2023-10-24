
numOfProducts = input("Enter amount of products: ")
productList = []


for i in range(int(numOfProducts)):
    product = input("enter product")
    category = input("category")
    quantity = input("quantity")

    products = {
    "Product" : product ,
    "Category" : category ,
    "Quantity" : quantity
}
    productList.append(products)
for i in range(len(productList)):
    print(productList[i])

print(productList[1]["Product"])






