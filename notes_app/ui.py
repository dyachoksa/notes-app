import wx


class ApplicationFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.SetSize(800, 600)
        self.SetMinSize(wx.Size(600, 500))

        panel = wx.Panel(self)

        self.notes_list_widget = wx.ListBox(panel, style=wx.LB_SINGLE)
        self.notes_list_widget.SetSelection(wx.NOT_FOUND)

        # test item
        self.notes_list_widget.Append("My Note")

        notes_sizer = wx.BoxSizer(wx.VERTICAL)
        notes_sizer.Add(self.notes_list_widget, 1, wx.EXPAND)

        self.title_widget = wx.TextCtrl(panel)
        self.text_widget = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        self.delete_btn = wx.Button(panel, label="Delete")
        self.save_btn = wx.Button(panel, label="Save")

        info_btn = wx.Button(panel, label="Info")
        self.Bind(wx.EVT_BUTTON, self.on_info_btn_click, info_btn)

        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        buttons_sizer.Add(info_btn, 0, 0)
        buttons_sizer.AddSpacer(5)
        buttons_sizer.Add(self.delete_btn, 0, 0)
        buttons_sizer.AddStretchSpacer()
        buttons_sizer.Add(self.save_btn)

        edit_sizer = wx.BoxSizer(wx.VERTICAL)
        edit_sizer.Add(self.title_widget, 0, wx.EXPAND)
        edit_sizer.Add(self.text_widget, 1, wx.ALIGN_TOP | wx.EXPAND | wx.TOP, 10)
        edit_sizer.Add(buttons_sizer, 0, wx.EXPAND | wx.TOP, border=10)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(
            notes_sizer, 2, wx.EXPAND | wx.TOP | wx.LEFT | wx.BOTTOM, border=15
        )
        main_sizer.Add(edit_sizer, 5, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL, border=15)

        panel.SetSizer(main_sizer)

        self.CreateStatusBar()
        self.SetStatusText("Ready")

    def on_info_btn_click(self, event):
        wx.InfoMessageBox(self)
