keybinds_mainwindow = [
    ("Tab", "Switch Mode"),
    ("Esc", "Exit"),
    ("U+2191" + "U+2193", "Select Item"),
    ("U+2190" + "U+2192", "Select Container"),
    ("F3", "Find in All"),
    ("F5", "Refresh All")

]
keybinds_maintab = {
    "Processes": {
        "Item": ["<Shift-Del> Kill Process"],
        "Container": ["<Strg-Tab> Change Sort Method"]
    },
    "Services": {
        "Item": ["<Shift-S> Start/Stop Service", "<Shift-T> Change Starttype", "<Shift-Del> Delete Service"],
        "Container": ["<Strg-Tab> Change Filter Method"]
    },
    "Drivers": {
        "Item": ["<Shift-S> Enable/Disable Driver", "<Shift-Del> Delete Driver"],
        "Container": ["<Strg-Tab> Change Filter Method"]
    },
    "Events": {
        "Item": ["<Enter> Show Details", "<Shift-Del> Delete Entry"],
        "Container": ["<Strg-Tab> Change Filter Layer", "<Strg-T> Change Filter Time",
                      "<Strg-Del> Delete Filtered Events"]
    },
    "Programs": {
        "Item": ["<Shift-D> Uninstall", "<Shift-R> Repair", "<Shift-O> Open Installdir"],
        "Container": ["<Strg-Tab> Change Sort Method"]
    },
    "Autostart": {
        "Item": ["<Shift-S> Activate/Deactivate"],
        "Container": ["<Strg-Tab> Change Filter Method"]
    }

}

events_details = {
    "Item": ["<Esc> Go Back", "<Shift-J> Search Online", "<Shift-C> Copy Message", "<Shift-Del> Delete Entry"]
}

keybinds_all_item = ["<Shift-R> Determine relation with other containers"]
keybinds_all_container = ["<Strg-F> Search", "<Strg-R> Refresh", "<Strg-M> Filter out Microsoft Related"]


