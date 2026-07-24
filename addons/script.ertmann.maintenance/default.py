# -*- coding: utf-8 -*-
import xbmc
import xbmcgui

def main():
    xbmc.log("[Ertmann Maintenance] Addon started", xbmc.LOGINFO)
    dialog = xbmcgui.Dialog()
    dialog.ok("Ertmann Maintenance", "Maintenance tools will be available here soon.")

if __name__ == '__main__':
    main()
