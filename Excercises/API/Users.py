import requests

class Users:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
        self.users = None

    def get_users(self):
        if self.users is None:
            print(f"Fetching users from {self.api_endpoint}...")
            try:
                response = requests.get(self.api_endpoint)
                if response.status_code == 200:
                    self.users = response.json()
                else:
                    print(f"Failed to fetch users. Status code: {response.status_code}")
            except requests.exceptions.RequestException as error:
                print(f"An error occurred while fetching users: {error}")

        return self.users

    def get_users_details(self):
        details = []
        users_response = self.get_users()

        if not users_response:
            print("No users found.")
            return details

        for user in users_response:
            addresses = user.get("address", {})

            if isinstance(addresses, dict):
                suite_name = addresses.get("suite", "")

                if "Suite" in suite_name:
                    details.append(user.get("email", None))


        return details

    def get_users_city_map(self):
        city_map = {}

        details = []
        users_response = self.get_users()

        if not users_response:
            print("No users found.")
            return details

        for user in users_response:
            address = user.get("address", {})

            if isinstance(address, dict):
                city_map[user.get("username", None)] = address.get("city", None)

        return city_map

    def get_city_stats(self):
        city_stats = {}

        details = []
        users_response = self.get_users()

        if not users_response:
            print("No users found.")
            return details

        for user in users_response:
            address = user.get("address", {})

            if isinstance(address, dict):
                city_stats[address.get("city", None)] = city_stats.get(address.get("city", None), 0) + 1

        return city_stats





if __name__ =="__main__":
    users = Users("https://jsonplaceholder.typicode.com/users")
    print(users.get_users_details())
    print(users.get_users_city_map())
    print(users.get_city_stats())








