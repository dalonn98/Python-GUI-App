import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# class MainWindow(QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.setWindowTitle("My App")
#         widget.setPixmap(QPixmap('apple.jpg'))


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Apples")
        widget = QLabel(text="Hello")
        widget.setPixmap(QPixmap(r"/home/jinnlee/python-projects/yohanee/Widgets/apple.jpg"))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

# 참고: https://martinii.fun/192