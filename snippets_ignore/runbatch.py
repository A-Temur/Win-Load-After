import subprocess
import os


def run_batch_file(path):
    """Run a batch file and capture its output."""
    try:
        # The subprocess.run() function executes the batch file.
        # 'shell=True' is often required on Windows to execute batch files.
        result = subprocess.run(path, shell=True, text=True, capture_output=True)

        # Check if the process was completed successfully
        if result.returncode == 0:
            print("Batch file ran successfully")
            print("Output:\n", result.stdout)
        else:
            print("Batch file failed to run")
            print("Error:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred while running the batch file: {e}")


