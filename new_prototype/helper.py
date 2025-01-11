from configparser import ConfigParser


def write_config(conf: ConfigParser, full_path):
    """
    Writes to a config wile (overwrites). The File will be created if it doesn't exist.
    :param conf:
    :param full_path:
    :return:
    """
    with open(full_path, 'w') as configfile:  # save
        configfile.write(conf)


def read_config(full_path):
    return ConfigParser().read(full_path)
