# -*- coding: utf-8 -*-
"""
Ertmann Packager
Automatically compress each addon directory in 'addons/' into a standard Kodi repository ZIP format.
Zips are saved in 'repository/zips/<addon_id>/<addon_id>-<version>.zip'.
After zipping, it automatically calls build_repo.py to update the addons.xml index.

Usage:
    python scripts/pack_release.py
"""

import os
import shutil
import xml.etree.ElementTree as ET
import subprocess

def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_base_dir():
    return os.path.dirname(get_script_dir())

def pack_addons():
    base_dir = get_base_dir()
    addons_dir = os.path.join(base_dir, 'addons')
    zips_dir = os.path.join(base_dir, 'repository', 'zips')
    
    if not os.path.exists(zips_dir):
        os.makedirs(zips_dir)
        
    print(f"Starting packaging from: {addons_dir}")
    
    count = 0
    for item in os.listdir(addons_dir):
        item_path = os.path.join(addons_dir, item)
        if os.path.isdir(item_path):
            addon_xml = os.path.join(item_path, 'addon.xml')
            if os.path.isfile(addon_xml):
                try:
                    tree = ET.parse(addon_xml)
                    root = tree.getroot()
                    addon_id = root.attrib.get('id')
                    version = root.attrib.get('version')
                    
                    if not addon_id or not version:
                        print(f"Skipping {item}: Missing ID or Version in addon.xml")
                        continue
                        
                    # Create specific addon zip folder in repo
                    addon_zip_dir = os.path.join(zips_dir, addon_id)
                    if not os.path.exists(addon_zip_dir):
                        os.makedirs(addon_zip_dir)
                        
                    zip_name = f"{addon_id}-{version}"
                    zip_path_no_ext = os.path.join(addon_zip_dir, zip_name)
                    
                    # Create ZIP archive using shutil
                    shutil.make_archive(zip_path_no_ext, 'zip', addons_dir, item)
                    print(f"Packed: {zip_name}.zip")
                    count += 1
                except Exception as e:
                    print(f"Failed to pack {item}: {e}")
                    
    print(f"\nSuccessfully packed {count} addons.")
    print("Triggering repository XML generation...")
    
    # Call build_repo.py to update XML and MD5
    build_script = os.path.join(get_script_dir(), 'build_repo.py')
    subprocess.call(['python', build_script])
    print("Release package cycle completed.")

if __name__ == '__main__':
    pack_addons()
