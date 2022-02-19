from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCloseEvent
import winreg
from winreg import *
import re
import shutil
import os
Form, Window = uic.loadUiType("untitled.ui")

def accsesClick():
    try:
        int(form.lineEdit.text())
        copyConfig()
    except:
        form.lineEdit.setText('error where u id64?')


def copyConfig():
    # converting steam id
    ID64 = int(form.lineEdit.text())
    y = int(ID64) - 76561197960265728
    x = y % 2
    ID3 = (((y - x) // 2) * 2) + x

    # where installing steam
    try:
        aKey = r"SOFTWARE\Valve\Steam"
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, aKey)
        steam_path = winreg.QueryValueEx(aKey, "SteamPath")
        path = steam_path[0]
    except FileNotFoundError:
        form.lineEdit.setText("not found software in U PC")

    # search path to CS:GO
    document_text = open(steam_path[0] + r'\steamapps\libraryfolders.vdf', 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    inputAccses = 0
    count = 0
    pathGame = [''] * 10
    accsesDisk = 0

    for word in match_pattern:
        if (word == 'label'):
            inputAccses = 0
            accsesDisk = 0
        elif (inputAccses == 1):
            if (accsesDisk == 1):
                pathGame[count - 1] += str(word) + ':/'
                accsesDisk = 0
            else:
                pathGame[count - 1] += str(word) + '/'
        elif (word == 'path'):
            accsesDisk = 1
            inputAccses = 1
            count += 1


    # search correct path to CS:GO
    i = 0
    while i < 10:
        fileName = pathGame[i] + 'steamapps\common\Counter-Strike Global Offensive/csgo.exe'
        if (os.path.isfile(fileName) == True):
            form.pathIndex = i
            break
        i += 1

    # copy u cfg
        if (form.radioButton.isChecked() == False):
            try:
                path = path + r'\userdata/' + str(ID3) + '/730/local/cfg/config.cfg'
                shutil.copyfile(path, "MyConfig.cfg")
            except FileNotFoundError:
                form.lineEdit.setText("not found this user")
        else:
            try:
                path = path + r'\userdata/' + str(ID3) + '/730/local/cfg/config.cfg'
                shutil.copyfile(path, pathGame[form.pathIndex] + 'steamapps/common/Counter-Strike Global Offensive/csgo/cfg/'+'MyConfig.cfg')
                form.lineEdit.setText('Done!')
            except FileNotFoundError:
                form.lineEdit.setText("not found this user")


app = QApplication([])
window = Window()
form = Form()
form.pathIndex=0
form.setupUi(window)
window.show()
form.radioButton.setChecked(True)
form.pushButton.clicked.connect(accsesClick)
app.exec_()





