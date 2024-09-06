import pandas as pd
import matplotlib.pyplot as plt
import os

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = None

    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        try:
            self.transactions = pd.read_csv(self.file_path)
        except Exception as e:
            raise Exception(f"Error loading CSV file: {e}")

    def clean_data(self):
        if self.transactions is None:
            raise ValueError("No data loaded. Run load_data() first.")

        # Strip whitespace from column names
        self.transactions.columns = self.transactions.columns.str.strip()

        # Convert numeric columns
        self.transactions['Debit Amount'] = pd.to_numeric(self.transactions['Debit Amount'], errors='coerce')
        self.transactions['Credit Amount'] = pd.to_numeric(self.transactions['Credit Amount'], errors='coerce')

        self.transactions['Posted Transactions Date'] = pd.to_datetime(self.transactions['Posted Transactions Date'],
                                                                       errors='coerce')

        # Calculate net amount (income - expenses)
        self.transactions['Net Amount'] = self.transactions['Credit Amount'].fillna(0) - self.transactions[
            'Debit Amount'].fillna(0)

    def get_data(self):
        """Returns the cleaned transactions data."""
        if self.transactions is None:
            raise ValueError("No data available. Run load_data() and clean_data() first.")
        return self.transactions