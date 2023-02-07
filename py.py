#!/usr/bin/env python3

# sys - System-specific parameters and functions.
import sys
# gi - Provides bindings for GObject based libraries.
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository.WebKit2 import WebView, Settings
from gi.repository import Gtk, Gdk, GObject, GLib
gi.require_version('Vte', '2.91')
from gi.repository import Vte
# io - Core tools for working with streams.
import io
# os - Miscellaneous operating system interfaces.
import os
# argparse - Parser for command-line options, arguments and sub-commands.
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import subprocess
import numpy
from numpy import loadtxt
import pandas as pd
from collections import Counter
# Gobject VTE entry.
GObject.type_register(Vte.Terminal)

c = Counter(a=1, b=1, c=1, d=1, e=1, f=1, g=1)

# CSS configuration file loaded by Gtk.CssProvider.
CSS_File = b"""
  /* shrink headerbars */
  headerbar {
      min-height: 0px;
      padding-left: 2px; /* same as childrens vertical margins for nicer proportions */
      padding-right: 2px;
      background-color: #2d2d2d;
      border:0;
  }
  textview text {
      color:#4fc3f7;
  }
  button {
      border-radius: 10px;
  }
  button:hover {
      border-color: pink;
      opacity: 50;
  }
  button:active {
    color: #FFF;
    background: #F00;
  }
  headerbar entry,
  headerbar spinbutton,
  headerbar button,
  headerbar separator {
      margin-top: 0px; /* same as headerbar side padding for nicer proportions */
      margin-bottom: 0px;
  }
  /* shrink ssd titlebars */
  .default-decoration {
      min-height: 0; /* let the entry and button drive the titlebar size */
      padding: 0px;
      background-color: #2d2d2d;
  }
  .default-decoration .titlebutton {
      min-height: 0px; /* tweak these two props to reduce button size */
      min-width: 0px;
  }
  window.ssd headerbar.titlebar {
      padding-top: 3px;
      padding-bottom: 3px;
      min-height: 0;
      background-color: #2d2d2d;
  }
  window.ssd headerbar.titlebar button.titlebutton {
      padding: 3px;
      min-height: 0;
      border-radius: 0;
      margin-right: 2px;
      background-color: #2d2d2d;
  }
"""

# Command line options.
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-f",
                    "--file", 
                    default="", 
                    help="File chosen to open with.")
args = vars(parser.parse_args())
file = args["file"]

# GTK Settings.
settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)
screen = Gdk.Screen.get_default()
provider = Gtk.CssProvider()
provider.load_from_data(CSS_File)
Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

  
# GTK Handeler class.
class Handler:
    # Closes program when window is exited.
    def onDestroy(self,*args):
      Gtk.main_quit()

    def onFileActivated(self,*args):
      file = filechooserwidget.get_filename()
      subprocess.run(["subl", file])

    def onEntryActivate(self,*args):
      title = "https://" + entry1.get_text()
      webview.load_uri(title)
      print(title)

    def onBackActivate(self,*args):
      webview.go_back()

    def onRefreshActivate(self,*args):
      webview.reload()

    def onForwardActivate(self,*args):
      webview.go_forwards()

    def onMinusButtonClicked(self,button):
      #statusbar.remove_all(context)
      if (mainnotebook.get_n_pages() >= 2):
        page = mainnotebook.get_current_page()
        mainnotebook.remove_page(page)
    
    def onAddButtonClicked(self,button):
      mainnotebook.page = Gtk.Box()
      mainnotebook.page.set_border_width(0)
      terminal1 = Vte.Terminal()
      terminal1.spawn_sync(Vte.PtyFlags.DEFAULT,
                           os.environ['HOME'],
                           ["/bin/bash"],
                           [],
                           GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                           None,
                           None,
                           )
      mainnotebook.page.add(terminal1)
      mainnotebook.page.set_child_packing(terminal1, True, True, 0, 0)
      mainnotebook.append_page(mainnotebook.page, Gtk.Label(label="Terminal"))
      window.show_all()
      mainnotebook.set_current_page(-1) 

    def onPackagerAdd(self,*args):
      text = entry2.get_text()
      lista=pd.read_csv('packages.txt',sep=',',header=None)[0].tolist()
      listc=pd.read_csv('packages.txt',sep=',',header=None)[2].tolist()
      text = entry2.get_text()
      print(lista)
      store.append((lista[0], listc[0]))

    def nestedToggled(self,*args):
      c['a'] += 1
      if c['a'] > 2:
        c['a'] = 1
      print(c['a'])

    def uefiToggled(self,*args):
      c['b'] += 1
      if c['b'] > 2:
        c['b'] = 1
      print(c['b'])

    def dndToggled(self,*args):
      c['c'] += 1
      if c['c'] > 2:
        c['c'] = 1
      print(c['c'])

    def clipboardToggled(self,*args):
        c['d'] += 1
        if c['d'] > 2:
          c['d'] = 1
        print(c['d'])

    def d3Toggled(self,*args):
        c['e'] += 1
        if c['e'] > 2:
          c['e'] = 1
        print(c['e'])

    def audioToggled(self,*args):
        c['f'] += 1
        if c['f'] > 2:
          c['f'] = 1
        print(c['f'])

    def usbToggled(self,*args):
        c['g'] += 1
        if c['g'] > 2:
          c['g'] = 1
        print(c['g'])

    def onCreateButton(self,*args):
      text = vmlocation.get_filename()
      print(text)
      uuid = vmEntry.get_text()
      if c['a'] == 2:
        mailA = print("VBoxManage modifyvm", uuid, "--nested-paging=on")
      cpu_cores = vmcores.get_value()
      vmMemory = vmvmemory.get_value()
      if c['b'] == 2:
        mailB = print("VboxManage", uuid, "bios=efi")
      if c['c'] == 2:
        mailC = print("VBoxManage", uuid, "--drag-and-drop= disabled")
      if c['d'] == 2:
        mailD = print
      if c['e'] == 2:
        mailE = print
      if c['f'] == 2:
        mailF = print
      if c['G'] == 2:
        mailG = print

      var = "grep MemTotal /proc/meminfo| awk -F ' ' '{print $2}'"
      output = subprocess.getoutput(var)
      print (output)
      max_ram_mb = int(output) / 1000
      print(max_ram_mb)
      vm_memory.set_range(0, max_ram_mb)
      text = str("Max = ") + str(max_ram_mb)
      vm_memory.set_placeholder_text(text)
      vm_memory.set_progress_fraction(1.00)




