class OrderQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order_id, items):
        order = {'order_id': order_id, 'items': items}
        self.queue.append(order)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display_orders(self):
        if self.is_empty():
            print("No orders in the queue.")
        else:
            print("Current Orders in Queue:")
            for order in self.queue:
                print(order)


order_queue = OrderQueue()
order_queue.enqueue(1, ["Burger", "Fries"])
order_queue.enqueue(2, ["Pizza", "Soda"])
order_queue.display_orders()
