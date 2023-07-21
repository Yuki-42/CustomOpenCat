"""
The firmware uploader is a GUI program to upload firmware to the board.
"""
from idlelib.tooltip import Hovertip

# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# Jason Wong
# Petoi LLC
# May.1st, 2022

# Rewritten by Kyle Pannan, 20th July 2023

from rewrite.utils import Translator, Config
from threading import Thread
from subprocess import check_call
from time import sleep as time_sleep
from tkinter import filedialog, ttk, Tk, Grid, StringVar, Menu, IntVar, N, E, S, W, Label, Button, Entry, messagebox, DISABLED, NORMAL, SUNKEN

import pathlib

from rewrite.utils import create_logger
from serialMaster.SerialCommunication import Communication
from serialMaster.ardSerial import connectPort, goodPorts, closeAllSerial, keepCheckingPort, portStrList, model

NyBoard_version_list = ['NyBoard_V1_0', 'NyBoard_V1_1', 'NyBoard_V1_2']
BiBoard_version_list = ['BiBoard_V0']


class Uploader:
    """
    The firmware uploader is a GUI program to upload firmware to the board.
    """

    def __init__(self, translator: Translator, config: Config):
        self.logger = create_logger("FirmwareUploader", "FirmwareUploaderLogs", "FirmwareUploader")

        self.logger.info("Initialising Uploader")

        self.logger.debug("Assigning variables")
        self.translator = translator
        self.config = config
        self.logger.debug("Variables assigned")

        connectPort(goodPorts, needTesting=False, needSendTask=False)
        closeAllSerial(goodPorts, clearPorts=False)
        self.win = Tk()
        self.OSname = self.win.call('tk', 'windowingsystem')
        self.shellOption = True
        self.win.geometry('+260+100')
        if self.OSname == 'aqua':
            self.backgroundColor = 'gray'
        else:
            self.backgroundColor = None

        if self.OSname == 'win32':
            self.shellOption = False
        self.win.resizable(False, False)
        self.bParaUpload = True
        self.bFacReset = False
        Grid.rowconfigure(self.win, 0, weight=1)
        Grid.columnconfigure(self.win, 0, weight=1)
        self.strProduct = StringVar()

        self.BittleNyBoardModes = list(map(lambda x: self.translator.getTranslation(self.config.language, x),
                                           ['Standard', 'RandomMind', 'Voice', 'Camera', 'Mind+']))
        self.NybbleNyBoardModes = list(
            map(lambda x: self.translator.getTranslation(self.config.language, x),
                ['Standard', 'RandomMind', 'Voice', 'Ultrasonic', 'RandomMind_Ultrasonic', 'Mind+']))
        self.BittleBiBoardModes = list(
            map(lambda x: self.translator.getTranslation(self.config.language, x), ['Standard']))
        self.NybbleBiBoardModes = list(
            map(lambda x: self.translator.getTranslation(self.config.language, x), ['Standard']))

        self.inv_txt = {v: k for k, v in self.translator.languageList[self.config.language]}  # Da fuck is this
        self.initWidgets()

        self.win.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.win.update()

        self.keepChecking = True
        thread = Thread(target=keepCheckingPort,
                        args=(goodPorts, lambda: self.keepChecking, False, self.updatePortlist))
        thread.daemon = True
        thread.start()
        self.win.mainloop()
        self.force_focus()  # force the main interface to get focus

    def buildMenu(self):
        self.menuBar = Menu(self.win)
        self.win.configure(menu=self.menuBar)

        if self.OSname == 'win32':
            self.win.iconbitmap(r'./resources/Petoi.ico')

        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label=self.translator.getTranslation(self.config.language, 'labAbout'),
                                  command=self.about)
        self.menuBar.add_cascade(label=self.translator.getTranslation(self.config.language, 'labHelp'),
                                 menu=self.helpMenu)

    def initWidgets(self):
        self.win.title(self.translator.getTranslation(self.config.language, 'uploaderTitle'))
        self.buildMenu()
        self.strFileDir = StringVar()
        self.strPort = StringVar()
        self.strStatus = StringVar()
        self.strSoftwareVersion = StringVar()
        self.strBoardVersion = StringVar()

        self.intMode = IntVar()
        self.strMode = StringVar()

        self.lastSetting = [model, self.config.path, strSwVersion, strBdVersion, mode]
        self.currentSetting = []

        self.logger.info(f"The firmware file folder is {self.config.path}")
        self.strFileDir.set(self.config.path)

        fmFileDir = ttk.Frame(self.win)
        fmFileDir.grid(row=0, columnspan=3, ipadx=2, padx=2, sticky=W + E + N + S)

        self.labFileDir = Label(fmFileDir, text=self.translator.getTranslation(self.config.language, 'labFileDir'),
                                font=('Arial', 16))
        self.labFileDir.grid(row=0, column=0, ipadx=2, padx=2, sticky=W)

        self.btnFileDir = Button(fmFileDir, text=self.translator.getTranslation(self.config.language, 'btnFileDir'),
                                 font=('Arial', 12), foreground='blue',
                                 background=self.backgroundColor, command=self.open_dir)  # bind open_dir function
        self.btnFileDir.grid(row=0, column=1, ipadx=5, padx=5, pady=5, sticky=E)

        self.entry = Entry(fmFileDir, textvariable=self.strFileDir, font=('Arial', 16), foreground='green',
                           background='white')
        self.entry.grid(row=1, columnspan=2, ipadx=5, padx=5, sticky=E + W)

        fmFileDir.columnconfigure(0, weight=8)  # set column width
        fmFileDir.columnconfigure(1, weight=1)  # set column width
        fmFileDir.rowconfigure(1, weight=1)

        fmProduct = ttk.Frame(self.win)
        fmProduct.grid(row=1, column=0, ipadx=2, padx=2, sticky=W)
        self.labProduct = ttk.Label(fmProduct, text=self.translator.getTranslation(self.config.language, 'labProduct'),
                                    font=('Arial', 16))
        self.labProduct.grid(row=0, column=0, ipadx=5, padx=5, sticky=W)

        cbProduct = ttk.Combobox(fmProduct, textvariable=self.strProduct, foreground='blue', font=12)
        # list of product
        cbProductList = ['Nybble', 'Bittle']
        # set default value of Combobox
        cbProduct.set(self.lastSetting[0])
        # set list for Combobox
        cbProduct['values'] = cbProductList
        cbProduct.grid(row=1, ipadx=5, padx=5, sticky=W)
        cbProduct.bind("<<ComboboxSelected>>", self.chooseProduct)

        fmSoftwareVersion = ttk.Frame(self.win)
        fmSoftwareVersion.grid(row=1, column=1, ipadx=2, padx=2, sticky=W)
        self.labSoftwareVersion = ttk.Label(fmSoftwareVersion, text=self.translator.getTranslation(self.config.language,
                                                                                                   'labSoftwareVersion'),
                                            font=('Arial', 16))
        self.labSoftwareVersion.grid(row=0, ipadx=5, padx=5, sticky=W)
        self.cbSoftwareVersion = ttk.Combobox(fmSoftwareVersion, textvariable=self.strSoftwareVersion,
                                              foreground='blue', font=12)
        self.cbSoftwareVersion.bind("<<ComboboxSelected>>", self.chooseSoftwareVersion)

        # list of software_version
        software_version_list = ['1.0', '2.0']
        # set default value of Combobox
        self.cbSoftwareVersion.set(self.lastSetting[2])

        # set list for Combobox
        self.cbSoftwareVersion['values'] = software_version_list
        self.cbSoftwareVersion.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmBoardVersion = ttk.Frame(self.win)
        fmBoardVersion.grid(row=1, column=2, ipadx=2, padx=2, sticky=W)
        self.labBoardVersion = ttk.Label(fmBoardVersion,
                                         text=self.translator.getTranslation(self.config.language, 'labBoardVersion'),
                                         font=('Arial', 16))
        self.labBoardVersion.grid(row=0, ipadx=5, padx=5, sticky=W)

        self.cbBoardVersion = ttk.Combobox(fmBoardVersion, textvariable=self.strBoardVersion, foreground='blue',
                                           font=12)
        self.cbBoardVersion.bind("<<ComboboxSelected>>", self.chooseBoardVersion)
        # list of board_version
        board_version_list = NyBoard_version_list + BiBoard_version_list
        # set default value of Combobox
        self.cbBoardVersion.set(self.lastSetting[3])
        # set list for Combobox
        self.cbBoardVersion['values'] = board_version_list
        self.cbBoardVersion.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmMode = ttk.Frame(self.win)
        fmMode.grid(row=2, column=0, ipadx=2, padx=2, pady=6, sticky=W)
        self.labMode = ttk.Label(fmMode, text=self.translator.getTranslation(self.config.language, 'labMode'),
                                 font=('Arial', 16))
        self.labMode.grid(row=0, column=0, ipadx=5, padx=5, sticky=W)

        if self.strProduct.get() == 'Bittle':
            if 'NyBoard' in self.strBoardVersion.get():
                cbModeList = self.BittleNyBoardModes
            else:
                cbModeList = self.BittleBiBoardModes
        elif self.strProduct.get() == 'Nybble':
            if 'NyBoard' in self.strBoardVersion.get():
                cbModeList = self.NybbleNyBoardModes
            else:
                cbModeList = self.NybbleBiBoardModes
        self.cbMode = ttk.Combobox(fmMode, textvariable=self.strMode, foreground='blue', font=12)
        # set default value of Combobox
        self.cbMode.set(self.translator.getTranslation(self.config.language, self.lastSetting[4]))
        # set list for Combobox
        self.cbMode['values'] = cbModeList
        self.cbMode.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmSerial = ttk.Frame(self.win)  # relief=GROOVE
        fmSerial.grid(row=2, column=1, ipadx=2, padx=2, pady=6, sticky=W)
        self.labPort = ttk.Label(fmSerial, text=self.translator.getTranslation(self.config.language, 'labPort'),
                                 font=('Arial', 16))
        self.labPort.grid(row=0, ipadx=5, padx=5, sticky=W)
        self.cbPort = ttk.Combobox(fmSerial, textvariable=self.strPort, foreground='blue', font=12)  # width=38,
        # list of serial port number
        port_number_list = []
        if len(portStrList) == 0:
            port_number_list = [' ']
            print("Cannot find the serial port!")
        else:
            self.logger.info(f"portStrList is {portStrList}")
            for p in portStrList:
                portName = p
                self.logger.debug(f"portName is {portName}")
                port_number_list.append(portName)
            self.logger.debug(f"port_number_list is {port_number_list}")
            self.cbPort.set(port_number_list[0])
        # set list for Combobox
        self.cbPort['values'] = port_number_list
        self.cbPort.grid(row=1, ipadx=5, padx=5, sticky=W)

        fmFacReset = ttk.Frame(self.win)  # relief=GROOVE
        fmFacReset.grid(row=2, column=2, ipadx=2, padx=2, pady=6, sticky=W + E)
        self.btnFacReset = Button(fmFacReset, text=self.translator.getTranslation(self.config.language, 'btnFacReset'),
                                  font=('Arial', 16, 'bold'), fg='red',
                                  relief='groove', command=self.factoryReset)
        self.btnFacReset.grid(row=0, ipadx=5, ipady=5, padx=9, pady=8, sticky=W + E + N + S)
        tip(self.btnFacReset, self.translator.getTranslation(self.config.language, 'tipFacReset'))
        fmFacReset.columnconfigure(0, weight=1)
        fmFacReset.rowconfigure(0, weight=1)

        fmUpload = ttk.Frame(self.win)
        fmUpload.grid(row=3, columnspan=3, ipadx=2, padx=2, pady=8, sticky=W + E + N + S)
        self.btnUpgrade = Button(fmUpload, text=self.translator.getTranslation(self.config.language, 'btnUpgrade'),
                                 font=('Arial', 16, 'bold'), foreground='blue',
                                 background=self.backgroundColor, relief='groove', command=self.upgrade)
        self.btnUpgrade.grid(row=0, column=0, ipadx=5, padx=5, pady=5, sticky=W + E)
        tip(self.btnUpgrade, self.translator.getTranslation(self.config.language, 'tipUpgrade'))
        self.btnUpdateMode = Button(fmUpload,
                                    text=self.translator.getTranslation(self.config.language, 'btnUpdateMode'),
                                    font=('Arial', 16, 'bold'), foreground='blue',
                                    background=self.backgroundColor, relief='groove', command=self.uploadeModeOnly)
        self.btnUpdateMode.grid(row=0, column=1, ipadx=5, padx=5, pady=5, sticky=W + E)
        Hovertip(self.btnUpdateMode, self.translator.getTranslation(self.config.language, 'tipUpdateMode'))
        fmUpload.columnconfigure(0, weight=1)
        fmUpload.columnconfigure(1, weight=1)
        fmUpload.rowconfigure(0, weight=1)

        fmStatus = ttk.Frame(self.win)
        fmStatus.grid(row=4, columnspan=3, ipadx=2, padx=2, pady=5, sticky=W + E + N + S)
        self.statusBar = ttk.Label(fmStatus, textvariable=self.strStatus, font=('Arial', 16), relief=SUNKEN)
        self.statusBar.grid(row=0, ipadx=5, padx=5, sticky=W + E + N + S)
        fmStatus.columnconfigure(0, weight=1)

    def uploadeModeOnly(self):
        self.bParaUpload = False
        self.bFacReset = False
        self.autoupload()

    def factoryReset(self):
        self.bParaUpload = True
        self.bFacReset = True
        self.autoupload()

    def upgrade(self):
        self.bParaUpload = True
        self.bFacReset = False
        self.autoupload()

    def updatePortlist(self):
        port_number_list = []
        if len(portStrList) == 0:
            port_number_list = [' ']
            print("Cannot find the serial port!")
        else:
            self.logger.info(f"portStrList is {portStrList}")
            for p in portStrList:
                portName = p
                self.logger.debug(f"{portName}")
                port_number_list.append(portName)
            self.logger.debug(f"port_number_list is {port_number_list}")
        self.cbPort.set(port_number_list[0])
        # set list for Combobox
        self.cbPort['values'] = port_number_list

    def about(self):
        self.msgbox = messagebox.showinfo(self.translator.getTranslation(self.config.language, 'titleVersion'),
                                          self.translator.getTranslation(self.config.language, 'msgVersion'))
        self.force_focus()

    def setActiveMode(self):
        if self.strSoftwareVersion.get() == '1.0':
            stt = DISABLED
            self.strMode.set(self.translator.getTranslation(self.config.language, 'Standard'))
            board_version_list = NyBoard_version_list
            self.strBoardVersion.set(board_version_list[-1])
        else:
            stt = NORMAL
            board_version_list = NyBoard_version_list + BiBoard_version_list
        # set list for Combobox
        self.cbBoardVersion['values'] = board_version_list
        self.cbMode.config(state=stt)

    def chooseSoftwareVersion(self, event):
        self.setActiveMode()

    def setActiveOption(self):
        if self.cbBoardVersion.get() in BiBoard_version_list:
            stt = DISABLED
            self.strSoftwareVersion.set('2.0')
        else:
            stt = NORMAL

        self.cbSoftwareVersion.config(state=stt)

    def chooseBoardVersion(self, event):
        self.setActiveOption()
        self.updateMode()

    def chooseProduct(self, event):
        self.updateMode()

    def updateMode(self):
        if self.strProduct.get() == 'Bittle':
            if 'NyBoard' in self.strBoardVersion.get():
                modeList = self.BittleNyBoardModes
            else:
                modeList = self.BittleBiBoardModes
        elif self.strProduct.get() == 'Nybble':
            if 'NyBoard' in self.strBoardVersion.get():
                modeList = self.NybbleNyBoardModes
            else:
                modeList = self.NybbleBiBoardModes
        self.cbMode['values'] = modeList

        if self.strMode.get() not in modeList:
            messagebox.showwarning(self.translator.getTranslation(self.config.language, 'Warning'),
                                   self.translator.getTranslation(self.config.language, 'msgMode'))
            # printH("modeList[0]:", modeList[0])
            self.strMode.set(modeList[0])
            self.force_focus()  # force the main interface to get focus

    def formalize(self, strdir=' '):
        sep = "/"
        listDir = strdir.split("/")
        if (strdir == str(pathlib.Path().resolve())):
            strdir = sep.join(listDir) + '/release'
        else:
            if (listDir[-1].find("release") == -1) and len(listDir) >= 2:
                while listDir[-1].find("release") == -1 and len(listDir) >= 2:
                    listDir = listDir[:-1]
                if listDir[-1] != "release":
                    strdir = " "
                else:
                    strdir = sep.join(listDir)
        self.strFileDir.set(strdir)

    def open_dir(self):
        # call askdirectory to open file director
        self.logger.debug(f"{self.strFileDir.get()}")
        if (self.strFileDir.get()).find(releasePath) != -1:
            initDir = releasePath
        else:
            initDir = self.strFileDir
        dirpath = filedialog.askdirectory(title=self.translator.getTranslation(self.config.language, 'titleFileDir'),
                                          initialdir=initDir)

        if dirpath:
            self.formalize(dirpath)
        self.force_focus()

    def encode(self, in_str, encoding='utf-8'):
        if isinstance(in_str, bytes):
            return in_str
        else:
            return in_str.encode(encoding)

    def WriteInstinctPrompts(self, port):
        ser = Communication(port, 115200, 0.5)
        self.logger.info(f"Connect to usb serial port: {port}.")
        strSoftwareVersion = self.strSoftwareVersion.get()
        promptJointCalib = {
            'message': self.translator.getTranslation(self.config.language, 'reset joints?'),
            'operating': self.translator.getTranslation(self.config.language, 'resetting joints'),
            'result': self.translator.getTranslation(self.config.language, 'joints reset'),
        }
        promptInstinct = {
            'message': self.translator.getTranslation(self.config.language, 'update instincts?'),
            'operating': self.translator.getTranslation(self.config.language, 'updating instincts'),
            'result': self.translator.getTranslation(self.config.language, 'instincts updated')
        }
        promptIMU = {
            'message': self.translator.getTranslation(self.config.language, 'calibrate IMU?'),
            'operating': self.translator.getTranslation(self.config.language, 'calibrating IMU'),
            'result': self.translator.getTranslation(self.config.language, 'IMU calibrated')
        }
        if strSoftwareVersion == '1.0':
            promptList = [promptJointCalib, promptInstinct, promptIMU]
        elif strSoftwareVersion == '2.0':
            promptList = [promptJointCalib, promptIMU]

        strBoardVersion = self.strBoardVersion.get()

        progress = 0
        retMsg = False
        counter = 0
        prompStr = ""
        while True:
            time_sleep(0.01)
            if ser.main_engine.in_waiting > 0:
                x = str(ser.main_engine.readline())
                prompStr = x[2:-1]
                self.logger.debug(f"new line:{x}")
                if x != "":
                    print(x[2:-1])
                    questionMark = "Y/n"
                    if x.find(questionMark) != -1:
                        if x.find("joint") != -1:
                            prompt = promptJointCalib
                        elif x.find("Instinct") != -1:
                            prompt = promptInstinct
                        elif x.find("Calibrate") != -1:
                            prompt = promptIMU
                        elif x.find("assurance") != -1:  # for BiBoard it need to be modified later
                            ser.Send_data(self.encode("n"))
                            continue
                        if progress > 0 and retMsg == True:
                            self.strStatus.set(promptList[progress - 1]['result'])
                            self.statusBar.update()
                        retMsg = messagebox.askyesno(self.translator.getTranslation(self.config.language, 'Warning'),
                                                     prompt['message'])
                        if retMsg:
                            self.strStatus.set(prompt['operating'])
                            self.statusBar.update()
                            ser.Send_data(self.encode("Y"))
                        else:
                            ser.Send_data(self.encode("n"))
                            if progress == len(promptList) - 1:
                                break
                        progress += 1
                    if not self.bFacReset:
                        if x.find("sent to mpu.setXAccelOffset") != -1 or x.find("Ready!") != -1:
                            self.strStatus.set(promptIMU['result'])
                            self.statusBar.update()
                            break
                    else:
                        if x.find("sent to mpu.setXAccelOffset") != -1 or x.find("Ready!") != -1:
                            self.strStatus.set(promptIMU['result'])
                            self.statusBar.update()
                            if strBoardVersion in BiBoard_version_list:  # for BiBoard it need to be modified later
                                break
                        elif x.find("Calibrated:") != -1:
                            self.strStatus.set(self.translator.getTranslation(self.config.language, '9685 Calibrated'))
                            self.statusBar.update()
                            break
            else:
                if self.bFacReset:
                    if prompStr.find("Optional: Connect PWM 3") != -1:
                        counter += 1
                        if counter == 10:
                            break

        ser.Close_Engine()
        self.logger.info("close the serial port.")
        self.force_focus()

    def autoupload(self):
        self.logger.info(f"lastSetting: {self.lastSetting}.")
        strProd = self.strProduct.get()
        self.config.path = self.strFileDir.get()
        strSoftwareVersion = self.strSoftwareVersion.get()
        strBoardVersion = self.strBoardVersion.get()
        strMode = self.inv_txt[self.strMode.get()]
        self.currentSetting = [strProd, self.config.path, strSoftwareVersion, strBoardVersion, strMode]
        self.logger.info(f"currentSetting: {self.currentSetting}.")

        if self.strFileDir.get() == '' or self.strFileDir.get() == ' ':
            messagebox.showwarning(self.translator.getTranslation(self.config.language, 'Warning'),
                                   self.translator.getTranslation(self.config.language, 'msgFileDir'))
            self.force_focus()  # force the main interface to get focus
            return False

        # NyBoard_V1_X software version are all the same
        if "NyBoard_V1" in strBoardVersion:
            pathBoardVersion = "NyBoard_V1"
        else:
            pathBoardVersion = strBoardVersion

        path = self.strFileDir.get() + '/' + strSoftwareVersion + '/' + strProd + '/' + pathBoardVersion + '/'

        if self.OSname == 'x11' or self.OSname == 'aqua':
            port = '/dev/' + self.strPort.get()
        else:
            port = self.strPort.get()
        print(self.strPort.get())
        if port == ' ' or port == '':
            messagebox.showwarning(self.translator.getTranslation(self.config.language, 'Warning'),
                                   self.translator.getTranslation(self.config.language, 'msgPort'))
            self.force_focus()
            return False

        if strBoardVersion in NyBoard_version_list:
            if self.bFacReset:
                fnWriteI = path + 'WriteInstinctAutoInit.ino.hex'
                fnOpenCat = path + 'OpenCatStandard.ino.hex'
                self.currentSetting[4] = 'Standard'
            else:
                fnWriteI = path + 'WriteInstinct.ino.hex'
                fnOpenCat = path + 'OpenCat' + strMode + '.ino.hex'
            filename = [fnWriteI, fnOpenCat]
            print(filename)
            uploadStage = ['Parameters', 'Main function']
            for s in range(len(uploadStage)):
                # if s == 0 and self.bParaUploaded and self.currentSetting[:4] == self.lastSetting[:4]:
                if s == 0 and (not self.bParaUpload):
                    continue
                self.strStatus.set(
                    self.translator.getTranslation(self.config.language, 'Uploading') + self.translator.getTranslation(
                        self.config.language, uploadStage[s]) + '...')
                self.win.update()
                # self.inProgress = True
                # status = self.translator.getTranslation(self.config.language, 'Uploading') + self.translator.getTranslation(self.config.language, uploadStage[s]) + '.'
                # t = threading.Thread(target=self.progressiveDots, args=(status,))
                # t.start()
                if self.OSname == 'win32':
                    avrdudePath = './resources/avrdudeWin/'
                elif self.OSname == 'x11':  # Linux
                    avrdudePath = '/usr/bin/'
                    path = pathlib.Path(avrdudePath + 'avrdude')
                    if not path.exists():
                        messagebox.showwarning(self.translator.getTranslation(self.config.language, 'Warning'),
                                               self.translator.getTranslation(self.config.language, 'msgNoneAvrdude'))
                        self.force_focus()  # force the main interface to get focus
                        return False
                    # avrdudeconfPath = '/etc/avrdude/'      # Fedora / CentOS
                    avrdudeconfPath = '/etc/'  # Debian / Ubuntu
                else:
                    avrdudePath = './resources/avrdudeMac/'
                print()
                try:
                    if self.OSname == 'x11':  # Linuxself.OSname == 'x11':     # Linux
                        check_call(
                            avrdudePath + 'avrdude -C' + avrdudeconfPath + 'avrdude.conf -v -V -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                            (port, filename[s]), shell=self.shellOption)
                    else:
                        check_call(
                            avrdudePath + 'avrdude -C' + avrdudePath + 'avrdude.conf -v -V -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i' % \
                            (port, filename[s]), shell=self.shellOption)
                # self.inProgress = False
                except:
                    status = self.translator.getTranslation(self.config.language,
                                                            uploadStage[s]) + self.translator.getTranslation(
                        self.config.language, 'failed to upload')
                    self.strStatus.set(status)
                    self.statusBar.update()
                    messagebox.showwarning(self.translator.getTranslation(self.config.language, 'Warning'),
                                           self.translator.getTranslation(self.config.language, 'Replug prompt'))
                    return False
                else:
                    status = self.translator.getTranslation(self.config.language,
                                                            uploadStage[s]) + self.translator.getTranslation(
                        self.config.language, 'is successully uploaded')

                self.strStatus.set(status)
                self.statusBar.update()

                if s == 0:
                    self.WriteInstinctPrompts(port)
                    if not self.bFacReset:
                        messagebox.showinfo(title=None, message=self.translator.getTranslation(self.config.language,
                                                                                               'parameterFinish'))
                    else:
                        pass
                else:
                    pass
        elif strBoardVersion in BiBoard_version_list:
            # fnBootLoader = path + 'OpenCatEsp32Standard.ino.bootloader.bin'
            fnBootLoader = path + 'OpenCatEsp32' + strMode + '.ino.bootloader.bin'
            # fnPartitions = path + 'OpenCatEsp32Standard.ino.partitions.bin'
            fnPartitions = path + 'OpenCatEsp32' + strMode + '.ino.partitions.bin'
            fnBootApp = path + 'boot_app0.bin'
            # fnMainFunc = path + 'OpenCatEsp32Standard.ino.bin '
            fnMainFunc = path + 'OpenCatEsp32' + strMode + '.ino.bin '

            filename = [fnBootLoader, fnPartitions, fnBootApp, fnMainFunc]
            print(filename)
            self.strStatus.set(
                self.translator.getTranslation(self.config.language, 'Uploading') + self.translator.getTranslation(
                    self.config.language, 'Main function') + '...')
            self.win.update()
            if self.OSname == 'win32':
                esptoolPath = './resources/esptoolWin/'
            else:
                esptoolPath = './resources/esptoolMac/'
            print()
            try:
                check_call(
                    esptoolPath + 'esptool --chip esp32 --port %s --baud 921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio --flash_freq 80m --flash_size 16MB 0x1000 %s 0x8000 %s 0xe000 %s 0x10000 %s' % \
                    (port, filename[0], filename[1], filename[2], filename[3]), shell=self.shellOption)
            except:
                status = self.translator.getTranslation(self.config.language,
                                                        'Main function') + self.translator.getTranslation(
                    self.config.language, 'failed to upload')
                self.strStatus.set(status)
                self.statusBar.update()
                return False
            else:
                status = self.translator.getTranslation(self.config.language,
                                                        'Main function') + self.translator.getTranslation(
                    self.config.language, 'is successully uploaded')

            self.strStatus.set(status)
            self.statusBar.update()
            self.WriteInstinctPrompts(port)

        self.lastSetting = self.currentSetting
        if self.bFacReset:
            self.strMode.set(self.translator.getTranslation(self.config.language, 'Standard'))

        print('Finish!')
        messagebox.showinfo(title=None, message=self.translator.getTranslation(self.config.language, 'msgFinish'))
        self.force_focus()  # force the main interface to get focus
        return True

    def force_focus(self):
        self.win.after(1, lambda: self.win.focus_force())

    def on_closing(self):
        if messagebox.askokcancel(self.translator.getTranslation(self.config.language, 'Quit'),
                                  self.translator.getTranslation(self.config.language, 'Do you want to quit?')):
            self.win.destroy()
