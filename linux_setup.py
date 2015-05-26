#!/usr/bin/env python3
import subprocess


def common_apps():
    """
    install common applications: ssh and wine if user chooses, gedit, peperflash,
    ubuntu-restricted-extras icedtea-7-plugin openjdk-7-jre openjdk-7-jdk
    and gnome-terminal. more apps can be added to list as needed
    :return: None
    """
    ###################################################
    #  List of apps to install, add common apps here  #
    ###################################################
    app_list = []

    all_app_list = ["gedit", "ubuntu-restricted-extras", "chromium-browser", "preload",
                    "icedtea-7-plugin openjdk-7-jre", "openjdk-7-jdk", "gnome-terminal",
                    "pepperflashplugin-nonfree", "tmux", "vim", "htop", "git"]


    option = input("\n\t Would you like to install SSH (y/N)")
    ssh = lambda cmd: app_list.append("ssh") if option == "y" else False
    ssh(option)

    option = input("\n\t Would you like to install wine and playonlinux (y/N)")
    wine = lambda cmd: app_list.append("playonlinux") if option == "y" else False
    wine(option)

    option = input("\n\t Would you like to install Atom Text editor (y/N)")
    if option == "y":
        call_cmd("sudo add-apt-repository -y ppa:webupd8team/atom")
        call_cmd("sudo apt-get update")
        call_cmd("sudo apt-get install atom -y")

    option = input("\n\t Would you like to run auto install for common apps (y/N)")
    if option == "y":
        app_list += all_app_list

        ############################################################################
        # Add apps that require ppa's or other miscellaneous options:              #
        # NOTE below apps will not present user with an option to install unless   #
        # coded in                                                                 #
        ############################################################################

        print("\n\t INSTALLING pipelight")
        call_cmd("sudo apt-add-repository ppa:pipelight/stable -y")
        call_cmd("sudo apt-get update -y && sudo apt-get install pipelight-multi -y")
        call_cmd("sudo pipelight-plugin --enable silverlight -y")
        call_cmd("sudo pipelight-plugin --enable widevine -y")

    for app in app_list:
        print("\n\t INSTALLING " + app)
        call_cmd("sudo apt-get install " + app + " -y")
        if app == "pepperflashplugin-nonfree":
            call_cmd("sudo update-pepperflashplugin-nonfree --install")


def menu():
    """
    presents the user with a menu of options
    :return: None
    """
    print("\n\n"
          "\t######################################################################\n"
          "\t# (1) Install Common Apps  \t(5) Install webmin                   #\n"
          "\t# (2) Install gnome-shell  \t(6) Set gnome-terminal as default    #\n"
          "\t# (3) Add Gnome 3.14 PPA's \t                                     #\n"
          "\t# (4) Install Pycharm      \t                                     #\n"
          "\t#                          \t                                     #\n"
          "\t#                          \t                                     #\n"
          "\t# (X) Exit       (M) Menu  \t(H) Help                             #\n"
          "\t######################################################################")


def what_is():
    """
    presents the user with a more descriptive menu of what
    the options do
    :return: None
    """
    print("\n"
          "\n\t (1) Install Common Apps \n"
          "\t       > installs gedit, peperflash, \n"
          "\t         restricted-extras, pipelight, wine,\n"
          "\t         gnome-terminal, ssh, java and more\n"
          "\n\t (2) Install gnome-shell \n"
          "\t       > installs gnome-shell and ubuntu-gnome-desktop\n"
          "\t         (non-updated)\n"
          "\n\t (3) Add Gnome 3.14 PPA's \n"
          "\t       > adds PPA's for gnome-shell 3.14 and prompts \n"
          "\t         for dist-upgrade\n"
          "\n\t (4) Install Pycharm \n"
          "\t       > downloads pycharm and installs by extracting \n"
          "\t         and calling bash script\n"
          "\n\t (5) Install webmin\n"
          "\t       > installs webmin and dependencies\n"
          "\n\t (6) Set gnome-terminal as default\n"
          "\t       > sets gnome terminal as default terminal\n"
          "\t         (WORKS ONLY WITH GSETTINGS)\n"
          "\n\t (H) Help \n"
          "\t       > You are here\n"
          "\n\t (M) Menu \n"
          "\t       > Shows start up menu for command reference\n"
          "\n\t (X) Exit \n"
          "\t       > exits program\n")


