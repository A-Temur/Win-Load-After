def activate_deactivate_driver_powershell(device_id, activate=True):
    """
    Enable/Disable-PnpDevice
    :param device_id:
    :param activate:
    :return:
    """
    enable_disable = ("Disable", "Enable")

    command = (f'{enable_disable[int(activate)]}-PnpDevice -InstanceId '
               f'"{device_id}" -Confirm:$false')
    return command


def kill_process_cmd(process_id, force=True):
    """
    taskkill
    :param process_id:
    :param force:
    :return:
    """
    force_ = ("", " /F")
    return f'taskkill{force_[int(force)]} /PID {process_id}'


def get_all_running_processes_cmd(output_format='table'):
    """
    tasklist
    :param output_format:
    table:
    csv:
    list:
    :return: returns a list of all running processes
    """
    output_formats = ['table', 'list', 'csv']
    output_format_ = output_formats.index(output_format)
    return f"tasklist /fo {output_formats[output_format_]}"


def find_process_powershell(process_name, search_mode='like'):
    """
    Get-Process | Where-Object ...
    :param process_name: str process name to search for
    :param search_mode: available modes:
    like (finds all processes that begins with string process_name*).
    eq = equals (string must be equal)
    :return: returns a list of all matching processes.
    """
    search_modes = ['like', 'eq']
    search_mode_ = search_modes.index(search_mode)
    return f"Get-Process | Where-Object {{$_.ProcessName -{search_modes[search_mode_]} \"{process_name}\"}}"


def find_process_cmd(process_name):
    return f'tasklist | findstr /B "{process_name}"'


def find_service_powershell(service_name, search_mode='like'):
    """
    Get-Service | Where-Object ...
    :param service_name: str service name to search for
    :param search_mode: available modes:
    like (finds all services that begins with string service_name*).
    eq = equals (string must be equal)
    :return: returns a list of all matching services.
    """
    search_modes = ['like', 'eq']
    search_mode_ = search_modes.index(search_mode)
    return f"Get-Service | Where-Object {{$_.DisplayName {search_modes[search_mode_]} \"{service_name}\"}}"


def find_firewall_rule_powershell(rule_name):
    return f'Get-NetFirewallRule -DisplayName "{rule_name}" -ErrorAction SilentlyContinue'


def remove_firewall_rule_powershell(rule_name):
    return f'Remove-NetFirewallRule -DisplayName "{rule_name}"'


def add_new_firewall_rule_powershell(rule_name, program_path, outbound=True):
    directions = ("Inbound", "Outbound")
    return (f'New-NetFirewallRule -DisplayName "{rule_name}" -Direction {directions[int(outbound)]} '
            f'-Program "{program_path}" -Action Block')


def get_service_path_powershell(service_name):
    return f'(Get-WmiObject -Query "SELECT PathName FROM Win32_Service WHERE Name = \'{service_name}\'").PathName'


def set_service_starttype_powershell(service_name, starttype="Manual"):
    starttypes = ["Automatic", "AutomaticDelayedStart", "Manual", "Disabled"]
    starttype_ = starttypes.index(starttype)
    return f'Set-Service -Name "{service_name}" -StartupType {starttypes[starttype_]}'


def set_service_starttype_cmd(service_name, starttype="manual"):
    starttypes = ["auto", "delayed_auto", "manual", "disabled"]
    starttype_ = starttypes.index(starttype)
    return f'sc config "{service_name}" start= {starttypes[starttype_]}'


def launch_exe_cmd(exe_path, priority="/NORMAL"):
    priorities = ["/LOW", "/BELOWNORMAL", "/NORMAL", "/ABOVENORMAL", "/HIGH", "/REALTIME"]
    priority_ = priorities.index(priority)
    return f'start "" {priorities[priority_]} "{exe_path}"'
