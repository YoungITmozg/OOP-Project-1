class Product:
    def __init__(self, id: int, name: str, price: int, stock: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print('Недопустимое значение')

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print('Недоступное значение')

    def __str__(self):
        return 'Номер товара:{} \tНазвание:{} \tЦена:{} \tКоличество:{}'.format(self.__id, self.__name, self.__price, self.__stock)

class CartItem:
    def __init__(self, product, qty):
        self.__qty = qty
        self.__product = product

    @property
    def product(self):
        return self.__product
   
    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        if qty > 0:
            self.__qty = qty
        else:
            print('Недопустимое значение')

class Cart:
    cartItems = []

    def addProduct(self, product):
        newItem = CartItem(product, 1)
        self.cartItems.append(newItem)

    def remove(self, productId):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        self.cartItems.remove(foundCartItem)

    def changeQty(self, productId, newQty):
        foundCartItem = next((i for i in self.cartItems if i.product.id == productId), None)
        foundCartItem.qty = newQty
    
    def geTotalPrice(self):
        total = 0
        for cartItem in self.cartItems:
            total = (total + cartItem.product.price) * cartItem.qty
        return total

    
t = Product(1, 'Лейс', 100, 500)
t2 = Product(2, 'Твикс', 35, 10)
t3 = Product(3, 'Сникерс', 42, 53)

c = Cart()

c.addProduct(t)
c.addProduct(t2)
c.addProduct(t3)

c.remove(2)

c.changeQty(1, 5)

total = c.geTotalPrice()

print()

#products = [t, t2, t3]



# for p in products:
#     print(p)

# class Cart:
#     products = []

#     def add(self, id: int, name: str, price: int, stock: int):

#         return products.append()











