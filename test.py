from urllib import request
from PyQt5 import uic
from PyQt5.QtWidgets import *
import winreg
from winreg import *
import shutil
import os

Form, Window = uic.loadUiType("GUI.ui")
def msgBox(x,y):
    msg = QMessageBox()
    msg.setWindowTitle(x)
    msg.setText(y)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def serchPathSteam():
    # where installing steam
    try:
        aKey = r"SOFTWARE\Valve\Steam"
        aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, aKey)
        steam_path = winreg.QueryValueEx(aKey, "SteamPath")
        path = steam_path[0]

        return path
    except FileNotFoundError:
        msgBox("Error", "not found software in U PC")
def userDataID():
    dirname = serchPathSteam() + '/userdata'
    files = os.listdir(dirname)
    return files

def userList():
    files=userDataID()
    arrUserName = [0] * len(files)

    for i in range(0, len(files)):
        asd = int(files[i]) + 76561197960265728
        url = 'https://steamcommunity.com/profiles/' + str(asd)
        html = request.urlopen(url).read().decode('utf8')
        start = html.find('<title>') + 7
        end = html.find('</title>', start)
        title = html[start:end]
        s1 = (title.replace("Steam Community :: ", ""))
        arrUserName[i] = s1
        form.comboBox.insertItem(i, s1)
        form.comboBox_2.insertItem(i, s1)
    return files


def copyConfig():
    # copy u cfg
    files=userDataID()
    if(form.comboBox.currentIndex()!=form.comboBox_2.currentIndex()):
        if (form.radioButton_2.isChecked() == True):
            try:
                path = serchPathSteam() + r'\userdata/' + str(files[form.comboBox.currentIndex()]) + '/730/local/cfg/config.cfg'
                shutil.copyfile(path, "MyConfig.cfg")
                msgBox("Yah", "All done")
            except FileNotFoundError:
                msgBox("Error","not found this user")
        else:
            try:
                video = serchPathSteam() + r'\userdata/' + str(files[form.comboBox.currentIndex()]) + '/730/local/cfg/video.txt'
                config = serchPathSteam() + r'\userdata/' + str(files[form.comboBox.currentIndex()]) + '/730/local/cfg/config.cfg'
                shutil.copyfile(video, serchPathSteam() + r'\userdata/' + str(files[form.comboBox_2.currentIndex()]) + '/730/local/cfg/video.txt')
                shutil.copyfile(config, serchPathSteam() + r'\userdata/' + str(files[form.comboBox_2.currentIndex()]) + '/730/local/cfg/config.cfg')
                msgBox("Yah","All done")
            except FileNotFoundError:
                msgBox("Error","not found this user")
    else:
        msgBox("Error","u cant copy, choose another account")


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
userList()
form.radioButton_2.setChecked(True)
form.pushButton.clicked.connect(copyConfig)
app.exec_()


