class Note:
    def __init__(self, note_id=None, title=None, content=None):
        self.id = note_id
        self.title = title
        self.content = content

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Note id={self.id} title={self.title}>"
