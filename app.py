import sys
from database import *
from sidebar import Sidebar
from pages import HomePage, NotesPage, FinancePage, HabitsPage
from PySide6.QtWidgets import QWidget, QStackedWidget, QApplication, QMainWindow, QHBoxLayout
                            

class Dashboard(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Life Dashboard")
        self.resize(900, 600)
        
        #Create sidebar
        self.sidebar = Sidebar()

        #Create pages
        home_page = HomePage()
        notes_page = NotesPage()
        finance_page = FinancePage()
        habits_page = HabitsPage()

        #Create stacked widget of tabs
        self.stacked_widget = QStackedWidget()

        self.stacked_widget.addWidget(home_page)
        self.stacked_widget.addWidget(notes_page)
        self.stacked_widget.addWidget(finance_page)
        self.stacked_widget.addWidget(habits_page)

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

def main():

    #Create application instance 
    app = QApplication(sys.argv)

    #Create database
    create_database()

    #Create Dashboard
    dashboard = Dashboard()
    dashboard.show()

    #Open app
    app.exec()

#RUN THIS CODE IF IT IS DIRECTLY RUN FROM HERE (not imports)
if __name__ == "__main__":
    main()

