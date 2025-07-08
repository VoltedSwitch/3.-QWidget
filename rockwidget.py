from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        self.setFixedSize(700, 80)

        button0 = QPushButton("Zero")
        button0.clicked.connect(self.button0_clicked)

        button1 = QPushButton("One")
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("Two")
        button2.clicked.connect(self.button2_clicked)

        button3 = QPushButton("Three")
        button3.clicked.connect(self.button3_clicked)

        button4 = QPushButton("Four")
        button4.clicked.connect(self.button4_clicked)

        button5 = QPushButton("Five")
        button5.clicked.connect(self.button5_clicked)

        button6 = QPushButton("Six")
        button6.clicked.connect(self.button6_clicked)

        button7 = QPushButton("Seven")
        button7.clicked.connect(self.button7_clicked)

        button8 = QPushButton("Eight")
        button8.clicked.connect(self.button8_clicked)

        button9 = QPushButton("Nine")
        button9.clicked.connect(self.button9_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button0)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)
        button_layout.addWidget(button5)
        button_layout.addWidget(button6)
        button_layout.addWidget(button7)
        button_layout.addWidget(button8)
        button_layout.addWidget(button9)

        self.setLayout(button_layout)

    @staticmethod
    def click_print(prompt: str | int):
        print(prompt, end="", flush=True)

    def button0_clicked(self):
        self.click_print("0")

    def button1_clicked(self):
        self.click_print("1")

    def button2_clicked(self):
        self.click_print("2")

    def button3_clicked(self):
        self.click_print("3")

    def button4_clicked(self):
        self.click_print("4")

    def button5_clicked(self):
        self.click_print("5")

    def button6_clicked(self):
        self.click_print("6")

    def button7_clicked(self):
        self.click_print("7")

    def button8_clicked(self):
        self.click_print("8")

    def button9_clicked(self):
        self.click_print("9")
