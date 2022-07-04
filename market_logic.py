from datetime import date, datetime

class Market:
    def __init__(self, buyOrders = [], sellOrders = [], users = {}) -> None:
        self.buyOrders = buyOrders
        self.sellOrders = sellOrders
        self.users = users

    def print_orders(self):
        print('### MARKET.PRINT_ORDERS() ###');
        print("- BUY ORDERS:")
        for buy in self.buyOrders:
            print('\tBuyer: {buyer}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(buyer=buy.buyer, item=buy.item.name, value=buy.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
        
        print("- SELL ORDERS: ")
        for sell in self.sellOrders:
            print('\tSeller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(seller=sell.seller, item=sell.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))

    def add_user(self,user):
        self.users[user.name] = user

    def addBuyOrder(self, buy):
        boughtOrder = self._buyFulfillment(buy)
        if not boughtOrder:
            i = 0
            while (i < len(self.buyOrders) and buy.value < self.buyOrders[i].value):
                i += 1
            self.buyOrders.insert(i, buy)
            return
        else:
            self.users[boughtOrder.seller].sellOrderFulfilled(boughtOrder)
            return boughtOrder

    def addSellOrder(self, sell):
        soldOrder = self._sellFulfillment(sell)
        if not soldOrder:
            i = 0
            while (i < len(self.sellOrders) and sell.value > self.sellOrders[i].value):
                i += 1
            self.sellOrders.insert(i, sell)
        else:
            return soldOrder

    def cancelBuyOrder(self, order):
        for i, o in enumerate(self.buyOrders):
            if o == order:
                self.buyOrders.pop(i)
                return True
        return False

    def cancelSellOrder(self, order):
        for i, o in enumerate(self.sellOrders):
            if o == order:
                self.sellOrders.pop(i)
                return True
        return False

    def _buyFulfillment(self, buy):
        for index, sell in enumerate(self.sellOrders):
            if buy.item.name == sell.item.name and \
                buy.value > sell.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller: {seller} Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                return self.sellOrders.pop(index)
        return
        
    def _sellFulfillment(self, sell):
        for index, buy in enumerate(self.buyOrders):
            if sell.item.name == buy.item.name and \
                sell.value < buy.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller:{seller} Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                return self.buyOrders.pop(index)
        return