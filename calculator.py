from __future__ import division
import wx
from math import *


class Calculator(wx.Dialog):
    
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Calculator")
        sizer = wx.BoxSizer(wx.VERTICAL)


        self.display = wx.ComboBox(self, -1)
        sizer.Add(self.display, 0, wx.EXPAND)
        

        gsizer = wx.GridSizer(4, 4, 4)
        for row in (("7", "8", "9", "/"),
                    ("4", "5", "6", "*"),
                    ("1", "2", "3", "-"),
                    ("0", ".", "C", "+")):
            for label in row:
                b = wx.Button(self, -1, label)
                gsizer.Add(b)
                self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(gsizer, 1, wx.EXPAND)

        b = wx.Button(self, -1, "=")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
        sizer.Add(b, 0, wx.EXPAND)
        self.equal = b

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.CenterOnScreen()
        
        
    def OnButton(self, evt):
        label = evt.GetEventObject().GetLabel()

        if label == "=":
            try:
                compute = self.display.GetValue()

                if not compute.strip():
                    return

                result = eval(compute)

                self.display.Insert(compute, 0)

                self.display.SetValue(str(result))
            except e:
                wx.LogError(str(e))
                return

        elif label == "C":
            self.display.SetValue(" ")

        else:
            self.display.SetValue(self.display.GetValue() + label)
            self.equal.SetFocus()


if __name__ == "__main__":
        
    app = wx.App()
    dlg = Calculator()
    dlg.ShowModal()
    dlg.Destroy()       
