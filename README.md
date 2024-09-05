# Financial Transaction Analyzer

This tool is designed to work with the transaction data exported from AIB Bank in CSV format. However, you can easily modify the code to work with other banks by adjusting the column names and formats in the data preprocessing steps. 
It processes CSV files containing transaction data, filters and summarizes income and expenses, and generates insightful visualizations. 
You can use this tool to better understand your financial habits, track savings, and detect anomalies in your transactions.

## Features

- **Load and Clean Data**: Reads CSV files containing your transaction data and handles missing or erroneous values.
- **Filter and Summarize**: Filters expenses and income, groups data by transaction categories and months, and provides insightful summaries.
- **Visualize Trends**: Generates bar charts and line graphs to visualize your top expense categories and monthly financial trends (income, expenses, and savings).
- **Anomaly Detection**: Highlights unusual spikes or dips in spending or income using a simple anomaly detection mechanism.

### Class Overview

1. **DataLoader** (`data_loader.py`)
   - Responsible for loading transaction data from a CSV file and cleaning it (handling missing values, converting data types).
   
2. **TransactionAnalyzer** (`transaction_analyzer.py`)
   - Analyzes transactions by filtering expenses and income, grouping by categories or months, and detecting anomalies.
   
3. **Plotter** (`plotter.py`)
   - Handles plotting bar charts and line graphs for the visual analysis of the data.
   
4. **FinancialAnalyzer** (`finance_analyzer.py`)
   - Coordinates the entire analysis process by using the DataLoader, TransactionAnalyzer, and Plotter classes.