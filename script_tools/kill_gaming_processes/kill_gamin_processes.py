import subprocess
import sys
import pyuac
import re


def main():
    tester = subprocess.run(f"tasklist /fo table", shell=True, text=True, capture_output=True, ).stdout
    tmp = tester.splitlines()

    pids = []
    pattern = r"\b\d{4,5}\b"
    filters = ["Razer", "GameManagerService", "CefSharp", "EABackground"]
    for processes in tmp:
        if len(processes) > 4:
            for bloat in filters:
                if bloat in processes:
                    drrr = re.findall(pattern, processes)[0]
                    pids.append(drrr)

    pids = [item + " " for item in pids]
    # pids_str = ''.join(map(str, pids)).rstrip(' ')
    # command = "taskkill /F /PID " + pids[0]
    # subprocess.run(command, shell=True, text=True, capture_output=True)
    for i in pids:
        subprocess.run(f"taskkill /F /PID {i}", shell=True, capture_output=True)


if __name__ == "__main__":
    
    if not pyuac.isUserAdmin():
        try:
            pyuac.runAsAdmin()
        except BaseException:
            sys.exit()
    else:
        main()
