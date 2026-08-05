import sys
from sidebar import Sidebar
from PySide6.QtWidgets import QWidget, QStackedWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout
                            

class Dashboard(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Life Dashboard")
        self.resize(900, 600)
        
        #Create sidebar
        self.sidebar = Sidebar()

        #Create stacked widget of tabs
        home_widget = QWidget()
        notes_widget = QWidget()
        finance_widget = QWidget()
        habits_widget = QWidget()

        self.stacked_widget = QStackedWidget()

        self.stacked_widget.addWidget(home_widget)
        self.stacked_widget.addWidget(notes_widget)
        self.stacked_widget.addWidget(finance_widget)
        self.stacked_widget.addWidget(habits_widget)

        #Create layouts for individual widgets
        home_layout = QVBoxLayout()
        notes_layout = QVBoxLayout()
        finance_layout = QVBoxLayout()
        habits_layout = QVBoxLayout()
        

        #Create labels for each widget page
        home_label = QLabel("This is the home page")
        home_layout.addWidget(home_label)
        notes_label = QLabel("This is the notes page")
        notes_layout.addWidget(notes_label)
        finance_label = QLabel("This is the finance page")
        finance_layout.addWidget(finance_label) 
        habits_label = QLabel("This is the habits page")
        habits_layout.addWidget(habits_label)

        #Set layouts of individual pages
        home_widget.setLayout(home_layout)
        notes_widget.setLayout(notes_layout)
        finance_widget.setLayout(finance_layout)
        habits_widget.setLayout(habits_layout)

        #Connect buttons to respective tabs
        self.sidebar.buttons['home'].clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.sidebar.buttons['notes'].clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.sidebar.buttons['finance'].clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.sidebar.buttons['habits'].clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        #Put all widgets in screen layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget, 1)

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