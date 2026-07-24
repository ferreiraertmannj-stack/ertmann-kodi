# -*- coding: utf-8 -*-
import xbmc
import xbmcgui

import urllib.request

def log(message, level=xbmc.LOGINFO):
    xbmc.log(f"[Ertmann Network] {message}", level)

def check_internet(url="http://www.kodi.tv", timeout=3):
    """Test connectivity by reaching Kodi's official servers."""
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception:
        return False

def main():
    log("Started execution")
    dialog = xbmcgui.Dialog()
    
    # Show progress dialog
    dp = xbmcgui.DialogProgress()
    dp.create("Ertmann Network", "Testing connection...")
    dp.update(30, "Checking local network IP...")
    
    # Get native IP using Kodi info label
    local_ip = xbmc.getInfoLabel('Network.IPAddress')
    mac_address = xbmc.getInfoLabel('Network.MacAddress')
    
    dp.update(70, "Pinging external servers...")
    has_internet = check_internet()
    dp.update(100)
    dp.close()
    
    status = "CONNECTED" if has_internet else "DISCONNECTED"
    report = (
        f"Internet Status: {status}\n\n"
        f"Local IP Address: {local_ip if local_ip else 'Unknown'}\n"
        f"MAC Address: {mac_address if mac_address else 'Unknown'}\n"
    )
    
    dialog.ok("Network Diagnostic Results", report)

if __name__ == '__main__':
    main()
