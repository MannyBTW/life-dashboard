from PySide6.QtWidgets import QWidget, QStackedWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout

class Sidebar(QWidget):
    

    def __init__(self, parent=None):
        super().__init__(parent)

        #Create sidebar buttons
    
        self.buttons = {
            "home": QPushButton("Home"),
            "notes": QPushButton("Notes"),
            "finance": QPushButton("Finance"),
            "habits": QPushButton("Habits")
        }

        #Create sidebar layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.buttons['home'])
        sidebar_layout.addWidget(self.buttons['notes'])
        sidebar_layout.addWidget(self.buttons['finance'])
        sidebar_layout.addWidget(self.buttons['habits'])
        sidebar_layout.addStretch()

        self.setLayout(sidebar_layout)