def gnome_shell():
    """
    installs gnome-shell and ubuntu-gnome-desktop, installs only from
    default PPA's not updated PPA's, most likely no the current version
    :return: None
    """
    print("\n\t INSTALLING GNOME-SHELL ")
    call_cmd("sudo apt-get install gnome-shell ubuntu-gnome-desktop -y")


def gnome_ppa():
    """
    adds gnome-shell 3.14 PPA's and runs sources update. then prompts
    the user for an installation of gnome-shell from newly added PPA's
    :return: None
    """
    print("\n\t ADDING GNOME PPA'S")
    call_cmd("sudo add-apt-repository ppa:gnome3-team/gnome3-staging -y")
    call_cmd("sudo add-apt-repository ppa:gnome3-team/gnome3 -y")
    call_cmd()

    option = input("\t Would you like to upgrade gnome-shell now (y/N): ")
    dist_update = lambda cmd: call_cmd("sudo apt-get dist-upgrade -y") if cmd == "y" else False
    dist_update(option)


def pycharm():
    """
    installs pycharm by getting file from online and extracting it, then
    it moves extracted files to /opt/pycharm/ or user specified directory
    after moving to directory the pycharm.sh script is launched
    :return: None
    """
    number = input("\n    What is the current version number for Pycharm: ")
    version = "pycharm-community-" + number
    call_cmd("wget http://download.jetbrains.com/python/" + version + ".tar.gz ")

    directory = input("    Enter installation directory (default /opt/pycharm/): ")
    if directory == "":
        directory = "/opt/pycharm/"
        call_cmd("sudo tar -zxvf " + version + ".tar.gz")
        call_cmd("sudo mv " + version + " " + directory)
        call_cmd("cd " + directory + "bin/ && " + "sudo ./pycharm.sh &")
        call_cmd("cd")

    else:
        call_cmd("sudo tar -zxvf " + version + ".tar.gz")
        call_cmd("sudo mv " + version + " " + directory)
        call_cmd("cd " + directory + "bin/ && " + "sudo ./pycharm.sh &")
        call_cmd("cd")


def webmin():
    """
    installs webmin by getting file from online and running the dpkg -i
    command to install it. Dependencies and installed as well through
    apt-get install
    :return: None
    """
    print("\n\t INSTALLING webmin")
    call_cmd("sudo apt-get install perl libnet-ssleay-perl openssl libauthen-pam-perl "
             "libpam-runtime libio-pty-perl apt-show-versions python -y")
    call_cmd("wget http://prdownloads.sourceforge.net/webadmin/webmin_1.740_all.deb")
    call_cmd("sudo dpkg -i webmin_1.740_all.deb")


def call_cmd(text="sudo apt-get update -y && sudo apt-get upgrade -y"):
    """
    runs 'call' command that allows python to run bash commands in through
    python script. function takes in string (command to run) and converts
    it to proper syntax to run from python
    :param text: Str # command to execute
    :return: None
    """
    subprocess.call("echo -e \033[93m", shell=True)
    print(" *** RUNNING -> " + text)
    subprocess.call("echo -e \033[0m", shell=True)

    subprocess.call([text], shell=True)
    print("\n\t *** DONE ***")


def select():
    """
    tests for proper command entry and executes functions according to the
    command the user wants to preform. pints invalid input for errors in input
    :return: None
    """
    cmds = ["1", "2", "3", "4", "5", "6", "H", "M", "X"]
    while True:
        option = input("\n > Select an option from the menu or \n"
                       "   type 'M' to view menu: ")
        if option in cmds:
            if option == "1":
                common_apps()
            if option == "2":
                gnome_shell()
            if option == "3":
                gnome_ppa()
            if option == "4":
                pycharm()
            if option == "5":
                webmin()
            if option == "6":
                call_cmd("sudo apt-get install gnome-terminal -y")
                call_cmd("sudo gsettings set org.gnome.desktop.default-applications.terminal "
                         "exec 'gnome-terminal'")
            if option == "H":
                what_is()
            if option == "M":
                menu()
            if option == "X":
                print()
                break
        else:
            print("\n\t *** Invalid Input ***")


def main():
    print("\n\n")
    option = input("\n > Have you updated before launching app (Y/n): ")
    update = lambda cmd: call_cmd() if cmd in ["n", "N"] else True
    update(option)

    menu()
    select()


if __name__ == '__main__':
    main()
