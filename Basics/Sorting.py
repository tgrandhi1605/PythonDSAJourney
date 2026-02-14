def sort(list):
    sorted_list = sorted(list,
                         key=lambda  x: float(x["price"]))

    print(sorted_list)

if __name__ == "__main__":
    products = [
        {"name": "iPhone 15", "price": "999.00"},
        {"name": "AirPods", "price": "129.00"},
        {"name": "MacBook Pro", "price": "1999.00"},
        {"name": "Charging Cable", "price": "19.00"}
    ]
    sort(products)

