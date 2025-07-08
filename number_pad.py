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
        # Define
        FONT = QFont("Arial", 18, QFont.Weight.Bold)

        WINDOW_WIDTH = 300
        WINDOW_HEIGHT = 300

        BUTTON_WIDTH = 60
        BUTTON_HEIGHT = 60

        BOTTOM_ROW = 3
        FIRST_LEFT_COLUMN = 0
        ROW_SPAN = 1
        COLUMN_SPAN = 3

        STYLE = """
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

        super().__init__()

        self.setWindowTitle("Numbers Grid")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        grid_layout = QGridLayout()
        bottom_row_layout = QHBoxLayout()

        main_button_labels = range(1, 10)
        bottom_button_labels = ["0", "🗑️"]

        main_button_positions = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]

        # Create main buttons
        for main_button_label, (row, column) in zip(
            main_button_labels, main_button_positions
        ):
            main_button = QPushButton(str(main_button_label))
            main_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            main_button.setFont(FONT)
            main_button.setStyleSheet(STYLE)
            main_button.clicked.connect(self.make_click_handler(main_button_label))

            grid_layout.addWidget(main_button, row, column)

        # Create bottom buttons
        for bottom_button_label in bottom_button_labels:
            bottom_button = QPushButton(bottom_button_label)
            bottom_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            bottom_button.setFont(FONT)
            bottom_button.setStyleSheet(STYLE)
            bottom_button.clicked.connect(self.make_click_handler(bottom_button_label))
            bottom_row_layout.addWidget(bottom_button)

        # Add the button_row_layout to the grid layout at the bottom row, spanning all columns
        grid_layout.addLayout(
            bottom_row_layout, BOTTOM_ROW, FIRST_LEFT_COLUMN, ROW_SPAN, COLUMN_SPAN
        )

        self.setLayout(grid_layout)

    def make_click_handler(self, text):
        return lambda _: self.click_print(text)

    @staticmethod
    def click_print(text: str | int) -> None:
        print(text, end="", flush=True)
