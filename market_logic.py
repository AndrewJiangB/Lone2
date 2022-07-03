class Market:
    def __init__(self, buyOrders = [], sellOrders = [], users = {}, buyOrdersFulfilled = [], sellOrdersFulfilled = []) -> None:
        self.buyOrders = buyOrders
        self.sellOrders = sellOrders
        self.users = users
        self.buyOrdersFulfilled = buyOrdersFulfilled
        self.sellOrdersFulfilled = sellOrdersFulfilled

    def print_orders(self):
        print("### BUY ORDERS ###")
        for buy in self.buyOrders:
            print('Buyer: {buyer}, Item: {item}, Value: {value}'
            .format(buyer=buy.buyer, item=buy.item.name, value=buy.value))
        
        print("### SELL ORDERS ###")
        for sell in self.sellOrders:
            print('Seller: {seller}, Item: {item}, Value: {value}'
            .format(seller=sell.seller, item=sell.item.name, value=sell.value))

    def add_user(self,user):
        self.users[user.name] = user

    def addBuyOrder(self, buy):
        boughtOrder = self.buyFulfillment(buy)
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
        soldOrder = self.sellFulfillment(sell)
        if not soldOrder:
            i = 0
            while (i < len(self.sellOrders) and sell.value > self.sellOrders[i].value):
                i += 1
            self.sellOrders.insert(i, sell)
        else:
            return soldOrder

    def buyFulfillment(self, buy):
        for index, sell in enumerate(self.sellOrders):
            if buy.item.name == sell.item.name and \
                buy.value > sell.value:
                print('Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}'
                .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=buy.value))
                return self.sellOrders.pop(index)
        return
        
    def sellFulfillment(self, sell):
        for index, buy in enumerate(self.buyOrders):
            if sell.item.name == buy.item.name and \
                sell.value < buy.value:
                print('Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}'
                .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=buy.value))
                return self.buyOrders.pop(index)
        return