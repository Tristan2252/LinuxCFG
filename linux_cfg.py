#!/bin/usr/env python3

import back_end
import window

try:
    from gi.repository import Gtk
    window.run()
except ImportError:
    back_end.OldFile()
