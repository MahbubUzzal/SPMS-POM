
import configparser
import os


class ReadConfig:
    config = configparser.RawConfigParser()

    @staticmethod
    def load_config():
        config_path = os.path.join(os.path.dirname(__file__), '..', 'configuration', 'config.ini')
        ReadConfig.config.read(config_path)

    @staticmethod
    def get_application_url():
        ReadConfig.load_config()
        url = ReadConfig.config.get("common info", "base_url")
        return url

    @staticmethod
    def get_user_name():
        ReadConfig.load_config()
        username = ReadConfig.config.get("common info", "user_name")
        return username

    @staticmethod
    def get_password():
        ReadConfig.load_config()
        password = ReadConfig.config.get("common info", "password")
        return password