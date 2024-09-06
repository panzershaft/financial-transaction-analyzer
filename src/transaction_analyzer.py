class TransactionAnalyzer:
    def __init__(self, transactions):
        if transactions is None or transactions.empty:
            raise ValueError("Transactions data must not be None or empty.")
        self.transactions = transactions

    def filter_expenses(self):
        return self.transactions[self.transactions['Debit Amount'] > 0]

    def filter_income(self):
        return self.transactions[self.transactions['Credit Amount'] > 0]

    @staticmethod
    def group_by_description(transactions):
        return transactions.groupby('Description1')['Debit Amount'].sum()

    def group_by_month(self):
        self.transactions['Month'] = self.transactions['Posted Transactions Date'].dt.to_period('M')
        return self.transactions.groupby('Month').agg({
            'Debit Amount': 'sum',
            'Credit Amount': 'sum'
        })