# Builder definitions.
builder = Gtk.Builder.new_from_file("/mnt/d/box/ho/ui.ui")
builder.connect_signals(Handler())
window = builder.get_object("main-window")
webview = builder.get_object("webview")
webview2 = builder.get_object("webview2")
terminal = builder.get_object("terminal")
filechooserwidget = builder.get_object("filechooserwidget")
entry1 = builder.get_object("entry1")
mainnotebook = builder.get_object("main-notebook")
statusbar = builder.get_object("statusbar")
liststore1 = builder.get_object("liststore1")
tree_one = builder.get_object("tree_one")
entry2 = builder.get_object("entry2")
vmNetwork = builder.get_object("vm_network")
vm_memory = builder.get_object("vm_memory")
vmEntry = builder.get_object("vmEntry")
vmlocation = builder.get_object("vm_location")
vmcores = builder.get_object("vm_cores")
vmvmemory = builder.get_object("vm_vmemory")
vmvmemory = builder.get_object("vm_vmemory")

# Opends the file specified in -f command line option if provided.
if (file != ""):
  pass

# Terminal spawn settings.
terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ['HOME'],
    ["/bin/bash"],
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )

# Sets the default page for the webview.
webview.load_uri("https://www.google.com")
webview2.load_uri("https://aur.archlinux.org/packages")

store = Gtk.ListStore(str, float)
#text = subprocess.run(["yay", "-Qq"])
#store.append(('yay', 'Package manager.', 11.3))
#lines = loadtxt("packages.txt", comments="#", delimiter=",", unpack=False)
#store.append((text, 'Package manager.', 11.3))

#lista=pd.read_csv('packages.txt',sep=',',header=None)[0].tolist()
#print(lista)
#store.append((lista, 'Package manager.', 11.3))

renderer = Gtk.CellRendererText()

column = Gtk.TreeViewColumn('Name', renderer, text=0)
tree_one.append_column(column)

column = Gtk.TreeViewColumn('Version', renderer, text=2)
tree_one.append_column(column)
store.append(('yay', 12.1))

store2 = Gtk.ListStore(str)
#renderer2 = Gtk.CellRendererText()
#column = Gtk.TreeViewColumn('Name', renderer2, text=0)
#store2.append_column(column)
list = ["NAT"]
store2.append((list))
vmNetwork.set_model(store2)

#vmNetwork.set_model(store)

# def on_select_change(self, widget):
#   m, itr = widget.get_selected()
#   if itr:
#     print(m[itr][1])

# select = tree_one.get_selection()
# select.connect('changed', on_select_change)



tree_one.set_model(store)
# Recursively shows the 'window' widget, and any child widgets.
window.show_all()
window.maximize()

# Runs the main loop until gtk_main_quit() is called.
Gtk.main()