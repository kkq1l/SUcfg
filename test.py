#converting steam id
ID64 = 76561198191542870

y = int(ID64) - 76561197960265728
x = y % 2

ID3 = (((y - x) // 2) * 2) + x

print(ID3)


#where installing steam
import winreg
from winreg import *

aKey = r"SOFTWARE\Valve\Steam"
aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
aKey = OpenKey(aReg, aKey)
steam_path = winreg.QueryValueEx(aKey, "SteamPath")
path=steam_path[0]
print((steam_path[0]))

#search path to CS:GO
import re
document_text = open(steam_path[0]+r'\steamapps\libraryfolders.vdf', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

inputAccses=0
count=0
pathGame=['']*10
accsesDisk=0

for word in match_pattern:
    if (word == 'label'):
        inputAccses = 0
        accsesDisk=0
    elif(inputAccses==1):
        if(accsesDisk==1):
            pathGame[count-1]+=str(word)+':/'
            accsesDisk=0
        else:
            pathGame[count - 1] += str(word) + '/'
    elif (word == 'path'):
        accsesDisk=1
        inputAccses = 1
        count += 1

print(pathGame)

#search correct path to CS:GO
import os
i=0
while i<10:
    fileName = pathGame[i] + 'steamapps\common\Counter-Strike Global Offensive/csgo.exe'
    if (os.path.isfile(fileName) == True):
        pathIndex=i
        break
    i+=1



#copy u cfg
try:
    import shutil
    path = path+r'\userdata/'+str(ID3)+'/730/local/cfg/config.cfg'
    shutil.copyfile(path, "MyConfig.cfg")
except FileNotFoundError:
    print("not found this user")



