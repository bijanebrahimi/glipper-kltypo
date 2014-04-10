# KLtypo (Keyboard Layout Typo)
# A glipper plugin to correct the words written in wrong keyboard layouts.
#
# Consider writing "Hello World" but you forgot the keyboard layout is not
# English (let's say Persian Layout)! Select the typo and choose 
# "Persian > English". the correct text will be replaced into clipboard and
# Will be ready to paste.
#
# Copyright: 2014 Bijan Ebrahimi, <bijanebrahimi@riseup.net>
#
# You may distribute this file under the terms of the GNU General
# Public License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
import gtk
import glipper
from gettext import gettext as _


menu = gtk.Menu()
menu_item = gtk.MenuItem(_("KLTypo"))
layouts = dict(fa=[u"\u06f1", u"\u06f2", u"\u06f3", u"\u06f4", u"\u06f5", u"\u06f6", u"\u06f7", u"\u06f8", u"\u06f9", u"\u06f0", u"\xf7", u"!", u"\u066c", u"\u066b", u"\ufdfc", u"\u066a", u"\xd7", u"\u060c", u"*", u")", u"(", u"\u0640", u"+", u"\u0636", u"\u0635", u"\u062b", u"\u0642", u"\u0641", u"\u063a", u"\u0639", u"\u0647", u"\u062e", u"\u062d", u"\u062c", u"\u0686", u"\\", u"\u0634", u"\u0633", u"\u06cc", u"\u0628", u"\u0644", u"\u0627", u"\u062a", u"\u0646", u"\u0645", u"\u06a9", u"\u06af", u"\u0638", u"\u0637", u"\u0632", u"\u0631", u"\u0630", u"\u062f", u"\u067e", u"\u0648", u".", u"/", u"\u0652", u"\u064c", u"\u064d", u"\u064b", u"\u064f", u"\u0650", u"\u064e", u"\u0651", u"]", u"[", u"}", u"{", u"|", u"\u0624", u"\u0626", u"\u064a", u"\u0625", u"\u0623", u"\u0622", u"\u0629", u"\xbb", u"\xab", u":", u"\u061b", u"\u0643", u"\u0653", u"\u0698", u"V", u"B", u"\u0654", u"\u0621", u">", u"<", u"\u061f"],
  en=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '\"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'])
menu_options = [dict(title='English > Persian', from_layout='en', to_layout='fa'),
  dict(title='Persian > English', from_layout='fa', to_layout='en')]


def info():
  info = {"Name": _("KLTypo"), 
    "Description": _("Corrects the words written in the wrong keyboard layout."),
    "Preferences": False}
  return info


def layout_decode(menu, from_layout, to_layout):
  string = glipper.get_history_item(0)
  result = []
  for ch in string:
    try:
      idx = layouts[from_layout].index(ch)
      result.append(layouts[to_layout][idx])
    except:
      result.append(ch)
  plaintext = ''.join(result)
  glipper.set_history_item(0, plaintext)
  glipper.add_history_item(plaintext)


def update_menu():
  global menu, menu_item, menu_items
  menu.destroy()
  menu = gtk.Menu()
  
  for menu_option in menu_options:
    item = gtk.MenuItem(_(menu_option['title']))
    item.connect("activate", layout_decode, menu_option['from_layout'], menu_option['to_layout'])
    menu.append(item)
  
  menu.show_all()
  menu_item.set_submenu(menu)


def init():
  global menu, menu_item
  update_menu()
  glipper.add_menu_item(menu_item)


def stop():
  menu.destroy()
