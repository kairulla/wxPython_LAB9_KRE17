#!/usr/bin/env python3
# coding=utf-8
import sys

import wx
import wx.xrc
import math

from wxPythonGUI import MainFrame


class MainFrame(MainFrame):

    def wxButtonSolveOnClick(self, event):
        try:
            a = float(self.wxTextCtrlA.GetValue())
            b = float(self.wxTextCtrlB.GetValue())
            x = float(self.wxTextCtrlX.GetValue())
            if x > 6:
                y = (6 * x * x - a * b) / (2 * x * x)
            else:
                y = 4 * (x + a * a + b * b)
            if math.isnan(y):
                self.wxStaticTextOtvet.SetLabelText("Нет решения")
            elif math.isinf(y):
                self.wxStaticTextOtvet.SetLabelText("Бесконечность")
            else:
                self.wxStaticTextOtvet.SetLabelText(str(format(y, '.2f')))
        except:
            self.wxStaticTextOtvet.SetLabelText("не могу понять тебя!")

    def wxButtonClearOnClick(self, event):
        self.wxTextCtrlA.SetLabelText("")
        self.wxTextCtrlB.SetLabelText("")
        self.wxTextCtrlX.SetLabelText("")
        self.wxStaticTextOtvet.SetLabelText("Ответ =")

    def wxButtonExitOnClick(self, event):
        sys.exit()


def main():
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
    # поставить в __init__
    # ico = wx.Icon('_MY_PICTURES/logo.png', wx.BITMAP_TYPE_PNG)
    # self.SetIcon(ico)


if __name__ == '__main__':
    main()
