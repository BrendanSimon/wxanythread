
  wxAnyThread:  allow methods on wxPython objects to be called from any thread

In wxPython, methods that alter the state of the GUI are only safe to call from
the thread running the main event loop.  Other threads must typically post
events to the GUI thread instead of invoking methods directly.

While there are builtin shortcuts for this (e.g. wx.CallAfter) they do not
capture the full semantics of a function call.  This module provides an easy
way to invoke methods from any thread *transparently*, propagating return
values and exceptions back to the calling thread.

The main interface is a decorator named "anythread", which can be applied
to methods to make them safe to call from any thread, like so:

  class MyFrame(wx.Frame):

     @anythread
     def GetSomeData():
         dlg = MyQueryDialog(self,"Enter some data")
         if dlg.ShowModal() == wx.ID_OK:
             resp = dlg.GetResponse()
             return int(resp)
         else:
             raise NoDataEnteredError()

The GetSomeData method can now be directly invoked from any thread.
The calling thread will block while the main GUI thread shows the dialog,
and will then receive a return value or exception as appropriate.

