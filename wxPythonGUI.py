# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Лабораторная 9", pos = wx.DefaultPosition, size = wx.Size( 500,197 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 500,197 ), wx.Size( 500,197 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.wxStaticTextA = wx.StaticText( self, wx.ID_ANY, u"A =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wxStaticTextA.Wrap( -1 )

		bSizer41.Add( self.wxStaticTextA, 0, wx.ALL, 5 )

		self.wxTextCtrlA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.wxTextCtrlA, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.wxStaticTextB = wx.StaticText( self, wx.ID_ANY, u"B =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wxStaticTextB.Wrap( -1 )

		bSizer41.Add( self.wxStaticTextB, 0, wx.ALL, 5 )

		self.wxTextCtrlB = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.wxTextCtrlB, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

		self.wxStaticTextX = wx.StaticText( self, wx.ID_ANY, u"X =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wxStaticTextX.Wrap( -1 )

		bSizer43.Add( self.wxStaticTextX, 0, wx.ALL, 5 )

		self.wxTextCtrlX = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.wxTextCtrlX, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer43, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.wxStaticBitmapMyPrimer = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"_MY_PICTURES/primer17++.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer32.Add( self.wxStaticBitmapMyPrimer, 0, wx.ALL, 5 )


		bSizer21.Add( bSizer32, 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.wxButtonSolve = wx.Button( self, wx.ID_ANY, u"РЕШЕНИЕ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.wxButtonSolve, 0, wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.wxButtonClear = wx.Button( self, wx.ID_ANY, u"ОЧИСТИТЬ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.wxButtonClear, 0, wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.wxButtonExit = wx.Button( self, wx.ID_ANY, u"ВЫХОД", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.wxButtonExit, 0, wx.ALL, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer22, 0, wx.EXPAND, 5 )

		self.wxStaticTextOtvet = wx.StaticText( self, wx.ID_ANY, u"ОТВЕТ =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wxStaticTextOtvet.Wrap( -1 )

		bSizer11.Add( self.wxStaticTextOtvet, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.wxButtonSolve.Bind( wx.EVT_BUTTON, self.wxButtonSolveOnClick )
		self.wxButtonClear.Bind( wx.EVT_BUTTON, self.wxButtonClearOnClick )
		self.wxButtonExit.Bind( wx.EVT_BUTTON, self.wxButtonExitOnClick )

		ico = wx.Icon('_MY_PICTURES/logo.png', wx.BITMAP_TYPE_PNG)
		self.SetIcon(ico)

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def wxButtonSolveOnClick( self, event ):
		event.Skip()

	def wxButtonClearOnClick( self, event ):
		event.Skip()

	def wxButtonExitOnClick( self, event ):
		event.Skip()


