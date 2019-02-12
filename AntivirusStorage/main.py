#!/usr/bin/env python3

from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


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


win = MyWindow()
win.show_all()
Gtk.main()
