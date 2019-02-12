#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import argparse


class MyWindow(Gtk.Window):

    strUsername = ""
    strPassword = ""

    folder_prefix_to_mount = "/tmp"
    disk_to_mount = "/dev/sda1"
    remote_address_to_copy = "192.168.1.100"
    remote_folder_name_to_copy = "usbdisk"

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_row_spacing(5)
        self.add(grid)

        entryUsername = Gtk.Entry()
        entryUsername.connect("key-release-event", self.on_key_release_entryUsername)

        entryPassword = Gtk.Entry()
        entryPassword.connect("key-release-event", self.on_key_release_entryPassword)

        btnStart = Gtk.Button(label="File")
        btnStart.set_size_request(80, 30)
        btnStart.connect("clicked", self.on_button_clicked_btnStart)

        btnQuit = Gtk.Button(label="Quit")
        btnQuit.set_size_request(80, 30)
        btnQuit.connect("clicked", self.on_button_clicked_btnQuit)

        grid.attach(entryUsername, 0, 0, 1, 1)
        grid.attach(entryPassword, 0, 1, 1, 1)
        grid.attach(btnStart, 0, 2, 1, 1)
        grid.attach(btnQuit, 0, 3, 1, 1)

        self.set_border_width(10)
        self.set_title("Pardus FS")
        self.set_default_size(50, 50)
        self.connect("destroy", Gtk.main_quit)

    def on_button_clicked_btnStart(self, widget):
        print(self.strUsername)
        print(self.strPassword)

    def on_button_clicked_btnQuit(self, widget):
        Gtk.main_quit()

    def on_key_release_entryUsername(self, widget, event):
        self.strUsername = widget.get_text()

    def on_key_release_entryPassword(self, widget, event):
        self.strPassword = widget.get_text()

parser = argparse.ArgumentParser(description='This script can securely transfer files from locally connected external media to a remote file server. It scans the files using multiple anti-viruses before the transfers. So that it can reduce the possibility of transmitting malware to your internal (secure) network from external media.')
parser.add_argument("--verbosity", "-v", help="increase output verbosity. 1: Prints info for every file processed. 2: Prints extra info (HASH etc.) for every file processed. 3: Prints debug information.")
parser.add_argument("--src_path", "-s", action="store", help='Source directory containing the files (defaults to "/media/external")')
parser.add_argument("--dst_path", "-d", action="store", help='Destination directory that will be mounted for the CIFS file share before the transfer (defaults to "/media/CIFS")')
parser.add_argument("--cifs_server", "-c", action="store", help='CIFS servers IP or FQDN to connect to (defaults to 192.168.1.100)')
parser.add_argument("--user_path", "-u", action="store", help='Pattern for the users folder on the CIFS server (defaults to "/Personal/<USERNAME>/")')
args = parser.parse_args()

if args.verbosity:
	print("Verbosity turned on. I will print about every file processed.")

src_path = args.src_path
if src_path == None:
	src_path="/media/external"

dst_path = args.dst_path
if dst_path == None:
	dst_path="/media/CIFS"

if args.verbosity == "3":
	print ("Source path:", src_path)
	print ("Source path:", dst_path)

win = MyWindow()
win.show_all()
Gtk.main()
