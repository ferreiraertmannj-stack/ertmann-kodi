# -*- coding: utf-8 -*-
"""
Ertmann Maintenance Tool
Cleans up Kodi thumbnails cache, package cache, and database to resolve graphical glitches and free up space.
"""

import os
import shutil
import xbmc
import xbmcgui
import xbmcvfs

def log(message, level=xbmc.LOGINFO):
    xbmc.log(f"[Ertmann Maintenance] {message}", level)

def clear_directory(path):
    """Safely removes all files and subdirectories inside the given path."""
    if not xbmcvfs.exists(path):
        return
        
    real_path = xbmcvfs.translatePath(path)
    try:
        for root, dirs, files in os.walk(real_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        log(f"Successfully cleared: {path}")
    except Exception as e:
        log(f"Failed to clear {path}: {e}", xbmc.LOGERROR)

def delete_file(path):
    """Safely deletes a specific file."""
    if xbmcvfs.exists(path):
        real_path = xbmcvfs.translatePath(path)
        try:
            os.remove(real_path)
            log(f"Successfully deleted: {path}")
        except Exception as e:
            log(f"Failed to delete {path}: {e}", xbmc.LOGERROR)

def main():
    log("Started execution")
    dialog = xbmcgui.Dialog()
    
    # Confirm action with user
    confirm = dialog.yesno(
        "Ertmann Maintenance", 
        "This will delete your thumbnails cache, temporary addon packages, and the textures database to fix graphical glitches and free up space.\n\nDo you want to proceed?"
    )
    
    if confirm:
        log("User confirmed cleanup")
        
        # 1. Clear Addon Packages cache
        clear_directory('special://home/addons/packages/')
        
        # 2. Clear Thumbnails
        clear_directory('special://userdata/Thumbnails/')
        
        # 3. Delete Textures13.db to force Kodi to rebuild artwork
        delete_file('special://userdata/Database/Textures13.db')
        
        dialog.ok(
            "Maintenance Complete", 
            "The cleanup was successful!\n\nIt is highly recommended that you restart the system now for the changes to take effect and the artwork to rebuild properly."
        )
        
    else:
        log("User cancelled cleanup")

if __name__ == '__main__':
    main()
