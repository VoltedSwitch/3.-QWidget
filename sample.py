from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys


class GuiPrinter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Print Example")

        layout = QVBoxLayout()

        self.output_label = QLabel("Waiting for input...")
        button = QPushButton("Say Hello")
        button.clicked.connect(self.say_hello)

        layout.addWidget(self.output_label)
        layout.addWidget(button)
        self.setLayout(layout)

    def say_hello(self):
        self.output_label.setText("Hello from the GUI!")


app = QApplication(sys.argv)
window = GuiPrinter()
window.show()
app.exec()
