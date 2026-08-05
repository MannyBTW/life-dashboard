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

        self.note_layout.addWidget(self.note_title)
        self.note_layout.addWidget(self.note_body)
        self.note_layout.addWidget(self.save_note_button)
        self.note_layout.addWidget(self.note_list)
        self.note_layout.addStretch()

        self.setLayout(self.note_layout)

        #Selecting notes
        self.note_list.currentRowChanged.connect(self.display_note)
            



    def save_note(self):
        
        #Get text of title and content
        title = self.note_title.text()
        content = self.note_body.toPlainText()
        if self.notes:
            note_id = max(note['id'] for note in self.notes) + 1
        else:
            note_id = 0

        note = {
            "title": title,
            "content": content,
            "id": note_id
        }

        if not title or not content:
            print("Title and note content cannot be empty.")
            return

        self.notes.append(note)
        self.note_list.addItem(note["title"])

        self.note_title.clear()
        self.note_body.clear()

        print("Note saved!")
        print(self.notes)
    
    def display_note(self):
        
        self.note_title.setText(self.notes[self.note_list.currentRow()]['title'])
        self.note_body.setText(self.notes[self.note_list.currentRow()]['content'])

        
        

    
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
        