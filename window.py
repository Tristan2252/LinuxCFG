#!/usr/bin/env python3

import os
import sys
import back_end
from dialog import AppDialog, PycharmDialog, PPADialog
from gi.repository import Gtk


back_end.TestTerminal()

class LinuxProgram(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Linux CFG {}".format(back_end.Version))

        # ++++++++++++++++++++ Window Setup ++++++++++++++++++++++++++++++++++++++++
        self.set_default_size(600, 600)  # sets window size
        self.main_box = Gtk.Box(True)
        self.table = Gtk.Table(10, 7, True)  # int (row), int (column), Fit widget
        self.add(self.main_box)
        self.main_box.add(self.table)

        # ++++++++++++++++++++++ Buttons +++++++++++++++++++++++++++++++++++++++++++
        self.update_bttn = Gtk.Button("Update")
        self.update_bttn.connect("clicked", self.on_update_clicked)

        self.pycharm_bttn = Gtk.Button("Pycharm")
        self.pycharm_bttn.connect("clicked", self.on_pycharm_clicked)

        self.webmin_bttn = Gtk.Button("Webmin")
        self.webmin_bttn.connect("clicked", self.on_webmin_clicked)

        self.common_bttn = Gtk.Button("Common App's")
        self.common_bttn.connect("clicked", self.on_common_clicked)

        self.gnome_ppa_bttn = Gtk.Button("Gnome PPA")
        self.gnome_ppa_bttn.connect("clicked", self.on_gnome_ppa_clicked)

        self.exit_bttn = Gtk.Button("Exit")
        self.exit_bttn.connect("clicked", Gtk.main_quit)  # exits Gtk app

        # +++++++++++++++++++ Table Attachments ++++++++++++++++++++++++++++++++++++
        # table.attach syntax: object, left, right, top, bottom, xpadding, ypadding
        # left side of app
        self.table.attach(Gtk.Label("Linux Updates\n and Upgrades"), 1, 3, 1, 2)
        self.table.attach(self.update_bttn, 1, 3, 2, 3, ypadding=5)
        self.table.attach(Gtk.Label("Install Pycharm IDE"), 1, 3, 3, 4)
        self.table.attach(self.pycharm_bttn, 1, 3, 4, 5, ypadding=5)
        self.table.attach(Gtk.Label("Install Webmin Server"), 1, 3, 5, 6, )
        self.table.attach(self.webmin_bttn, 1, 3, 6, 7, ypadding=5)

        # right side of app
        self.table.attach(Gtk.Label("Install Common App's"), 4, 6, 1, 2)
        self.table.attach(self.common_bttn, 4, 6, 2, 3, ypadding=5)
        self.table.attach(Gtk.Label("Add Gnome Staging PPA"), 4, 6, 3, 4)
        self.table.attach(self.gnome_ppa_bttn, 4, 6, 4, 5, ypadding=5)

        # exit button (bottom right)
        self.table.attach(self.exit_bttn, 6, 7, 9, 10, xpadding=10, ypadding=10)

    @staticmethod  # static method dose not use self fyi
    def on_update_clicked(widget):
        """
        Runs linux update and upgrade
        :param widget:
        :return: None
        """
        update_obj = back_end.Update()
        update_obj.do_update()

    @staticmethod
    def on_webmin_clicked(widget):
        """
        Function runs install method from back_end.webmin
        :param widget:
        :return:None
        """
        webmin = back_end.Webmin()
        webmin.install()

    def on_pycharm_clicked(self, widget):
        """
        Creates PycharmDialog object and grabs text from dialog entry when
        OK is clicked
        :param widget:
        :return: None
        """
        version_dialog = PycharmDialog(self)
        response = version_dialog.run()

        if response == Gtk.ResponseType.OK:
            version = version_dialog.ver_entry.get_text()  # grabs text when OK is clicked
            location = version_dialog.loc_entry.get_text()
            pycharm = back_end.Pycharm(version, location)
            pycharm.install()

        version_dialog.destroy()

    def on_common_clicked(self, widget):
        """
        Common applications window used to select common applications to install
        :param widget:
        :return: None
        """
        common_app_window = AppDialog(self)
        response = common_app_window.run()

        if response == Gtk.ResponseType.OK:  # ran if OK button is pressed
            common_app_window.install()  # installs applications added to common_app_window object

        common_app_window.destroy()

    def on_gnome_ppa_clicked(self, widget):
        """
        Runs dialog to prompt user for adding Gnome staging PPA and also asks user
        if they want to upgrade after adding PPA
        :param widget:
        :return: None
        """
        gnome_update = PPADialog(self)
        update_response = gnome_update.run()

        ppa = back_end.GnomePPA()

        if update_response == Gtk.ResponseType.YES:
            ppa.run_upgrade()  # runs add PPA and upgrade

        if update_response == Gtk.ResponseType.NO:
            ppa.add_ppa()

        gnome_update.destroy()

def run():
    if back_end.Debug:
        # Running program without root for convenience

        # old_file = back_end.OldFile()
        # old_file.run_old_file()
        win = LinuxProgram()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    else:
        # following code taken from
        # http://stackoverflow.com/questions/5222333/authentication-in-python-script-to-run-as-root
        # tests if the program is running as root, needs to run as root, needs to run as root to
        # execute sudo commands
        euid = os.geteuid()
        if euid != 0:
            print("Program not started as root. Running sudo..")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            # the next line replaces the currently-running process with the sudo
            os.execlpe('sudo', *args)

        print('Running as root successful!!')

        win = LinuxProgram()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

        ##############################################################################################
        # Sources                                                                                    #
        # http://askubuntu.com/questions/85162/how-can-i-change-the-wallpaper-using-a-python-script  #
        # GTK Python Doc's:                                                                          #
        # - https://python-gtk-3-tutorial.readthedocs.org/en/latest/index.html                       #
        # - http://learngtk.org/tutorials/python_gtk3_tutorial/html/index.html                       #
        ##############################################################################################
