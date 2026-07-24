# -*- coding: utf-8 -*-
"""
Ertmann Repository Builder
Reads all addon.xml files in the addons/ directory, generates a master addons.xml,
and creates the corresponding addons.xml.md5 hash file.

Usage:
    python scripts/build_repo.py
"""

import os
import hashlib
import xml.etree.ElementTree as ET

def get_addons_dir():
    """Returns the absolute path to the addons directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(script_dir), 'addons')

def get_repo_out_dir():
    """Returns the absolute path to the repository output directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(script_dir), 'repository')

def build_addons_xml():
    """Iterates through addons and builds the master addons.xml."""
    addons_dir = get_addons_dir()
    repo_out = get_repo_out_dir()
    
    if not os.path.exists(repo_out):
        os.makedirs(repo_out)
        
    master_xml_path = os.path.join(repo_out, 'addons.xml')
    master_md5_path = os.path.join(repo_out, 'addons.xml.md5')
    
    print(f"Scanning for addons in: {addons_dir}")
    
    addons_root = ET.Element("addons")
    
    found_count = 0
    
    for item in os.listdir(addons_dir):
        item_path = os.path.join(addons_dir, item)
        if os.path.isdir(item_path):
            addon_xml_path = os.path.join(item_path, 'addon.xml')
            if os.path.isfile(addon_xml_path):
                print(f"Found addon: {item}")
                try:
                    tree = ET.parse(addon_xml_path)
                    root = tree.getroot()
                    if root.tag == "addon":
                        addons_root.append(root)
                        found_count += 1
                except Exception as e:
                    print(f"Error parsing {addon_xml_path}: {e}")
                    
    print(f"Found {found_count} total addons. Generating addons.xml...")
    
    # Write the master addons.xml
    tree = ET.ElementTree(addons_root)
    # Using 'UTF-8' with xml_declaration ensures correct Kodi processing
    tree.write(master_xml_path, encoding="UTF-8", xml_declaration=True)
    
    # Generate the MD5 hash
    with open(master_xml_path, "rb") as f:
        file_bytes = f.read()
        md5_hash = hashlib.md5(file_bytes).hexdigest()
        
    with open(master_md5_path, "w", encoding="utf-8") as f:
        f.write(md5_hash)
        
    print(f"Successfully generated:")
    print(f" - {master_xml_path}")
    print(f" - {master_md5_path} (MD5: {md5_hash})")

if __name__ == '__main__':
    build_addons_xml()
