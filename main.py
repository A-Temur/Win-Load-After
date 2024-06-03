import easygui
import os
import subprocess
from pyuac import main_requires_admin


@main_requires_admin
def main():
    proc_name = easygui.enterbox("Enter Process name (load before)")
    load_after = easygui.fileopenbox("Select file to load after the process")
    time_delay = easygui.integerbox("Specify how much seconds after your file should load")
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    batch_file_path = os.path.join(dir_path, "scheduler.bat")
    daemon_path = os.path.join(dir_path, "daemon.py")

    with open(batch_file_path, 'w') as file:
        file.write(f"@echo off\n")
        file.write(f"python \"{daemon_path}\" {proc_name} {load_after} {time_delay}")

    # Create a scheduled task to run the batch file at system startup.
    command = f"schtasks /create /sc onstart /tn LoadOrder /tr \"{batch_file_path}\" /rl LIMITED"
    try:
        subprocess.run(command, check=True, shell=True)
        print("Scheduled task created successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to create scheduled task.")
        print(e)


if __name__ == "__main__":
    main()
