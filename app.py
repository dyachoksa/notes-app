import wx

from notes_app import ApplicationFrame, NotesService

app = wx.App()

# service layer
notes_service = NotesService()
notes_service.load_notes()

# Application main window
frm = ApplicationFrame(notes_service, None, title="Notes App")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
