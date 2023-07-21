"""
Contains the FirmwareUploader class.
"""

from ..utils import create_logger, Translator, Config


class FirmwareUploader:
    """
    Contains the FirmwareUploader class.
    """

    def __init__(self, config: Config, translator: Translator):
        self.logger = create_logger("FirmwareUploader", "FirmwareUploader", "FirmwareUploader_", "DEBUG")

        self.logger.info("Initializing FirmwareUploader")
        self.logger.debug("Initializing Config")
        self.config = config
        self.logger.debug("Config Initialized")

        self.logger.debug("Initializing Translator")
        self.translator = translator
        self.logger.debug("Translator Initialized")

        self.logger.debug("Initializing Window")


    def __str__(self) -> str:
        return "Firmware Uploader"

    @property
    def name(self) -> str:
        """
        Gets the name of the app.
        """
        return self.__str__()

    def rebuildWindow(self):
        """
        Rebuilds the window.
        """
        pass
