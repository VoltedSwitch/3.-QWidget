from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
)


class NumberPad(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Numbers Grid")
        self.setFixedSize(300, 300)

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
            button.clicked.connect(lambda _, text=label: self.click_print(text))
            layout.addWidget(button, row, column)

        self.setLayout(layout)

    @staticmethod
    def click_print(prompt: str | int) -> None:
        print(prompt, end="", flush=True)
