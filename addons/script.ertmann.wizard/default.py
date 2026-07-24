# -*- coding: utf-8 -*-
"""
Ertmann Media Center - Setup Wizard
Entry point for the initial configuration guided flow.
"""

import sys
import xbmc
import xbmcgui
import xbmcaddon

ADDON = xbmcaddon.Addon(id='script.ertmann.wizard')

def log(message, level=xbmc.LOGINFO):
    """Log helper wrapping Kodi's logging functionality."""
    xbmc.log(f"[Ertmann Wizard] {message}", level)

class WizardUI(xbmcgui.WindowXMLDialog):
    """
    Main UI class for the setup wizard.
    Inherits from WindowXMLDialog to load custom skin XML.
    Note: 'wizard_main.xml' and 'Default' are placeholders for the future XML skinning structure.
    """
    def __init__(self, *args, **kwargs):
        super(WizardUI, self).__init__()
        self.step = 0

    def onInit(self):
        log("Wizard UI initialized")
        # Initialize UI elements here when XML is ready
        pass
        
    def onAction(self, action):
        action_id = action.getId()
        log(f"Action triggered: {action_id}")
        
        # Action IDs: 92 (Back) / 10 (Escape)
        if action_id in (92, 10):
            log("Wizard cancelled by user")
            self.close()

    def onClick(self, controlId):
        log(f"Control {controlId} clicked")

def main():
    log("Wizard add-on started")
    try:
        # Load the wizard_main.xml from the addon's resources/skins/Default/1080i/ path
        ui = WizardUI('wizard_main.xml', ADDON.getAddonInfo('path'), 'Default', '1080i')
        ui.doModal()
        del ui
    except Exception as e:
        log(f"Error launching wizard UI: {e}", xbmc.LOGERROR)

if __name__ == '__main__':
    main()
