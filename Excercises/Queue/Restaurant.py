from Excercises.Queue.Queue import Queue
from threading import Thread
import time

class Restaurant:
    def __init__(self, orders):
        self.orders = orders

    def place_order(self, orders):
        for item in orders:
            time.sleep(0.5)
            self.orders.enqueue(item)
            print(f"Placed order for {item}")


    def serve_order(self):
        while not self.orders.is_empty():
            order = self.orders.dequeue()
            print(f"Serving {order}")
            time.sleep(2)

if __name__  =="__main__":
    orders = ["Pizza", "Burger", "Pasta", "Salad"]
    order_queue = Queue()
    restaurant = Restaurant(order_queue)
    place_order_thread = Thread(target=restaurant.place_order(orders), args=(orders,))
    serve_order_thread = Thread(target=restaurant.serve_order(), args=(orders,))
    place_order_thread.start()
    serve_order_thread.start()

    place_order_thread.join()
    serve_order_thread.join()



