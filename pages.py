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



    def save_note(self):
 
            if self.note_list.currentRow() != -1: #If an existing note is selected
                row = self.note_list.currentRow() 
                note = self.notes[row] #Get that note in order to modify it

                if not self.note_title.text() or not self.note_body.toPlainText(): #Return if empty 
                    print("Title and note content cannot be empty.")
                    return

                note['title'] = self.note_title.text()
                note['content'] = self.note_body.toPlainText()

                self.note_list.currentItem().setText(note["title"])
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
        
        self.note_list.takeItem(row)
        del self.notes[row]

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

        #Create layout
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the habits page")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        