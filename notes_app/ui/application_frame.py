import wx

from notes_app.models import Note
from notes_app.services import NotesService

from .note_panel import NotePanel


class ApplicationFrame(wx.Frame):
    def __init__(self, notes_service: NotesService, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.notes_service = notes_service

        self.setup_ui()
        self.update_notes()

        if self.notes_service.notes:
            self.set_active(0)
        else:
            self.note_panel.note = Note()

    def setup_ui(self):
        self.SetSize(800, 600)
        self.SetMinSize(wx.Size(600, 500))

        panel = wx.Panel(self)

        self.notes_list_widget = wx.ListBox(panel, style=wx.LB_SINGLE)
        self.notes_list_widget.SetSelection(wx.NOT_FOUND)
        self.Bind(wx.EVT_LISTBOX, self.on_note_changed, self.notes_list_widget)

        info_btn = wx.Button(panel, label="Info")
        self.Bind(wx.EVT_BUTTON, self.on_info_btn_click, info_btn)

        create_btn = wx.Button(panel, label="Create")
        self.Bind(wx.EVT_BUTTON, self.on_note_add, create_btn)

        self.note_panel = NotePanel(self.notes_service, self, panel)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer1.Add(info_btn, 0, 0)
        sizer1.AddStretchSpacer()
        sizer1.Add(create_btn, 0, 0)

        notes_sizer = wx.BoxSizer(wx.VERTICAL)
        notes_sizer.Add(self.notes_list_widget, 1, wx.EXPAND)
        notes_sizer.Add(sizer1, 0, wx.EXPAND | wx.TOP, 10)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(
            notes_sizer, 2, wx.EXPAND | wx.TOP | wx.LEFT | wx.BOTTOM, border=15
        )
        main_sizer.Add(
            self.note_panel, 5, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL, border=15
        )

        panel.SetSizer(main_sizer)

        self.CreateStatusBar()
        self.SetStatusText("Ready")

    def update_notes(self):
        self.notes_list_widget.Clear()

        for title in self.notes_service.get_titles():
            self.notes_list_widget.Append(title)

    def set_active(self, idx: int):
        note = self.notes_service.notes[idx]
        self.notes_list_widget.SetSelection(idx)
        self.note_panel.note = note

    def on_note_changed(self, event):
        note_title = event.GetString()
        note = self.notes_service.get_by_title(note_title)
        self.note_panel.note = note

    def on_note_add(self, event):
        self.notes_list_widget.SetSelection(wx.NOT_FOUND)
        self.note_panel.note = Note()

    def on_note_updated(self, event):
        print(event)

    def on_note_delete(self):
        self.update_notes()
        self.set_active(0)

    def on_info_btn_click(self, event):
        wx.InfoMessageBox(self)
