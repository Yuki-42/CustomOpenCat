"""
Contains the Config class
"""

from json import load, dump
from misc import create_logger  # Importing create logger from misc.py


class Config:
    """
    Stores the config data from the config file and provides a refresh method to update the data dynamically. This is
    useful for when the config file is changed while the program is running.
    """

    def __init__(self, config_file_path="config.json"):
        self.config_file_path = config_file_path  # This is done here instead of below to allow the _get_value()
        # method to function

        self.logger = create_logger('Config', 'ConfigLogs', 'Config_')
        self.logger.info('Initializing Config object')

        self.logger.info("Checking if the config file exists")
        try:
            with open(config_file_path, "r"):
                pass

        except FileNotFoundError:
            self.logger.error("Config file not found, creating new one")

            # Create new config file
            with open(config_file_path, "w") as file:
                dump(
                    {
                        "language": "English"
                    },
                    file
                )

    @property
    def language(self):
        """
        Gets the language from the config file.

        Returns:
            The language from the config file.
        """
        return self._get_value("language")

    def _get_value(self, key: str):
        """
        Gets a value from the config file.

        Args:
            key: The key of the value to get.

        Returns:
            The value of the key.
        """
        self.logger.debug(f"Property {key} accessed")

        with open(self.config_file_path, 'r') as file:
            configData = load(file)

        try:
            self.logger.debug(f"Getting value for key '{key}'")

        except AttributeError:
            pass
        return configData[key]

    def _set_value(self, key: str, value):
        """
        Writes a new value to the config file.
        Args:
            key(str): The key of the value to write.
            value: The value to write.
        """
        self.logger.debug(f"Writing new value for key '{key}': {value}")
        with open(self.config_file_path, 'r') as file:
            configData = load(file)

        configData[key] = value

        with open(self.config_file_path, 'w') as file:
            dump(configData, file, indent=4)


if __name__ == "__main__":
    # Create config for testing
    config = Config()
