"""
Contains the miscellaneous methods associated with the project but not part of the main logic of the system
"""

from datetime import datetime
# create_logger imports
from logging import FileHandler, StreamHandler, getLogger, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, \
    LoggerAdapter
from os import getcwd, path, mkdir
from pathlib import Path
from sys import stdout


def get_ansi_escape_code(
        base_colour: str,
        bold: bool = False,
        underline: bool = False,
) -> str:
    """
    Gets the ANSI escape code for the given colour.

    Args:
        base_colour (str): The base colour to get the ANSI escape code for.
        bold (bool): Whether the text should be bold.
        underline (bool): Whether the text should be underlined.

    Returns:
        str: The ANSI escape code for the given colour.

    Raises:
        ValueError: If the given colour is not a valid colour.

    Reference:
        https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
    """
    if base_colour.endswith("_H"):  # Specifies that the colour is of a high intensity. (Defined as 90-97)
        base_colour = base_colour[:-2]
        high_intensity = True
    else:
        high_intensity = False

    match base_colour.upper():
        case "BLACK":
            colour_code = 30
        case "RED":
            colour_code = 31
        case "GREEN":
            colour_code = 32
        case "YELLOW":
            colour_code = 33
        case "BLUE":
            colour_code = 34
        case "PURPLE":
            colour_code = 35
        case "CYAN":
            colour_code = 36
        case "WHITE":
            colour_code = 37
        case _:
            raise ValueError(f"{base_colour} is not a valid colour.")

    if high_intensity:
        colour_code += 60

    if bold:
        formatter = "1;"
    elif underline:
        formatter = "4;"
    elif bold and underline:
        formatter = "1;4;"
    else:
        formatter = ""
    # Assemble the ANSI escape code
    ansi_escape_code = f"\033[{formatter}{colour_code}m"

    return ansi_escape_code


class ColourCodedFormatter(Formatter):
    """
    A formatter that adds colour coding to the log messages.
    """

    def __init__(self, fmt=None, datefmt=None, style='%',
                 colour_coding: dict = None
                 ):
        super().__init__(fmt, datefmt, style)

        if colour_coding is None:
            colour_coding = {
                "DEBUG": get_ansi_escape_code("CYAN"),
                "INFO": get_ansi_escape_code("GREEN"),
                "WARNING": get_ansi_escape_code("YELLOW"),
                "ERROR": get_ansi_escape_code("RED"),
                "CRITICAL": get_ansi_escape_code("RED_H"),
            }
        self.colour_coding = colour_coding

    def format(self, record):
        """
        Formats the log message.

        Args:
            record (LogRecord): The log record to format.

        Returns:
            str: The formatted log message.
        """
        try:
            record.levelname = f"{self.colour_coding[record.levelname]}{record.levelname}\033[0m"
        except KeyError:  # Handles the case where the level name is not in the colour coding dictionary
            pass
        return super().format(record)


def create_logger(
        name: str,
        logging_directory: str,
        log_file_name: str,
        level: str = "DEBUG",
        format_string: str = "%(asctime)-15s %(logger_name)s - %(levelname)s - %(message)s",
        handlers: list = None,
        do_colour: bool = True,
        colour_coding: dict = None
) -> LoggerAdapter:
    """
    Creates a logger with the specified name, logging path, level, and formatter.

    Args:
        name (str): The name of the logger.
        logging_directory (str): The path to the logging directory.
        log_file_name (str): The name of the log file.
        level (str): The level of the logger.
        format_string (str): The format string for the logger.
        handlers (list): Additional handlers for the logger.
        do_colour (bool): Whether to use colour coding in the logger for logging outputs.
        colour_coding (dict): The colour coding for the logger. Defaults to the default colour coding defined in the
            function.

    Returns:
        logger (Logger): The logger object.

    """
    if not path.exists(Path(f"{getcwd()}/Logs/")):
        mkdir(Path(f"{getcwd()}/Logs/"))

    # Check if the logging directory exists, if not, create it
    if not path.exists(Path(f'{getcwd()}/Logs/{logging_directory}')):
        mkdir(Path(f'{getcwd()}/Logs/{logging_directory}'))

    match level.lower():
        case "debug":
            level = DEBUG
        case "info":
            level = INFO
        case "warning":
            level = WARNING
        case "error":
            level = ERROR
        case "critical":
            level = CRITICAL
        case _:
            raise ValueError('Invalid level specified')

    logger = getLogger(name)  # Sets the logger's name
    logger.setLevel(level)  # Sets the logger's level

    if logger.hasHandlers():  # This checks if the logger has already been created and if it has, it replaces the
        # handlers with the new ones
        logger.handlers.clear()

    if handlers is None:
        handlers = [
            FileHandler(
                Path(
                    f'{getcwd()}/Logs/{logging_directory}/{log_file_name}{datetime.now().strftime("%d.%m.%Y")}.log'
                ),
                encoding='utf-8'
            ),  # Creates the file handler for the logger
            StreamHandler(stdout)  # Creates the stream handler for the logger
        ]

    colour_formatter = ColourCodedFormatter(format_string, colour_coding=colour_coding)
    formatter = Formatter(format_string)

    for handler in handlers:
        if not do_colour or isinstance(handler, FileHandler):
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            pass

        else:
            handler.setFormatter(colour_formatter)
            logger.addHandler(handler)

    # A logger adapter is used here to allow for the logger name to be included in the log messages. This is useful
    # when multiple loggers are used in the same project.
    logger = LoggerAdapter(logger, {'logger_name': name})
    return logger
