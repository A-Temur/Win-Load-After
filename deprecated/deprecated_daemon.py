import subprocess
import sys
import time
import logging
import os
from setup_reg import get_reg_value


if __name__ == "__main__":

    dir_path = get_reg_value(r"Software\LoadOrder", "LoadOrderInstallDir")
    logs_path = os.path.join(dir_path, 'logs')

    if not os.path.isdir(logs_path):
        os.mkdir(logs_path)

    logging.basicConfig(filename=f'{logs_path}/daemon.log', filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

    logging.info("Starting main")


    def launch_exe(exe_path, time_delay):
        try:
            time_delay_int = int(time_delay)
        except ValueError:
            logging.error("couldn't convert str", exc_info=True)
            time_delay_int = 10
        time.sleep(time_delay_int)
        """Launch the given executable."""
        logging.debug("launching executable")
        logging.debug(f'start "" {sys.argv[-1]} "{exe_path}"')
        subprocess.Popen(f'start "" {sys.argv[-1]} "{exe_path}"', shell=True)


    def wait_for_proc(procname):
        logging.debug("wait for proc start")
        fail_counter = 0
        while True:
            if fail_counter >= 36:
                sys.exit(369)
            result = subprocess.run(f'tasklist | findstr /B "{procname}"', text=True, capture_output=True, shell=True)
            tmp = result.stdout.splitlines()
            logging.debug(f"process results {tmp}")
            if len(tmp) >= 1:
                return True
            fail_counter += 1
            logging.debug("no process found checking again")
            time.sleep(5)

    try:
        proc_name_result = wait_for_proc(sys.argv[1])
    except Exception:
        logging.error("Unhandled exception", exc_info=True)
        sys.exit(444)

    if proc_name_result:
        launch_exe(sys.argv[2], sys.argv[3])
        logging.info("Exiting daemon")
