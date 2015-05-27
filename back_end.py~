import subprocess
import os

Debug = False


class RunCmd(object):
    def __init__(self, cmd):
        self._cmd = cmd
        self._custom_cmd = ""
        self.command()

    def command(self):
        """
        Function takes in a string representing a command and then runs it
        through subprocess.call to execute command in the shell.
        :param cmd: str # command to be ran
        :return: None
        """
        self.extra_cmds()  # checks for any extra command that need to be added after or before cmd

        if Debug:
            cmd = 'xterm -e "' + self._cmd + ' ;bash & exit"'
            print("\n\nFull Cmd: {}\n\nRunning Command: {}".format(cmd, self._cmd))
            # os.system(cmd)
        # command for opening new terminal running cmd and then exiting terminal
        else:
            cmd = 'xterm -e "' + self._cmd + ' ;bash & exit"'
            os.system(cmd)

    def extra_cmds(self):
        """
        Custom commands for apps that need it, if there is more than one command per
        custom command be sure to include ';' after each one. Ex: cd; ls
        :return: None
        """

        if "pipelight-multi" in self._cmd:
            pipelight_ppa = "sudo apt-add-repository -y ppa:pipelight/stable; "
            self._custom_cmd = pipelight_ppa + self._custom_cmd[:]

            pipelight_install = "sudo pipelight-plugin --enable silverlight; " \
                                "sudo pipelight-plugin --enable widevine"
            self._cmd += ";" + pipelight_install  # pipelight install cmd's need to be at the end of final cmd

        if "pepperflashplugin-nonfree" in self._cmd:
            pepperflash_cmd = "sudo update-pepperflashplugin-nonfree --install"
            self._cmd += "; " + pepperflash_cmd  # pepperflash install need to be at end of final cmd

        if "atom" in self._cmd:
            atom_ppa = "sudo apt-add-repository -y ppa:webupd8team/atom"
            self._custom_cmd = atom_ppa + "; " + self._custom_cmd[:]

        # update needed after adding repository
        if "apt-add-repository" in self._custom_cmd:
            self._cmd = self._custom_cmd + "sudo apt-get update; " + self._cmd[:]

        if "add-apt-repository" in self._custom_cmd:
            self._cmd = self._custom_cmd + "sudo apt-get update; " + self._cmd[:]


class Update(object):
    def __init__(self):
        self.update_cmd = "sudo apt-get update; sudo apt-get upgrade -y; sudo apt-get dist-upgrade -y"

    def do_update(self):
        """
        Runs update command
        :return: None
        """
        RunCmd(self.update_cmd)


class CommonApps(object):

    def __init__(self):
        self.app_lst = []

    def add_apps(self, app):
        """
        Function adds app to app_lst if not already in app_lst
        :param app: str # name of app
        :return: None
        """
        if app in self.app_lst:
            self.app_lst.remove(app)

        else:
            self.app_lst.append(app)

    def install_apps(self):
        """
        Function ran from appdialog to install all apps within app_lst
        :return: None
        """
        if self.app_lst:  # only ran if app_lst returns True
            added_apps = " ".join(self.app_lst)
            cmd = "sudo apt-get -y install " + added_apps + " "
            RunCmd(cmd)


class Pycharm(object):
    def __init__(self, num, location):
        self._version = "pycharm-community-" + num
        self._directory = location

    def install(self):
        """
        Runs commands downloade pycharm from the web and to install
        pycharm ide in user specified directory
        :return: None
        """
        RunCmd("wget http://download.jetbrains.com/python/" + self._version + ".tar.gz; "
               "sudo tar -zxvf " + self._version + ".tar.gz; "
               "sudo mv " + self._version + " " + self._directory + "; "
               "cd " + self._directory + "bin/; "
               "./pycharm.sh; "
               "cd")


class Webmin(object):
    @staticmethod
    def install():
        """
        Runs command for installing webmin
        :return: None
        """
        RunCmd("sudo apt-get install perl libnet-ssleay-perl openssl libauthen-pam-perl "
               "libpam-runtime libio-pty-perl apt-show-versions python -y; "
               "wget http://prdownloads.sourceforge.net/webadmin/webmin_1.740_all.deb; "
               "sudo dpkg -i webmin_1.740_all.deb")


class GnomePPA(object):
    def __init__(self):
        self._staging_cmd = "sudo add-apt-repository ppa:gnome3-team/gnome3-staging -y"
        self._gnome_ppa_cmd = "sudo add-apt-repository ppa:gnome3-team/gnome3 -y"
        self._gnome_upgrade_cmd = "sudo apt-get update; sudo apt-get upgrade -y; " \
                                  "sudo apt-get dist-upgrade -y; " \
                                  "sudo apt-get install gnome-shell ubuntu-gnome-desktop -y "

    def add_ppa(self):
        """
        Function runs command to add gnome ppa
        :return: None
        """
        RunCmd(self._staging_cmd + "; " + self._gnome_ppa_cmd + "; sudo apt-get update")

    def run_upgrade(self):
        """
        Function runs command to add ppa and then an upgrade
        :return: None
        """
        RunCmd(self._staging_cmd + "; " + self._gnome_ppa_cmd + "; " + self._gnome_upgrade_cmd)


class OldFile(object):
    def __init__(self):
        self._old_file_cmd = "chmod +x linux_setup.py && ./linux_setup.py"

    def run_old_file(self):
        """
        Runs command to make old file executable and then launches it.
        used subprocess.call because RunCmd launches new window and
        user may want to run in single terminal only.
        :return: None
        """
        while True:
            question = input("Dependencies not found\n"
                             "Would you like to install GTK dependencies (yes/no) ")
            if question == "no":
                subprocess.call(self._old_file_cmd, shell=True)

            elif question == "yes":
                subprocess.call("sudo apt-get install python3-gi python-gtk2", shell=True)
                subprocess.call("python3 front_end.py", shell=True)

            else:
                print("\n**** Answer not Valid! ****\n")


class TestTerminal(object):
    def __init__(self):
        self.test_cmd = 'xterm -e "echo TERMINAL TESTING ;bash & exit"'
        self.fix_cmd = "echo Dependencies not met, preparing to install them; sleep 2;" \
                       "sudo apt-get install xterm -y"
        while self.run_test():
            self.run_test()

    def run_test(self):
        if subprocess.call(self.test_cmd, shell=True) > 0:  # 0 indicates no errors
            subprocess.call(self.fix_cmd, shell=True)
        elif subprocess.call(self.test_cmd, shell=True) == 0:
            return False
