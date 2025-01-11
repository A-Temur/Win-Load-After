import winreg as reg
import logging


def get_reg_value(path, name):
    """
    Retrieve a value from the registry.

    Args:
    path (str): The registry path under HKCU where the value is stored.
    name (str): The name of the value to retrieve.

    Returns:
    The value stored in the registry, or None if the value does not exist.

    Example:
    dir_path = get_reg_value(r"Software\LoadOrder", "LoadOrderInstallDir")
    """
    try:
        # Open the specified registry key
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, path, 0, reg.KEY_READ)

        # Read the value
        value, regtype = reg.QueryValueEx(key, name)
        reg.CloseKey(key)
        return value
    except FileNotFoundError:
        logging.error(f"Registry key {path} not found.", exc_info=True)
    except WindowsError as e:  # Handle the case where the value does not exist
        logging.error(f"Error reading the registry value {name}: {e}", exc_info=True)

    return None


def set_reg_value(path, name, value):
    """
    Set a value in the registry.

    Args:
    path (str): The registry path under HKCU where the value should be stored.
    name (str): The name of the value to store.
    value (str): The data to store in the registry.

    Example:
    set_reg_value(r"Software\LoadOrder", "LoadOrderInstallDir", "C:\tmp\loadorder")
    """
    try:
        # Open the specified registry key or create it if it doesn't exist
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, path, 0, reg.KEY_WRITE | reg.KEY_SET_VALUE)
    except FileNotFoundError:
        # If the key does not exist, create it
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, path)

    # Set the value in the registry
    reg.SetValueEx(key, name, 0, reg.REG_SZ, value)
    reg.CloseKey(key)
    logging.info(f"Value '{name}' set in the registry under HKCU\\{path}")

# def main():
#     # Define the registry path, value name, and the data to store
#     reg_path = r"Software\LoadOrder"
#     value_name = "LoadOrderInstallDir"
#     data_to_store = dir_path
#
#     # Call the function to set the registry value
#     set_reg_value(reg_path, value_name, data_to_store)
#
#
#     tmp = get_reg_value(reg_path, value_name)
#     print(True)
#
#
# if __name__ == "__main__":
#     main()
