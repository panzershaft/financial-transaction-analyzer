from config import FILE_MAPPING
from data_loader import DataLoader
from plotter import Plotter
from transaction_analyzer import TransactionAnalyzer


class FinancialAnalyzer:
    def __init__(self, data_loader, plotter):
        self.data_loader = data_loader
        self.plotter = plotter

    def run_analysis(self):
        try:
            # Load data
            self.data_loader.load_data()
            self.data_loader.clean_data()
            transactions = self.data_loader.get_data()
            analyzer = TransactionAnalyzer(transactions)

            # Analyze data
            expenses = analyzer.filter_expenses()
            analyzer.filter_income()
            monthly_summary = analyzer.group_by_month()

            # Plot
            expense_summary = analyzer.group_by_description(expenses).sort_values(ascending=False).head(5)
            self.plotter.plot_bar(expense_summary, 'Top 5 Expense Categories', 'Amount (€)')

            self.plotter.plot_line(
                monthly_summary.index.astype(str),
                {
                    'Income': monthly_summary['Credit Amount'],
                    'Expenses': monthly_summary['Debit Amount']
                },
                'Monthly Income and Expenses'
            )
        except Exception as e:
            print(f"An error occurred during the analysis: {e}")


if __name__ == "__main__":
    file_path = FILE_MAPPING['2023.csv']
    data_loader = DataLoader(file_path)
    plotter = Plotter()

    analysis_app = FinancialAnalyzer(data_loader, plotter)
    try:
        # Run the main code
        analysis_app.run_analysis()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")