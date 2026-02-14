class SanitizeData:
    def __init__(self, data):
        self.data = data

    def sanitize_data(self):
        sanitized_data = {}

        for event in self.data:
            if not event["name"]:
                continue
            price = event["price"].replace('$', '')
            event["price"] = float(price)
            if event["id"] not in sanitized_data or event["version"] > sanitized_data[event["id"]]["version"]:
                sanitized_data[event["id"]] = event
        return sanitized_data

if __name__ == "__main__":
    raw_data = [
        {"id": 1, "name": "iPhone", "price": "$999.00", "version": 1},
        {"id": 1, "name": "iPhone", "price": "999.00", "version": 2},  # Keep this (higher version)
        {"id": 2, "name": None, "price": "49.00", "version": 1},  # Remove this (no name)
        {"id": 3, "name": "AirPods", "price": "150.00", "version": 1}
    ]

    sanitize = SanitizeData(raw_data)
    print(sanitize.sanitize_data())