import json
import typing

from .models import Note


class NotesService:
    def __init__(self, database: str = "notes.json"):
        self.notes: typing.List[Note] = []
        self.database = database

    def load_notes(self) -> typing.List[Note]:
        """Loads notes from JSON database file"""
        with open(self.database, "r") as f:
            notes = json.load(f)

        for note in notes:
            if len(note["title"]) == 0:
                continue

            self.notes.append(Note(**note))

        return self.notes

    def save_notes(self):
        """Stores notes in JSON database file"""
        pass

    def get_titles(self) -> typing.Iterator[str]:
        return map(lambda x: x.title, self.notes)

    def get_by_title(self, title: str) -> typing.Optional[Note]:
        pass

    def update(self, note: Note) -> bool:
        return True

    def delete(self):
        pass

    def create(self, title, content):
        pass
