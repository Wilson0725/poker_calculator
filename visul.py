import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys

# Create an example DataFrame
data = {'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

class DataFrameUI(QMainWindow):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DataFrame UI')
        self.setGeometry(100, 100, 800, 400)

        # Create a QTableWidget to display the DataFrame
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(len(self.df.columns))
        self.table_widget.setRowCount(len(self.df))
        self.table_widget.setHorizontalHeaderLabels(self.df.columns)

        for i, row in enumerate(self.df.values):
            for j, value in enumerate(row):
                item = str(value)
                self.table_widget.setItem(i, j, QTableWidgetItem(item))

        # Create a Matplotlib figure and canvas to display data
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.df.plot(kind='bar', x='Column2', y='Column1', ax=self.ax)
        self.ax.set_title('DataFrame Visualization')

        # Create a QWidget containing the Matplotlib canvas
        self.chart_widget = QWidget()
        self.chart_layout = QVBoxLayout()
        self.chart_layout.addWidget(self.table_widget)
        self.chart_layout.addWidget(self.canvas)
        self.chart_widget.setLayout(self.chart_layout)

        # Set the QWidget as the central widget
        self.setCentralWidget(self.chart_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataFrameUI(df)
    window.show()
    sys.exit(app.exec_())