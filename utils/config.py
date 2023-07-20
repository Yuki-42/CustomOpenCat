"""
Contains the Config class
"""

from json import load, dump
from .misc import create_logger  # Importing create logger from misc.py


class Config:
    """
    Stores the config data from the config file and provides a refresh method to update the data dynamically. This is
    useful for when the config file is changed while the program is running. This class also provides getters and
    setters for the config data.

    Due to the way that the setters are written, the config file will be saved every time a value is changed. This is
    to ensure that the config file is always up-to-date.

    Attributes:
        config_file_path (str): The path to the config file.
        logger (logging.Logger): The logger for the Config class.

    Properties:
        language (str): The language from the config file.
        model (str): The model from the config file.
        path (str): The path from the config file.
        software_version (str): The software version from the config file.
        board_version (str): The board version from the config file.
        mode (str): The mode from the config file.
    """

    def __init__(self, config_file_path="config.json"):
        self.config_file_path = config_file_path  # This is done here instead of below to allow the _get_value()
        # method to function

        self.logger = create_logger('Config', 'ConfigLogs', 'Config_')
        self.logger.info('Initializing Config object')

        self.logger.info("Checking if the config file exists")

        try:
            with open(config_file_path, "r"):  # Check if the config file exists by trying to open it in read mode
                pass  # If the file exists, do nothing

        except FileNotFoundError:
            self.logger.error("Config file not found, creating new one")

            # Create new config file
            with open(config_file_path, "w") as file:  # Open the config file in write mode and write the default
                # config data to it
                dump({
                    "language": "English",
                    "model": "Bittle",
                    "path": "./release",
                    "software_version": "2.0",
                    "board_version": "NyBoard_V1_2",
                    "mode": "Standard"
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

    @language.setter
    def language(self, value):
        """
        Sets the language in the config file.

        Args:
            value: The value to set the language to.
        """
        self._set_value("language", value)

    @property
    def model(self):
        """
        Gets the model from the config file.

        Returns:
            The model from the config file.
        """
        return self._get_value("model")

    @model.setter
    def model(self, value):
        """
        Sets the model in the config file.

        Args:
            value: The value to set the model to.
        """
        self._set_value("model", value)

    @property
    def path(self):
        """
        Gets the path from the config file.

        Returns:
            The path from the config file.
        """
        return self._get_value("path")

    @path.setter
    def path(self, value):
        """
        Sets the path in the config file.

        Args:
            value: The value to set the path to.
        """
        self._set_value("path", value)

    @property
    def software_version(self):
        """
        Gets the software version from the config file.

        Returns:
            The software version from the config file.
        """
        return self._get_value("software_version")

    @software_version.setter
    def software_version(self, value):
        """
        Sets the software version in the config file.

        Args:
            value: The value to set the software version to.
        """
        self._set_value("software_version", value)

    @property
    def board_version(self):
        """
        Gets the board version from the config file.

        Returns:
            The board version from the config file.
        """
        return self._get_value("board_version")

    @board_version.setter
    def board_version(self, value):
        """
        Sets the board version in the config file.

        Args:
            value: The value to set the board version to.
        """
        self._set_value("board_version", value)

    @property
    def mode(self):
        """
        Gets the mode from the config file.

        Returns:
            The mode from the config file.
        """
        return self._get_value("mode")

    @mode.setter
    def mode(self, value):
        """
        Sets the mode in the config file.

        Args:
            value: The value to set the mode to.
        """
        self._set_value("mode", value)

    def _get_value(self, key: str):
        """
        Gets a value from the config file. This method is private and should not be called outside of this class.

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
        Writes a new value to the config file. This method is private and should not be called outside of this class.

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
