import configparser

def config_read(filename: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(filename)
    return config
