import wx.lib.newevent

from .application_frame import ApplicationFrame

NoteUpdatedEvent, EVT_NOTE_UPDATED = wx.lib.newevent.NewEvent()

__all__ = ["ApplicationFrame"]
