class computer:

    def __init__(self):
        self.maxprice = 900

    def sell(self):
        print("selling price:",self.maxprice)

    def setmax(self,price):
        self. maxprice = price

#obj
ob1 = computer()
ob1.sell()

#change max price
ob1. maxprice = 1000
ob1.sell()