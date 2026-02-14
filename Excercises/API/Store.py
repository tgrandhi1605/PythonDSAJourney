import requests

class Store:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
        self.cart_items = None
        self.products_info = {}

        self.product_prices = {}

        response = requests.get(f"{self.api_endpoint}/products")
        if response.status_code == 200:
            product_details = response.json()
            self.products_info = product_details

            for product in product_details:
                self.product_prices[product.get("id", None)] = product.get("price", None)


    def get_cart_items(self, cart_number):
        if cart_number:
            cart_endpoint = f"{self.api_endpoint}/carts/{cart_number}"
        else:
            cart_endpoint = f"{self.api_endpoint}/carts/"
        if self.cart_items is None:
            print(f"Fetching cart items from {cart_endpoint}...")
            try:
                response = requests.get(cart_endpoint)
                if response.status_code == 200:
                    self.cart_items = response.json()
                else:
                    print(f"Failed to fetch cart items. Status code: {response.status_code}")

            except requests.exceptions.RequestException as error:
                print(f"An error occurred while fetching cart items: {error}")

        return self.cart_items

    def get_product_price(self, product_id):
        product_endpoint = f"{self.api_endpoint}/products/{product_id}"
        print(f"Fetching product price from {product_endpoint}...")
        try:
            response = requests.get(product_endpoint)
            if response.status_code == 200:
                product_data = response.json()
                return product_data.get("price", None)
            else:
                print(f"Failed to fetch product price. Status code: {response.status_code}")
        except requests.exceptions.RequestException as error:
            print(f"An error occurred while fetching product price: {error}")


    def get_cart_total(self, cart_number):
        cart_items = self.get_cart_items(cart_number)
        total = 0

        if not cart_items:
            print("No cart items found.")
            return total

        products_in_cart = cart_items.get("products", [])
        if products_in_cart:
            for product in products_in_cart:

                total += self.product_prices[product.get("productId", 0.0)] * product.get("quantity", 0)
        return total

    def get_products_from_cart(self):
        cart_products = []
        cart_items = self.get_cart_items(None)

        if not cart_items:
            print("No cart items found.")
            return cart_products

        for c in cart_items:
            products_in_cart = c.get("products", [])

            if products_in_cart:
                for product in products_in_cart:
                    cart_products.append(product.get("productId", None))

        return cart_products

    def get_unsold_products(self, products_in_cart):
        unsold_products = []
        for pro in self.products_info:
            if pro:
                if pro.get("id", None) not in products_in_cart:
                    unsold_products.append(pro.get("id", None))
        return unsold_products


if __name__ =="__main__":
    store = Store("https://fakestoreapi.com")
    cart = 1
    cart_total = store.get_cart_total(cart)
    print(f"Total price of items in cart {cart}: {cart_total}")
    cart_products = store.get_products_from_cart()
    orphaned_products = store.get_unsold_products(cart_products)
    print(f"Unsold products: ${orphaned_products}")
