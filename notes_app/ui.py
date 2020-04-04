import wx


class ApplicationFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        panel = wx.Panel(self)

        self.notesListWidget = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.notesListWidget.AppendColumn("ID")
        self.notesListWidget.AppendColumn("Title")

        self.textWidget = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        self.deleteBtn = wx.Button(panel, label="Delete")
        self.saveBtn = wx.Button(panel, label="Save")

        info_btn = wx.Button(panel, label="Info")
        self.Bind(wx.EVT_BUTTON, self.on_info_btn_click, info_btn)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        buttons_sizer.Add(info_btn, 0, wx.LEFT)
        buttons_sizer.Add(self.deleteBtn, 0, wx.ALIGN_LEFT)
        buttons_sizer.Add(self.saveBtn, 0, wx.ALIGN_RIGHT)

        edit_sizer = wx.BoxSizer(wx.VERTICAL)
        edit_sizer.Add(self.textWidget, 1, wx.ALIGN_TOP | wx.EXPAND)
        edit_sizer.Add(buttons_sizer, 0, wx.ALIGN_BOTTOM)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.notesListWidget, 0, wx.ALIGN_LEFT)
        main_sizer.Add(edit_sizer, 1, wx.ALIGN_RIGHT | wx.EXPAND)

        panel.SetSizer(main_sizer)

        self.CreateStatusBar()
        self.SetStatusText("Ready")

    def on_info_btn_click(self, event):
        wx.InfoMessageBox(self)
