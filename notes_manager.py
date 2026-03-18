import json
from datetime import datetime

FILE_PATH = "data/notes.json"


class NotesManager:

    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(FILE_PATH, "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, content):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notes.append(note)
        self.save_notes()
        print("Note added successfully!")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        for note in self.notes:
            print("\nID:", note["id"])
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Created:", note["created"])


# MENU FUNCTION (write this BELOW the class)

def notes_menu():

    manager = NotesManager()

    while True:

        print("\n------ Notes Manager ------")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.view_notes()

        elif choice == "2":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            manager.add_note(title, content)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")