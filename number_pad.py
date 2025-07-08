from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
)
from PySide6.QtGui import QFont


class NumberPad(QWidget):
    def __init__(self) -> None:
        # Set up
        FONT = QFont("Arial", 18, QFont.Weight.Bold)

        WINDOW_WIDTH = 300
        WINDOW_HEIGHT = 300

        BUTTON_WIDTH = 60
        BUTTON_HEIGHT = 60

        BOTTOM_ROW = 3
        FIRST_LEFT_COLUMN = 0
        ROW_SPAN = 1
        COLUMN_SPAN = 3

        DISPLAY_HEIGHT = 40

        DISPLAY_STYLE = "font-size: 20px;"
        BUTTON_STYLE = """
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

        self.display = QLineEdit()

        self.display.setReadOnly(True)  # Prevents typing it into manually
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setStyleSheet(DISPLAY_STYLE)

        self.setWindowTitle("Numbers Grid")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        main_layout = QVBoxLayout()
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

        # Create main grid buttons
        for main_button_label, (row, column) in zip(
            main_button_labels, main_button_positions
        ):
            main_button = QPushButton(str(main_button_label))
            main_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            main_button.setFont(FONT)
            main_button.setStyleSheet(BUTTON_STYLE)
            main_button.clicked.connect(self.make_click_handler(main_button_label))

            grid_layout.addWidget(main_button, row, column)

        # Create bottom grid buttons
        for bottom_button_label in bottom_button_labels:
            bottom_button = QPushButton(bottom_button_label)
            bottom_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
            bottom_button.setFont(FONT)
            bottom_button.setStyleSheet(BUTTON_STYLE)
            bottom_button.clicked.connect(self.make_click_handler(bottom_button_label))

            bottom_row_layout.addWidget(bottom_button)

        # Add the button_row_layout to the grid layout at the bottom row, spanning all columns
        grid_layout.addLayout(
            bottom_row_layout, BOTTOM_ROW, FIRST_LEFT_COLUMN, ROW_SPAN, COLUMN_SPAN
        )
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def make_click_handler(self, label):
        return lambda _, text=label: (
            self.display.setText(self.display.text()[:-1])
            if text == "🗑️"
            else self.click_display(text)
        )

    def click_display(self, text: str | int) -> None:
        self.display.setText(self.display.text() + str(text))
