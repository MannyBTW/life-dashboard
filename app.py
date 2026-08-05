import sys
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout
                            

class Dashboard(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Life Dashboard")
        self.resize(900, 600)

        #Create sidebar buttons
        self.home_button = QPushButton("Home")
        self.notes_button = QPushButton("Notes")
        self.finance_button = QPushButton("Finance")
        self.habits_button = QPushButton("Habits")

        #Create sidebar layout
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.home_button)
        sidebar_layout.addWidget(self.notes_button)
        sidebar_layout.addWidget(self.finance_button)
        sidebar_layout.addWidget(self.habits_button)
        sidebar_layout.addStretch()
        
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)

        #Create content widget
        self.content_label = QLabel("WELCOME")
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.content_label)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        #Put all widgets in screen layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(content_widget, 1)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        

#Create application instance 
app = QApplication(sys.argv)

#Create Dashboard
dashboard = Dashboard()
dashboard.show()

#Open app
app.exec()