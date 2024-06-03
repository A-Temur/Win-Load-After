import subprocess
import sys
import time


if __name__ == "__main__":
    def launch_exe(exe_path, time_delay):
        time.sleep(time_delay)
        """Launch the given executable."""
        subprocess.Popen(exe_path)

    def wait_for_proc(procname):
        while True:
            result = subprocess.run(f'tasklist | findstr /B "{procname}"', text=True, capture_output=True, shell=True)
            tmp = result.stdout.splitlines()
            if len(tmp) >= 1:
                return True
            time.sleep(5)

    try:
        proc_name_result = wait_for_proc(sys.argv[1])
        if proc_name_result:
            launch_exe(sys.argv[2], sys.argv[3])
    except Exception as e:
        with open("log.txt", 'w') as file:
            file.write(e.__str__())
