import sys

import wx

from notes_app import NotesService, ApplicationFrame

app = wx.App()

database = None
if len(sys.argv) > 1:
    database = sys.argv[1]

# service layer
notes_service = NotesService(database)
notes_service.load_notes()

# Application main window
frm = ApplicationFrame(notes_service, None, title="Notes App")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
