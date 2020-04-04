import wx

from notes_app import ApplicationFrame

app = wx.App()

# Application main window
frm = ApplicationFrame(None, title="Notes App")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
