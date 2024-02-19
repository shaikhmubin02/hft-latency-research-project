import random

class OrderBook:
    def __init__(self):
        self.bids = {}  # Dictionary to store bid orders
        self.asks = {}  # Dictionary to store ask orders

    def add_order(self, order):
        if order['side'] == 'buy':
            if order['price'] in self.bids:
                self.bids[order['price']] += order['quantity']
            else:
                self.bids[order['price']] = order['quantity']
        elif order['side'] == 'sell':
            if order['price'] in self.asks:
                self.asks[order['price']] += order['quantity']
            else:
                self.asks[order['price']] = order['quantity']

    def remove_order(self, order):
        if order['side'] == 'buy':
            self.bids[order['price']] -= order['quantity']
            if self.bids[order['price']] == 0:
                del self.bids[order['price']]
        elif order['side'] == 'sell':
            self.asks[order['price']] -= order['quantity']
            if self.asks[order['price']] == 0:
                del self.asks[order['price']]

    def execute_trade(self, trade):
        executed_orders = []
        remaining_quantity = trade['quantity']
        for price, quantity in sorted(self.asks.items()):  # Matching against asks first
            if remaining_quantity == 0:
                break
            if quantity >= remaining_quantity:
                executed_orders.append({'price': price, 'quantity': remaining_quantity})
                self.remove_order({'side': 'sell', 'price': price, 'quantity': remaining_quantity})
                remaining_quantity = 0
            else:
                executed_orders.append({'price': price, 'quantity': quantity})
                self.remove_order({'side': 'sell', 'price': price, 'quantity': quantity})
                remaining_quantity -= quantity
        if remaining_quantity > 0:  # If there's still remaining quantity, match against bids
            for price, quantity in sorted(self.bids.items(), reverse=True):
                if remaining_quantity == 0:
                    break
                if quantity >= remaining_quantity:
                    executed_orders.append({'price': price, 'quantity': remaining_quantity})
                    self.remove_order({'side': 'buy', 'price': price, 'quantity': remaining_quantity})
                    remaining_quantity = 0
                else:
                    executed_orders.append({'price': price, 'quantity': quantity})
                    self.remove_order({'side': 'buy', 'price': price, 'quantity': quantity})
                    remaining_quantity -= quantity
        return executed_orders

def simulate_order_book_behavior(strategy, order_book, num_orders):
    for _ in range(num_orders):
        order_type = random.choice(['buy', 'sell'])
        price = random.randint(90, 110) 
        quantity = random.randint(1, 10)  
        order = {'side': order_type, 'price': price, 'quantity': quantity}
        if order_type == 'buy':
            strategy.execute_order(order, order_book.asks)
        elif order_type == 'sell':
            strategy.execute_order(order, order_book.bids)

class ExtremeLowLatencyStrategy:
    def execute_order(self, order, order_book_side):

        # Placeholder for extreme low-latency order execution behavior
        print("Executing order with extreme low latency.")

def analyze_order_book_dynamics():
    order_book = OrderBook()
    num_orders = 100  # Number of orders to simulate

    extreme_low_latency_strategy = ExtremeLowLatencyStrategy()  # Instantiate extreme low-latency strategy

    # Simulate order book behavior with extreme low-latency strategy
    simulate_order_book_behavior(extreme_low_latency_strategy, order_book, num_orders)

    # Analyze order book dynamics here, e.g., check for disruptions or front-running activities
    print("Order book dynamics analysis complete.")

if __name__ == "__main__":
    analyze_order_book_dynamics()
