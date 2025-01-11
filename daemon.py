import sys
import win32serviceutil
import win32service
import win32event
import servicemanager
import subprocess
import time
import configparser
import os


#TODO: servicemanager (logs) doesn't work. Find convenient way to add logs to event viewer


class PythonWinService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ProgramMaster200'
    _svc_display_name_ = 'ProgramMaster200'
    _svc_description_ = 'Python Service for using LoadAfter feature'

    def __init__(self, args):
        self.is_running = True
        try:
            self.conf = configparser.ConfigParser()
            self.conf.read(r"D:\PycharmProjects\LoadOrder\service.ini")
        except Exception as ec:
            servicemanager.LogErrorMsg(f"Error {str(ec)}\n")
            self.SvcStop()
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def log_info(self, message:str):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            0xF000,
            (message,)
        )

    def SvcStop(self):
        self.is_running = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def wait_for_proc(self, procname):
        self.log_info("wait for proc start")
        fail_counter = 0
        while True:
            if fail_counter >= 36:
                sys.exit(369)
            result = subprocess.run(f'tasklist | findstr /B "{procname}"', text=True, capture_output=True, shell=True)
            tmp = result.stdout.splitlines()
            self.log_info(f"process results {tmp}")
            if len(tmp) >= 1:
                return True
            fail_counter += 1
            self.log_info("no process found checking again")
            time.sleep(5)

    def launch_exe(self, exe_path, time_delay, priority):
        try:
            time_delay_int = int(time_delay)
        except ValueError:
            servicemanager.LogErrorMsg("couldn't convert str")
            time_delay_int = 10
        time.sleep(time_delay_int)
        """Launch the given executable."""
        priority = priority.replace('"', '')
        self.log_info("launching executable")
        # self.log_info(f'start "" {priority} "{exe_path}"')
        # subprocess.run(f'start "" {priority} "{exe_path}"', shell=True)
        os.startfile(exe_path)
        self.SvcStop()

    def main(self):
        while self.is_running:
            # React to the stop event
            if win32event.WaitForSingleObject(self.hWaitStop, 100) == win32event.WAIT_OBJECT_0:
                self.is_running = False
                break

            try:
                proc_name_result = self.wait_for_proc(self.conf["LoadAfter"]["process_load_before"])
            except Exception as e:
                servicemanager.LogErrorMsg(f"Unhandled exception {str(e)}")
                self.SvcStop()
                break

            if proc_name_result:
                self.launch_exe(self.conf["LoadAfter"]["process_load_after"], self.conf["LoadAfter"]["process_delay"],
                                self.conf["LoadAfter"]["process_priority"])
            self.SvcStop()
            break


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonWinService)
