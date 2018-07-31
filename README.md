
Status: Revived !!
==================

I have revived this repository from the original author, whom had archived the repository (thanks for the initial work Ryan!)

Ryan has kindly transferred the repository to me and is officially maintained at https://github.com/BrendanSimon/wxanythread

There are other forks hanging around github, but from what I can decipher it seems there are no public commits/branches with any modifications.

My intention is to bring it up to date and to hopefully have it accepted upstream by the wxPython team (hi Robin et al!), possibly as part of the `wx.lib` package.

Initial goals
* Add some simpler functions/decorators to use `wx.CallAfter()`, without blocking and waiting for results
* Make it work with Python 3 and wxPython 4 (aka Phoenix)
* Hopefully find a way to be able to use properties directly (e.g. `self.gauge.Value = 10` instead of `self.gauge.SetValue(10)`)

**==== ORIGINAL wxAnyThread description below ====**

wxAnyThread:  allow methods on wxPython objects to be called from any thread
============================================================================

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

