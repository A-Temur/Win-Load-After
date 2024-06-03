import subprocess


def create_batch_file(script_path, batch_file_path):
    """Create a batch file to run a Python script."""
    with open(batch_file_path, 'w') as file:
        file.write(f"@echo off\n")
        file.write(f"python \"{script_path}\"\npause\n")


def create_scheduled_task(batch_file_path, task_name):
    """Create a scheduled task to run the batch file at system startup."""
    command = f"schtasks /create /sc onstart /tn \"{task_name}\" /tr \"{batch_file_path}\" /rl LIMITED"
    try:
        subprocess.run(command, check=True, shell=True)
        print("Scheduled task created successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to create scheduled task.")
        print(e)


def main():
    script_path = "C:\\Path\\To\\Your\\Script.py"  # Change this to your Python script's path
    batch_file_path = "C:\\Path\\To\\Your\\run_script.bat"  # Change this to where you want to save the batch file
    task_name = "MyPythonScriptStartup"  # Change this to your preferred task name

    create_batch_file(script_path, batch_file_path)
    create_scheduled_task(batch_file_path, task_name)