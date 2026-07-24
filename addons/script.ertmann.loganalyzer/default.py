# -*- coding: utf-8 -*-
"""
Ertmann Log Analyzer
Reads the current Kodi log file, filters out standard info, and presents ERROR, FATAL, and WARNING lines to the user via GUI.
"""

import os
import xbmc
import xbmcgui
import xbmcvfs

def log(message, level=xbmc.LOGINFO):
    xbmc.log(f"[Ertmann LogAnalyzer] {message}", level)

def read_and_filter_log():
    """Reads the kodi.log file and extracts important lines."""
    # Kodi stores the active log in special://logpath/kodi.log
    log_path = xbmcvfs.translatePath('special://logpath/kodi.log')
    
    if not os.path.exists(log_path):
        return "Log file not found at expected location."
        
    filtered_lines = []
    keywords = ["ERROR", "FATAL", "WARNING", "EXCEPTION"]
    
    try:
        # Read the file line by line
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            # We will process all lines, but only keep the ones containing keywords
            for line in f:
                # Basic optimization: check if any keyword exists in the string before appending
                if any(kw in line for kw in keywords):
                    filtered_lines.append(line.strip())
                    
        if not filtered_lines:
            return "No errors, warnings or fatal exceptions found in the log! Your system looks healthy."
            
        # Return a compiled string, displaying the last 100 errors to prevent UI freezing
        max_lines = 100
        result = "\n".join(filtered_lines[-max_lines:])
        
        if len(filtered_lines) > max_lines:
            result = f"... (showing last {max_lines} entries of {len(filtered_lines)} found) ...\n\n" + result
            
        return result
        
    except Exception as e:
        log(f"Failed to read log file: {e}", xbmc.LOGERROR)
        return f"Error trying to read the log file:\n{e}"

def main():
    log("Started execution")
    
    # Show progress dialog while reading (useful for huge log files)
    dp = xbmcgui.DialogProgress()
    dp.create("Ertmann Log Analyzer", "Analyzing system logs. Please wait...")
    dp.update(50)
    
    log_report = read_and_filter_log()
    
    dp.update(100)
    dp.close()
    
    # Present the result in a native text viewer
    dialog = xbmcgui.Dialog()
    dialog.textviewer("Ertmann Diagnostics - Error Report", log_report)
    
    log("Execution finished")

if __name__ == '__main__':
    main()
