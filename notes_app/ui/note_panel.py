import typing
import wx

from notes_app.models import Note
from notes_app.services import NotesService


class NotePanel(wx.Panel):
    def __init__(self, notes_service: NotesService, main_frame, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._note: typing.Optional[Note] = None
        self.main_frame: "ApplicationFrame" = main_frame

        self.notes_service = notes_service
        self.setup_ui()

    def setup_ui(self):
        self.title_widget = wx.TextCtrl(self)
        self.text_widget = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        delete_btn = wx.Button(self, label="Delete")
        self.Bind(wx.EVT_BUTTON, self.on_delete, delete_btn)

        save_btn = wx.Button(self, label="Save")
        self.Bind(wx.EVT_BUTTON, self.on_save, save_btn)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        buttons_sizer.Add(delete_btn, 0, 0)
        buttons_sizer.AddStretchSpacer()
        buttons_sizer.Add(save_btn)

        edit_sizer = wx.BoxSizer(wx.VERTICAL)
        edit_sizer.Add(wx.StaticText(self, label="Title"), 0)
        edit_sizer.Add(self.title_widget, 0, wx.EXPAND | wx.TOP, border=5)
        edit_sizer.Add(wx.StaticText(self, label="Content"), 0, wx.TOP, border=10)
        edit_sizer.Add(self.text_widget, 1, wx.ALIGN_TOP | wx.EXPAND | wx.TOP, 5)
        edit_sizer.Add(buttons_sizer, 0, wx.EXPAND | wx.TOP, border=10)

        self.SetSizer(edit_sizer)

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note: Note):
        self._note = note
        self.title_widget.SetValue(note.title)
        self.text_widget.SetValue(note.content)

    def on_delete(self, event):
        self.notes_service.delete(self._note)
        self.main_frame.on_note_delete()

    def on_save(self, event):
        self._note.title = self.title_widget.GetValue()
        self._note.content = self.text_widget.GetValue()

        if not self._note.title or not self._note.content:
            alert = wx.MessageDialog(self, "Note can't be empty", "Warning", wx.OK | wx.ICON_EXCLAMATION)
            return alert.ShowModal()

        if self._note.id is None:
            self.notes_service.create(self._note)
        else:
            self.notes_service.update(self._note)

        self.main_frame.update_notes()

        # evt = NoteUpdatedEvent(note=self._note)
        # wx.PostEvent(self.GetParent(), evt)
