from subprocess import run as subrun
from os import path as ospath
from easygui import boolbox
from pyuac import isUserAdmin, runAsAdmin


def main():

    dir_path = ospath.dirname(ospath.realpath(__file__))
    turnon_path = ospath.join(dir_path, "turnonrazercontroller.ps1")
    turnoff_path = ospath.join(dir_path, "turnofrazercontroller.ps1")

    action = turnoff_path

    turnoff = boolbox("Disable Razer Xbox Controller?", choices=["Yes", "No"])
    if not turnoff:
        action = turnon_path

    powershell_executable = (
        subrun("where powershell", shell=True, capture_output=True, text=True).stdout.
        replace('\n', '')
    )

    command = [powershell_executable, "-ExecutionPolicy", "Bypass", "-File", action]

    # Run the command
    subrun(command, capture_output=False, shell=True)


if __name__ == "__main__":
    if not isUserAdmin():
        runAsAdmin()
    else:
        main()
