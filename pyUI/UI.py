#!/usr/bin/python3
# -*- encoding: UTF-8 -*-

"""
The UI file for the project. This file contains the UI class.
"""

# Rongzhong Li
# Petoi LLC
# May.22nd, 2022

# Contributed to by Kyle Pannan, 19th July 2023


# New imports

from Calibrator import *
from SkillComposer import *

translator = Translator()

apps = ['Firmware Uploader', 'Joint Calibrator', 'Skill Composer']  # This is used in creating the buttons for other
# parts of the app, this needs to


# be rewritten


class UI:
    """
    This class is the main UI class, it is responsible for creating the main window and the buttons that are used to
    access the other parts of the app. It also contains the code that is used to create the buttons and the code that
    is used to create the window.
    """

    def __init__(self):
        self.logger = create_logger("UI", "UI", "UI_", "DEBUG")

        self.logger.info("Initializing UI")
        self.logger.debug("Initializing Config")

        self.config = Config()

        self.logger.debug("Config Initialised")

        self.logger.debug("Initializing Translator")  # This is used to translate the UI into different languages
        self.translator = Translator()
        self.logger.debug("Translator Initialised")

        self.start()

    def start(self):
        """
        This function is used to start the UI.
        """
        self.logger.debug("Initializing Window")
        self.window = Tk()

        osName = self.window.call('tk', 'windowingsystem')  # This gets the current os name so that the UI can
        # be adjusted for the OS that it is running on. There is definitely a better way to do this but I don't know
        # what it is.

        if osName == 'win32':
            self.window.iconbitmap(r'./resources/Petoi.ico')
            self.window.geometry('398x270+800+400')
        else:
            self.window.geometry('+800+400')
            self.backgroundColor = 'gray'  # This is unused

        self.myFont = tkFont.Font(family='Times New Roman', size=20, weight='bold')  # This does not need to be a property
        # of the class
        self.window.title(translator.getTranslation(self.config.language, 'uiTitle'))
        self.createMenu()
        self.modelLabel = Label(self.window, text=model, font=self.myFont)
        self.modelLabel.grid(row=0, column=0, pady=10)

        for i in range(len(apps)):  # What the fuck is this trying to do
            Button(self.window, text=translator.getTranslation(self.config.language, apps[i]), font=self.myFont,
                   fg='blue', width=23, relief='raised',
                   command=lambda app=apps[i]: self.utility(app)).grid(row=1 + i, column=0, padx=10, pady=(0, 10))

        self.ready = True
        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.window.update()

        self.window.resizable(False, False)
        self.window.mainloop()

    def createMenu(self):
        self.menubar = Menu(self.window, background='#ff8000', foreground='black', activebackground='white',
                            activeforeground='black')
        file = Menu(self.menubar, tearoff=0, background='#ffcc99', foreground='black')

        for key in NaJoints:
            file.add_command(label=key, command=lambda model=key: self.changeModel(model))

        self.menubar.add_cascade(label=self.translator.getTranslation(self.config.language, 'Model'), menu=file)

        lan = Menu(self.menubar, tearoff=0)

        for l in translator.languages:  # This is used to create the language menu
            lan.add_command(label=translator.getTranslation(l, "lanOption"),
                            command=lambda lanChoice=l: self.changeLan(lanChoice))

        self.menubar.add_cascade(label=self.translator.getTranslation(self.config.language, 'lanMenu'), menu=lan)

        helpMenu = Menu(self.menubar, tearoff=0)
        helpMenu.add_command(label=self.translator.getTranslation(self.config.language, 'About'),
                             command=self.showAbout)
        self.menubar.add_cascade(label=self.translator.getTranslation(self.config.language, 'Help'), menu=helpMenu)

        self.window.config(menu=self.menubar)

    def changeModel(self, modelName):
        global model
        model = copy.deepcopy(modelName)
        self.modelLabel.configure(text=model)


    def changeLan(self, newLanguage):  # Changes the window language
        """
        This function is used to change the language of the UI. It takes in a language code and then changes the UI to
        that language.

        Args:
            newLanguage (str): The language code of the language that the UI should be changed to.
        """
        # Check to make sure that the UI is not already in the language that is being requested. The check is done here
        # as it makes the code more readable to have it here.
        if newLanguage == self.config.language:
            self.logger.warning(f"Attempted to change language to {newLanguage} when already in that language")
            return

        # Check if the language that is being requested is a valid language code
        elif newLanguage not in translator.languages:
            self.logger.error(f"Attempted to change language to {newLanguage} which is not a valid language code")
            return

        else:
            self.logger.info(f"Changing language to {newLanguage}")
            self.config.language = newLanguage

            self.menubar.destroy()
            self.createMenu()
            self.window.title(translator.getTranslation(self.config.language, 'uiTitle'))

            for i in range(len(apps)):  # I have no idea what this is trying to do but it does not work
                self.window.winfo_children()[1 + i].config(
                    text=self.translator.getTranslation(self.config.language, apps[i]))

    def utility(self, app):
        self.window.destroy()

        if app == 'Firmware Uploader':
            Uploader(self.translator, self.config)
        elif app == 'Joint Calibrator':
            Calibrator(self.translator, self.config)
        elif app == 'Skill Composer':
            SkillComposer(self.translator, self.config)
        elif app == 'Task Scheduler':
            pass

    def showAbout(self):
        messagebox.showinfo('Petoi Desktop App',
                            u'Petoi Desktop App\nOpen Source on GitHub\nCopyright © Petoi LLC\nwww.petoi.com')

    def on_closing(self):
        if messagebox.askokcancel(self.translator.getTranslation(self.config.language, 'Quit'),
                                  self.translator.getTranslation(self.config.language, 'Do you want to quit?')):
            self.window.destroy()


if __name__ == '__main__':
    UI()
