"""
This file contains all the common variables and functions used in the UI.
"""

# New Code
from sys import path, version

path.append('../serialMaster/')
resourcePath = './resources/'
releasePath = './release'
path.append(resourcePath)
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import platform
import os

NyBoard_version = 'NyBoard_V1_2'
verNumber = version.split('(')[0].split()[0]
verNumber = verNumber.split('.')
print(verNumber)
# verNumber = [2,1,1] #for testing
supportHoverTip = True

if int(verNumber[0]) < 3 or int(verNumber[1]) < 7:
    print("Please upgrade your Python to 3.7.1 or above!")
    root = Tk()
    root.overrideredirect(1)
    root.withdraw()
    messagebox.showwarning(title='Warning', message='Please upgrade your Python\nto 3.7.1 or above\nto show hovertips!')
    root.destroy()
    supportHoverTip = False
#    exit(0)

try:
    from idlelib.tooltip import Hovertip
except Exception as e:
    raise e

NaJoints = {
    'Nybble': [3, 4, 5, 6, 7],
    'Bittle': [1, 2, 3, 4, 5, 6, 7],
    'DoF16': []
}
scaleNames = [
    'Head Pan', 'Head Tilt', 'Tail Pan', 'N/A',
    'Shoulder', 'Shoulder', 'Shoulder', 'Shoulder',
    'Arm', 'Arm', 'Arm', 'Arm',
    'Knee', 'Knee', 'Knee', 'Knee']
sideNames = ['Left Front', 'Right Front', 'Right Back', 'Left Back']

ports = []


def mkdir(path):
    """
    This is shit.
    """
    # delete spaces in the path string
    path = path.strip()
    # delete the '\' at the end of path string
    path = path.rstrip("\\").rstrip("/")
    # path = path.rstrip("/")

    # check whether the path exists
    isExists = os.path.exists(path)

    if not isExists:
        # Create the directory if it does not exist
        os.makedirs(path)
        print(path + ' creat successfully')
        return True
    else:
        # If the directory exists, it will not be created and prompt that the directory already exists.
        print(path + ' already exists')
        return False


if platform.system() == "Windows":  # for Windows
    seperation = '\\'
    homeDri = os.getenv('HOMEDRIVE')
    homePath = os.getenv('HomePath')
    configDir = homeDri + '\\' + homePath

else:  # for Linux & macOS
    seperation = '/'
    home = os.getenv('HOME')
    configDir = home

# This is shit and needs to be removed, you should only be storing files inside the project. Storing them in hidden
# places like .config just confuses the user and polutes their system
configDir = configDir + seperation + '.config' + seperation + 'Petoi'
mkdir(configDir)
defaultConfPath = configDir + seperation + 'defaultConfig.txt'
print(defaultConfPath)


def createImage(frame, imgFile, imgW):
    img = Image.open(imgFile)
    ratio = img.size[0] / imgW
    img = img.resize((imgW, round(img.size[1] / ratio)))
    image = ImageTk.PhotoImage(img)
    imageFrame = Label(frame, image=image)
    imageFrame.image = image
    return imageFrame


def tip(item, note):
    if supportHoverTip:
        Hovertip(item, note)
#    else:
#        print(note)
