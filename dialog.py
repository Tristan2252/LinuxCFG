from gi.repository import Gtk
import back_end


class AppDialog(Gtk.Dialog):

    def __init__(self, parent):
        self.run_common_apps = back_end.CommonApps()

        Gtk.Dialog.__init__(self, "Linux CFG", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self._common_app_lst = ["gedit", "ubuntu-restricted-extras", "chromium-browser", "preload",
                                "icedtea-7-plugin openjdk-7-jre", "openjdk-7-jdk", "gnome-terminal",
                                "pepperflashplugin-nonfree", "tmux", "vim", "htop", "git",
                                "pipelight-multi"]
        self._ssh = "ssh"
        self._atom = "atom"
        self._play_on_linux = "playonlinux"

        # ++++++++++++++++++++ Window Setup ++++++++++++++++++++++++++++++++++++++++ #
        self.set_default_size(550, 500)  # sets window size
        box = self.get_content_area()
        self.table = Gtk.Table(7, 7, True)  # int (row), int (column), Fit widget

        # ++++++++++++++++++++ Checkboxes ++++++++++++++++++++++++++++++++++++++++++ #
        self.ssh_ckbox = Gtk.CheckButton(self._ssh)
        self.ssh_ckbox.connect("clicked", self.add_app, self._ssh)
        self.atom_ckbox = Gtk.CheckButton(self._atom)
        self.atom_ckbox.connect("clicked", self.add_app, self._atom)
        self.play_on_linux_ckbox = Gtk.CheckButton(self._play_on_linux)
        self.play_on_linux_ckbox.connect("clicked", self.add_app, self._play_on_linux)
        self.common_app_ckbox = Gtk.CheckButton("Common Applications")
        self.common_app_ckbox.connect("clicked", self.add_common_apps)

        # ++++++++++++++++++++ Window Labels +++++++++++++++++++++++++++++++++++++++ #
        self.label = Gtk.Label("Common Applications Installs:\n"
                               "gedit, ubuntu-restricted-extras, chromium-browser, preload,\n"
                               "icedtea-7-plugin openjdk-7-jre, openjdk-7-jdk, gnome-terminal,\n"
                               "pepperflashplugin-nonfree, tmux, vim, htop, and git")
        header = Gtk.Label("Select Applications to Install")

        # ++++++++++++++++++++ Table Setup +++++++++++++++++++++++++++++++++++++++++ #
        # table.attach syntax: object, left, right, top, bottom, xpadding, ypadding
        self.table.attach(self.ssh_ckbox, 1, 4, 1, 2, ypadding=10)
        self.table.attach(self.atom_ckbox, 1, 4, 2, 3, ypadding=10)
        self.table.attach(self.play_on_linux_ckbox, 1, 4, 3, 4, ypadding=10)
        self.table.attach(self.common_app_ckbox, 1, 4, 4, 5, ypadding=10)
        self.table.attach(self.label, 1, 6, 5, 7, ypadding=10)

        box.add(header)
        box.add(self.table)
        self.show_all()

    def add_app(self, widget, app):
        """
        function add app to list of apps to be installed when user is done selecting them
        :param app: str # name of app to be installed
        :param widget:
        :return: None
        """
        self.run_common_apps.add_apps(app)

    def add_common_apps(self, widget):
        """
        function iterates through each app in common apps list while adding that app to the
        list of apps to be installed when user is done.
        :param widget:
        :return:None
        """
        for app in self._common_app_lst:
            self.add_app(self, app)

    def install(self):
        """
        ran by front end to install all apps added to list, this function is here in order
        to preserve CommonApps object, If placed outside of file a new CommonApps object
        is created
        :return: None
        """
        self.run_common_apps.install_apps()  # odd configuration, there must be a better way


class PycharmDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Linux CFG", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(300, 50)
        box = self.get_content_area()
        self.table = Gtk.Table(4, 3, False)

        self.header1 = Gtk.Label("Enter Current Pycharm Version\t\t")
        self.header2 = Gtk.Label("Enter Installation Directory\t\t\t")
        self.ver_entry = Gtk.Entry()
        self.loc_entry = Gtk.Entry()
        self.ver_entry.set_text("4.0.6")
        self.loc_entry.set_text("/opt/pycharm/")

        self.table.attach(self.header1, 0, 4, 0, 1)
        self.table.attach(self.ver_entry, 0, 4, 1, 2, xpadding=10, ypadding=10)
        self.table.attach(self.header2, 0, 4, 2, 3)
        self.table.attach(self.loc_entry, 0, 4, 3, 4, xpadding=10, ypadding=10)

        box.add(self.table)
        self.show_all()


class PPADialog(Gtk.Dialog):
    def __init__(self, parent):
        self.run_gnome_ppa = back_end.GnomePPA()
        Gtk.Dialog.__init__(self, "Linux CFG", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_YES, Gtk.ResponseType.YES,
                             Gtk.STOCK_NO, Gtk.ResponseType.NO))

        self.set_default_size(300, 50)
        box = self.get_content_area()
        self.table = Gtk.Table(4, 2, False)

        self.header = Gtk.Label("Do Gnome Upgrade After adding PPA\n"
                                "- If you just want to add Gnome PPA chose NO\n"
                                "  upgrading after includes Gnome-Shell installation")

        self.table.attach(self.header, 0, 4, 0, 1, xpadding=10, ypadding=10)

        box.add(self.table)
        self.show_all()