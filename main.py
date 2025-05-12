import sys
import easygui
import os
import subprocess
import pyuac
import logging
from setup_reg import set_reg_value


if not os.path.isdir('logs'):
    os.mkdir('logs')

logging.basicConfig(filename='logs/main.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s',
                    level=logging.DEBUG)


def main():
    def exit_on_cancel(func, *args):
        val = func(*args)
        if val:
            return val
        else:
            sys.exit()

    proc_name = exit_on_cancel(easygui.enterbox, "Enter Process name (load before). Example: Motherboard Software Process Name (e.g. 'GCC', 'ArmouryCrate'...)."
                                                 "no full Process Name required, this program will check each running process which 'begins with' your given input (also case insensitive).")
    easygui.msgbox("Now you have to select the .exe file, which should run automatically after the process (load after). E.g. (select Razer Synapse executable).")
    load_after = exit_on_cancel(easygui.fileopenbox, "Select file to load after the process")
    time_delay = exit_on_cancel(easygui.integerbox, "Specify a delay in seconds between the Process (load before) and the final execution of your selected .exe (load after).")
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # set windows environment var for daemon
    set_reg_value(r"Software\LoadOrder", "LoadOrderInstallDir", dir_path)

    batch_file_path = os.path.join(dir_path, "rundaemon.bat")
    daemon_path = os.path.join(dir_path, "daemon.py")

    with open(batch_file_path, 'w') as file:
        file.write(f"@echo off\n")
        file.write(f"""pythonw \"{daemon_path}\" {proc_name} "{load_after}" {time_delay} \n""")
        file.write(f"exit")

    # Create a scheduled task to run the batch file at system startup.
    command = f"schtasks /create /sc onlogon /np /tn LoadOrder /tr \"{batch_file_path}\" /rl LIMITED /f"
    try:
        subprocess.run(command, check=True, shell=True)
        easygui.msgbox("Scheduled task created successfully.")
    except subprocess.CalledProcessError:
        logging.error("Failed to create scheduled task", exc_info=True)


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        try:
            pyuac.runAsAdmin()
        except BaseException as e:
            if e.args[0] == 1223:
                easygui.msgbox("This program need Admin privileges for using the window Task Scheduler, "
                               "exiting program")
                sys.exit(305)
            else:
                logging.error("Uncaught Exception", exc_info=True)
                sys.exit(444)

    else:
        main()
