from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QPushButton


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

        self.notes = []

        self.note_title = QLineEdit()
        self.note_body = QTextEdit()
        self.note_list = QListWidget()
        
        self.save_note_button = QPushButton("Save Note")
        self.save_note_button.clicked.connect(self.save_note)

        self.new_note_button = QPushButton("New Note")
        self.new_note_button.clicked.connect(self.new_note)

        self.note_layout.addWidget(self.note_title)
        self.note_layout.addWidget(self.note_body)
        self.note_layout.addWidget(self.save_note_button)
        self.note_layout.addWidget(self.new_note_button)
        self.note_layout.addWidget(self.note_list)
        self.note_layout.addStretch()

        self.setLayout(self.note_layout)

        #Selecting notes
        self.note_list.currentRowChanged.connect(self.display_note)
            



    def save_note(self):
 
            if self.note_list.currentRow() != -1: #If an existing note is selected
                row = self.note_list.currentRow() 
                note = self.notes[row] #Get that note in order to modify it
                note['title'] = self.note_title.text()
                note['content'] = self.note_body.toPlainText()
            else: #If an existing note is not selected
                title = self.note_title.text() #Get text of title and content
                content = self.note_body.toPlainText()

                if not title or not content: #Return if empty 
                    print("Title and note content cannot be empty.")
                    return

                if self.notes: #If a note exists
                    note_id = max(note['id'] for note in self.notes) + 1 #Make this a new note
                else: #If no note exists then start the ids at 1
                    note_id = 1

                note = {
                    "title": title,
                    "content": content,
                    "id": note_id
                }

                self.notes.append(note)
                self.note_list.addItem(note["title"])

                self.note_title.clear()
                self.note_body.clear()

                print("Note saved!")
                print(self.notes)

        
   
    
    def display_note(self, row):
        
        if row != -1:
            self.note_title.setText(self.notes[row]['title'])
            self.note_body.setText(self.notes[row]['content'])
        else:
            self.note_title.clear()
            self.note_body.clear()
    
    def new_note(self):
        self.note_title.clear()
        self.note_body.clear()
        self.note_list.setCurrentRow(-1)
        
        

    
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

        #Create layout
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the habits page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        