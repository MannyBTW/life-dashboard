from PySide6.QtWidgets import QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
from PySide6.QtCore import Qt
from database import add_note, delete_note, get_notes, update_note, add_habit, delete_habit, get_habits, complete_habit, get_completed_habit_ids, delete_completed_habit
from datetime import date

class HomePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Create layout
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the home page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class NotesPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Create layout
        self.note_layout = QVBoxLayout()

        self.notes = get_notes()
        print(self.notes)

        self.note_title = QLineEdit()
        self.note_body = QTextEdit()
        self.note_list = QListWidget()

        #Load stored notes
        self.load_notes()
        
        self.save_note_button = QPushButton("Save Note")
        self.save_note_button.clicked.connect(self.save_note)

        self.new_note_button = QPushButton("New Note")
        self.new_note_button.clicked.connect(self.new_note)

        self.delete_note_button = QPushButton("Delete Note")
        self.delete_note_button.clicked.connect(self.delete_note)
        self.delete_note_button.setVisible(False)
        
        self.note_layout.addWidget(self.note_title)
        self.note_layout.addWidget(self.note_body)
        self.note_layout.addWidget(self.save_note_button)
        self.note_layout.addWidget(self.new_note_button)
        self.note_layout.addWidget(self.delete_note_button)
        self.note_layout.addWidget(self.note_list)
        self.note_layout.addStretch()

        self.setLayout(self.note_layout)

        #Selecting notes
        self.note_list.currentRowChanged.connect(self.display_note)
    
        
    def load_notes(self):
        #Load titles
        for note in self.notes:
            self.note_list.addItem(note[1])

    def refresh_notes(self, selected_note_id=None):
        #Clear existing notes in note list and refresh from db
        self.note_list.clear()
        self.notes = get_notes()

        #Add notes to UI
        for note in self.notes:
            self.note_list.addItem(note[1])
        
        #Show selected item again, since clearing the note list would 
        #deselect any item
        for row, note in enumerate(self.notes):
            if note[0] == selected_note_id:
                self.note_list.setCurrentRow(row)
                break
        
        
    def save_note(self):
        #Define row, title, and content of the note
        row = self.note_list.currentRow()
        title = self.note_title.text().strip()
        content = self.note_body.toPlainText().strip()

        #Validate if fields are empty, if so return
        if not title or not content:
                print("Title and note content cannot be empty.")
                return

        if row != -1: #If an existing note is selected
            
            selected_note_id = self.notes[row][0]
            #Then save the existing note by updating it in the db
            update_note(self.notes[row][0], title, content)

        else: #If an existing note is not selected (aka, its a new note)

            #Add a new note to the db
            selected_note_id = add_note(title, content)

            print("Note saved!")
            print(self.notes)
        
        #Refresh UI, keeping id of selected item
        self.refresh_notes(selected_note_id)

    def display_note(self, row):
        
        if row != -1:
            self.note_title.setText(self.notes[row][1])
            self.note_body.setText(self.notes[row][2])
            self.delete_note_button.setVisible(True)
        else:
            self.note_title.clear()
            self.note_body.clear()
            self.delete_note_button.setVisible(False)
    
    def new_note(self):
        self.note_title.clear()
        self.note_body.clear()
        self.note_list.setCurrentRow(-1)

    def delete_note(self):
        row = self.note_list.currentRow()
        note_id = self.notes[row][0] 

        delete_note(note_id)
        self.refresh_notes()

        #Clear text boxes if no notes left
        if not self.notes:
            self.note_title.clear()
            self.note_body.clear()
        
  
class FinancePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Create layout
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the finance page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class HabitsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Create layouts
        self.habit_entry_layout = QHBoxLayout()
        self.habits_layout = QVBoxLayout()

        #Create top line
        habit_entry_widget = QWidget()
        habit_entry_widget.setLayout(self.habit_entry_layout)

        self.habit_entry = QLineEdit()
        self.habit_entry_button = QPushButton("Add Habit")
        self.habit_remove_button = QPushButton("Delete Habit")

        self.habit_entry_layout.addWidget(self.habit_entry)
        self.habit_entry_layout.addWidget(self.habit_entry_button)
        self.habit_entry_layout.addWidget(self.habit_remove_button)

        #Add habit and delete habbit buttons
        self.habit_entry_button.clicked.connect(self.enter_habit)
        self.habit_remove_button.clicked.connect(self.remove_habit)

        #Add top line to layout
        self.habits_layout.addWidget(habit_entry_widget)
        self.habits_layout.addStretch()

        #Create list of habits
        self.habit_list = QListWidget()
        
        self.setLayout(self.habits_layout)
        self.habits_layout.addWidget(self.habit_list)

        #Create signal for checked box
        self.habit_list.itemChanged.connect(self.finish_habit)

        #Load habits
        self.refresh_habits()


    def enter_habit(self):
        add_habit(self.habit_entry.text())
        self.refresh_habits()

        self.habit_entry.clear()
    
    def remove_habit(self):
        row = self.habit_list.currentRow()
        habits = get_habits()
        delete_habit(habits[row][0])
        print("Habit deleted")

        self.refresh_habits()
        

    def refresh_habits(self):
        today = date.today().isoformat()
        completed_ids = get_completed_habit_ids(today)

        # Prevent itemChanged from firing while rebuilding the list
        self.habit_list.blockSignals(True)

        self.habit_list.clear()

        for habit in get_habits():
            habit_id = habit[0]
            habit_name = habit[1]

            item = QListWidgetItem(habit_name)

            # Store the database ID inside the list item
            item.setData(Qt.ItemDataRole.UserRole, habit_id)

            # Make the item checkable
            item.setFlags(
                item.flags() | Qt.ItemFlag.ItemIsUserCheckable
            )

            if habit_id in completed_ids:
                item.setCheckState(Qt.CheckState.Checked)
            else:
                item.setCheckState(Qt.CheckState.Unchecked)

            self.habit_list.addItem(item)

        self.habit_list.blockSignals(False)
    
    def finish_habit(self, item):
        if item.checkState() == Qt.CheckState.Checked and item.data(Qt.ItemDataRole.UserRole) not in get_completed_habit_ids(str(date.today().isoformat())):
            complete_habit(item.data(Qt.ItemDataRole.UserRole), date.today().isoformat())
            print("Completed habit")
        elif item.checkState() == Qt.CheckState.Unchecked:
            delete_completed_habit(item.data(Qt.ItemDataRole.UserRole), date.today().isoformat())

        






        