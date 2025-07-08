from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
)
from PySide6.QtGui import QFont


class NumberPad(QWidget):
    def __init__(self) -> None:
        FONT = QFont("Arial", 18, QFont.Weight.Bold)

        WINDOW_WIDTH = 300
        WINDOW_HEIGHT = 300

        BUTTON_WIDTH = 60
        BUTTON_HEIGHT = 60

        super().__init__()

        self.setWindowTitle("Numbers Grid")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        layout = QGridLayout()
        labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        positions = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 1),
        ]

        for label, (row, column) in zip(labels, positions):
            button = QPushButton(label)
            button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            button.setFont(FONT)
            button.setStyleSheet(
                """
                QPushButton {
                    background-color: #3820d0;
                    color: white;
                    font-size: 18px;
                    font-family: "Comic Sans MS";
                    border: 4px solid #d020b0;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #FF5733;
                }
                QPushButton:pressed {
                    background-color: #20d02a;
                }
                """
            )
            button.clicked.connect(lambda _, text=label: self.click_print(text))

            layout.addWidget(button, row, column)

        self.setLayout(layout)

    @staticmethod
    def click_print(prompt: str | int) -> None:
        print(prompt, end="", flush=True)
