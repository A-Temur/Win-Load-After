import sys
import time
import easygui
import os
import subprocess
import pyuac
import logging
from setup_reg import set_reg_value
from configparser import ConfigParser

# todo find additional services/processes through directories of installed application


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

    conf = ConfigParser()

    proc_name = exit_on_cancel(easygui.enterbox, "Enter Process name (load before). Example: Razer Synapse")
    easygui.msgbox("Now you have to select the .exe file, which should run automatically after the process")
    load_after = exit_on_cancel(easygui.fileopenbox, "Select file to load after the process")
    time_delay = exit_on_cancel(easygui.integerbox, "Specify how much seconds after your file should load")
    change_priority = easygui.boolbox("do you want to change the cpu priority of the launching process?")
    priority = easygui.buttonbox("Select CPU Priority (Default = Normal)", "CPU Priority",
                                 choices=["/LOW", "/BELOWNORMAL", "/NORMAL", "/ABOVENORMAL", "/HIGH",
                                          "/REALTIME"])
    block_outbound_connection = easygui.buttonbox("Do you want to block outbound (internet)"
                                                  " connection for this application all of its related processes and "
                                                  "services?",
                                                  choices=["YES", "NO"])
    if block_outbound_connection == "YES":
        filter_processes = easygui.enterbox("Enter the Process/Service Name, which begins with. "
                                            "E.g. \"Razer\" will block all processes and Services which names starts with "
                                            "Razer (Razer Synapse Software, Razer Centeral...)")

        set_starttype = easygui.buttonbox("Choose the starttype of the services",
                                          choices=["Don't Change", "Automatic", "AutomaticDelayedStart", "Manual",
                                                   "Disabled"])

    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # set windows environment var for daemon
    set_reg_value(r"Software\LoadOrder", "LoadOrderInstallDir", dir_path)

    batch_file_path = os.path.join(dir_path, "rundaemon.bat")
    daemon_path = os.path.join(dir_path, "daemon.py")
    block_related_ps_path = os.path.join(dir_path, "block_related_services.ps1")
    conf_file_path = os.path.join(dir_path, "service.ini")

    # write to conf file
    logging.info("read config")
    try:
        conf.read(conf_file_path)
        conf["LoadAfter"]["process_load_before"] = proc_name
        conf["LoadAfter"]["process_load_after"] = load_after
        conf["LoadAfter"]["process_delay"] = str(time_delay)
        conf["LoadAfter"]["process_priority"] = priority

        with open(conf_file_path, 'w') as configfile:  # save
            configfile.write(conf)
            logging.info("wrote config")
    except Exception:
        logging.error("exce", exc_info=True)
        sys.exit()

    # Create a scheduled task to run the batch file at system startup.
    # firewall_rule_name = f"LoadAfter_{proc_name}"
    # command_firewall_delete = f"netsh advfirewall firewall delete rule name=\"{firewall_rule_name}\""
    # command_firewall_add = (f"netsh advfirewall firewall add rule name=\"{firewall_rule_name}\" "
    #                         f"dir=out action=block program=\"{load_after}\" enable=yes")
    # command_task = f"schtasks /create /sc onlogon /np /tn LoadOrder /tr \"{batch_file_path}\" /rl LIMITED /f"
    try:
        # logging.debug(command_firewall_delete)
        # subprocess.run(command_firewall_delete)
        if block_outbound_connection == "YES":
            # Define the path to the PowerShell executable
            powershell_executable = (
                subprocess.run("where powershell", shell=True, capture_output=True, text=True).stdout.
                replace('\n', '')
            )
            logging.debug(powershell_executable)

            if set_starttype != "Don't Change":
                command = [powershell_executable, "-ExecutionPolicy", "Bypass", "-File", block_related_ps_path,
                           "-ProgramName", filter_processes, "-StartType", set_starttype, "-ChangeStartType"]
            else:
                command = [powershell_executable, "-ExecutionPolicy", "Bypass", "-File", block_related_ps_path,
                           "-ProgramName", filter_processes]

            # Command to run the PowerShell script

            logging.debug(command)

            # Run the command
            subprocess.run(command, capture_output=False, shell=True)
        # subprocess.run(command_task, check=True, shell=True)
        # easygui.msgbox("Scheduled task created successfully.")
        logging.info("trying to run python installer")
        res = subprocess.run(f"pythonw {daemon_path} install", check=True, shell=True, text=True, capture_output=True)
        logging.info(res)
        logging.info("sleeping")
        time.sleep(5)
        subprocess.run(f"sc config ProgramMaster200 start= delayed-auto", check=True, shell=True)
    except subprocess.CalledProcessError:
        logging.error("Failed to create service", exc_info=True)


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
