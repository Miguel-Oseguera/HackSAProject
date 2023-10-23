user= input("Enter what section of products sold: ")
shampoo=int(input('enter number of shampoo started with: '))
shampoo_sold= int(input("Number of shampoo sold: "))
shampo= (shampoo - shampoo_sold)
product = {'Beauty': ['shampoo', shampo, 'hairbrush', 'hairtyes'], 'house items': ['chair', 'bed', 'table'],
           'produce': ['apples', 'meat', 'bread']}

print(product['Beauty'][0:2])
for key, values in product.items():
    print(key, values)

    print(product['house items'][0])
