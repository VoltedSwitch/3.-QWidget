from PySide6.QtWidgets import QApplication
from number_pad import NumberPad

import sys

app = QApplication(sys.argv)
window = NumberPad()
window.show()

app.exec()
