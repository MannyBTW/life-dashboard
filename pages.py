from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class HomePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("This is the home page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class NotesPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("This is the notes page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class FinancePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("This is the finance page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class HabitsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.label = QLabel("This is the habits page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        