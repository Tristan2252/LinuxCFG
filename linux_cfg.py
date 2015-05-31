import back_end
import window

try:
    from gi.repository import Gtk
    window.run()
except ImportError:
    back_end.OldFile()
