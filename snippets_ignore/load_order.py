import psutil
import subprocess
import time
import easygui

powershell_get_process_like = 'Get-Process | Where-Object {$_.Name -like "RAZER*"} | Select-Object Name'
cmd_get_process_like = 'tasklist | findstr /B "RAZER"'
tmp = 'Get-Process Razer'


def get_powershell_location():
    result = subprocess.run('where powershell', shell=True, text=True, capture_output=True).stdout.rstrip('\n')
    return result


def get_processes(process_name, powershell=True):
    if powershell:
        command = powershell_get_process_like.replace("RAZER", process_name)
        cmd = ['powershell', '-command', command]
        # Execute powershell command
        # result = subprocess.run(cmd, text=True, capture_output=True)
        result = subprocess.run()
    else:
        command = cmd_get_process_like.replace('RAZER', process_name)
        # Execute cmd command
        result = subprocess.run(command, text=True, capture_output=True, shell=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command executed successfully!")
        print("Output:\n", result.stdout)
    else:
        print("Command failed.")
        print("Error:\n", result.stderr)






# def wait_for_process(process_name):
#     """Wait for the given process to start."""
#     while True:
#         # Check if the process is currently active
#         psutil.process_iter()
#         if any(process_name in proc.name() for proc in psutil.process_iter(attrs=['name'])):
#             return True
#         time.sleep(5)  # Check every 5 seconds
#
#
# def launch_exe(exe_path):
#     """Launch the given executable."""
#     subprocess.Popen(exe_path, shell=True)
#
#
target_process = easygui.enterbox("input proccess name (load first)")
# exe_to_launch = easygui.fileopenbox("Select Exe (load after)")
#
get_processes(target_process)
#
# # Wait for the target process to start
# print(f"Waiting for {target_process} to start...")
# wait_for_process(target_process)
# print(f"{target_process} started. Launching {exe_to_launch}...")
#
# # Launch the .exe file
# launch_exe(exe_to_launch)
