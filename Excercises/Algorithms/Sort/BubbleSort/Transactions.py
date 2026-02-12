class Transactions:
    def __init__(self, transactions):
        self.transactions = transactions

    def  bubble_sort(self, key):
        size = len(self.transactions)

        for i in range(size - 1):
            swapped = False
            for j in range(size - 1 - i):
                if self.transactions[j][key] > self.transactions[j + 1][key]:
                    temp = self.transactions[j]
                    self.transactions[j] = self.transactions[j +1]
                    self.transactions[j + 1] = temp
                    swapped = True

            if not swapped:
                break
        return self.transactions

if __name__ == "__main__":
    elements = [
        { 'name' : 'kathy', 'transaction_amount' : 1200, 'device' : 'vivo' },
        { 'name' : 'dhaval', 'transaction_amount' : 400, 'device' : 'google pixel' },
        { 'name' : 'aamir', 'transaction_amount' : 1800, 'device' : 'iphone-8' },
        { 'name' : 'mona', 'transaction_amount' : 1000, 'device' : 'iphone-10' }
    ]

    sort_transactions = Transactions(elements)
    sorted_transactions_by_amount = sort_transactions.bubble_sort('transaction_amount')
    print(sorted_transactions_by_amount)

    sorted_transactions_by_name = sort_transactions.bubble_sort('name')
    print(sorted_transactions_by_name)

