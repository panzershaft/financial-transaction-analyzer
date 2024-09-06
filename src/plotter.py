import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot_bar(data, title, ylabel):
        if data.empty:
            raise ValueError("No data to plot.")
        data.plot(kind='bar', color='salmon')
        plt.title(title)
        plt.ylabel(ylabel)
        plt.show()

    @staticmethod
    def plot_line(x_data, y_data_dict, title):
        if not y_data_dict:
            raise ValueError("No data to plot.")

        for label, y_data in y_data_dict.items():
            plt.plot(x_data, y_data, label=label, marker='o')
        plt.title(title)
        plt.xlabel('Month')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.show()
