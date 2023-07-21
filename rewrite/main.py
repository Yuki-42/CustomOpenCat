"""
The main injection point for the program. This file is responsible for creating the UI and starting the program.
"""

# Kyle Pannan
# Independent Spite Rewrite
# 21st July 2023

# Imports
from utils import create_logger, Translator, Config
from tkinter import Tk, Menu, Label, Button, messagebox
from tkinter.font import Font
from platform import system as system_platform  # The platform function is renamed to system_platform because the name
# 'system' is too generic and could cause issues if it is used elsewhere in the program.
from apps import FirmwareUploader, JointCalibrator, SkillComposer


"""
Requirements: 
    The app must be able to run on Windows, Mac and Linux
    The app must be able to be translated into different languages
    The app must be able to be used by people who are not programmers
    The app must be able to be used by people who are not familiar with the Nybble
    The program must be written in an asynchronous manner to allow for the UI to be responsive
"""

NaJoints = {
    'Nybble': [3, 4, 5, 6, 7],
    'Bittle': [1, 2, 3, 4, 5, 6, 7],
    'DoF16': []
}  # TODO: Find out what the fuck this actually means

apps = [FirmwareUploader, JointCalibrator, SkillComposer]


class MainWindow:
    """
    The main window of the program, used to select different sub-apps to use. Users can change the language of the app
    from here too.
    """

    def __init__(self):
        """
        The initialisation method of the MainWindow class. This method is responsible for creating the window and the
        buttons that are used to select the different sub-apps.
        """
        self.logger = create_logger("MainWindow", "MainWindow", "MainWindow_", "DEBUG")

        self.logger.info("Initializing MainWindow")
        self.logger.debug("Initializing Config")

        self.config = Config()

        self.logger.debug("Config Initialised")

        self.logger.debug("Initializing Translator")
        self.translator = Translator(self.config.language)
        self.logger.debug("Translator Initialised")

        self.openApps = {}

        self.logger.debug("Initializing Window")
        self.window = Tk()

        # If the OS is Windows, the window is set to a specific size. This is because the window is too small on Windows
        # by default.
        if system_platform() == "Windows":
            self.window.geometry(self.config.windowsSize)
        else:
            self.window.geometry("300x300")

        # Set the window icon
        self.window.iconbitmap(r'./assets/Petoi.ico')

        # Set the window title
        self.window.title = self.translator.getTranslation("uiTitle")

        # Set the font
        font = Font(family="Times New Roman", size=20, weight="bold")

        # Create the menu bar
        menuBar = Menu(self.window, background="#ff8000", foreground="black", activebackground="white",
                       activeforeground="black")

        # Create the file menu
        fileMenu = Menu(menuBar, tearoff=0, background='#ffcc99', foreground='black')

        # Populate the file menu with NaJoints for some reason
        for key in NaJoints:  # This is used for changing the models; I don't know why it is named like that
            fileMenu.add_command(label=key, command=lambda key=key: self.updateModelLabel(key))

        # I do not know what self.menuBar.add_cascade does, but it is used in the original code, so I am keeping it
        menuBar.add_cascade(label=self.translator.getTranslation("Model"), menu=fileMenu)

        # Create the language menu
        languageMenu = Menu(menuBar, tearoff=0, background='#ffcc99', foreground='black')

        # Populate the language menu with languages
        for language in self.translator.languages:
            languageMenu.add_command(label=self.translator.getIndependentTranslation(language, "lanOption"),
                                     command=lambda languageOption=language: self.updateLanguage(languageOption))

        # Add the language menu to the menu bar
        menuBar.add_cascade(label=self.translator.getTranslation("lanMenu"), menu=languageMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label=self.translator.getTranslation("About"), command=self.showAbout)  # This is adding
        # an about button to the help menu
        menuBar.add_cascade(label=self.translator.getTranslation("Help"), menu=helpMenu)  # What the fuck is this
        # variable naming

        self.window.config(menu=menuBar)

        # Create the model label
        self.modelLabel = Label(self.window, text=self.config.model, font=font)
        self.modelLabel.grid(row=0, column=0, pady=10)

        # Populate the window with the apps
        Button(self.window, text=self.translator.getTranslation("Firmware Uploader"), font=font,
               fg="blue", width=23, relief="raised",
               command=lambda app="Firmware Uploader": self.openApp("Firmware Uploader")).grid(row=1, column=0, padx=10,
                                                                                               pady=(0, 10))
        Button(self.window, text=self.translator.getTranslation("Joint Calibrator"), font=font,
               fg="blue", width=23, relief="raised",
               command=lambda app="Joint Calibrator": self.openApp("Joint Calibrator")).grid(row=2, column=0, padx=10,
                                                                                             pady=(0, 10))
        Button(self.window, text=self.translator.getTranslation("Skill Composer"), font=font,
               fg="blue", width=23, relief="raised",
               command=lambda app="Skill Composer": self.openApp("Skill Composer")).grid(row=3, column=0, padx=10,
                                                                                         pady=(0, 10))

        self.window.protocol("WM_DELETE_WINDOW", self.confirmClose)
        self.window.update()

        self.window.resizable(False, False)
        self.window.mainloop()

    def updateModelLabel(self, model):
        """
        Updates the model label to the given model.

        Args:
            model: The model to update the model label to.
        """
        self.modelLabel.config(text=model)
        self.config.model = model

    def updateLanguage(self, language: str):
        """
        Updates the language of the app to the given language.

        Args:
            language: The language to update the app to.
        """
        self.logger.info(f"Changing language to {language}")
        self.config.language = language
        self.translator.language = language

        self.logger.debug("Destroying window")
        # Destroy the main window and rebuild it in the new language
        self.window.destroy()

        # Loop through all open apps, destroy their windows without closing them, and then rebuild them
        for app in self.openApps:
            self.openApps[app].window.destroy()
            self.openApps[app].rebuildWindow()

        self.logger.debug("Rebuilding window")
        self.__init__()

    @staticmethod
    def showAbout():
        """
        Shows the 'about' window.
        """
        messagebox.showinfo('Petoi Desktop App', u'Petoi Desktop App\nOpen Source on GitHub\nCopyright © Petoi LLC\n'
                                                 u'www.petoi.com')

    def openApp(self, app: str):
        """
        Opens the given app.

        Args:
            app: The app to open.
        """
        self.logger.info(f"Opening {app}")
        match app:
            case "Firmware Uploader":
                self.logger.debug("Opening Firmware Uploader")
                self.openApps[len(self.openApps) + 1] = FirmwareUploader(self.config, self.translator)

            case "Joint Calibrator":
                self.logger.debug("Opening Joint Calibrator")
                self.openApps[len(self.openApps) + 1] = JointCalibrator(self.config, self.translator)

            case "Skill Composer":
                self.logger.debug("Opening Skill Composer")
                self.openApps[len(self.openApps) + 1] = SkillComposer(self.config, self.translator)

    def confirmClose(self):
        """
        Confirms that the user wants to close the app.
        """
        if messagebox.askokcancel(self.translator.getTranslation("Quit"),
                                  self.translator.getTranslation("Do you want to quit?")):
            self.window.destroy()


if __name__ == "__main__":
    MainWindow()
