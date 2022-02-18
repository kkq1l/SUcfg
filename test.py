#converting steam id
ID64 = 76561198133783003

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

#copy u cfg
import shutil
path = path+r'\userdata/'+str(ID3)+'/730/local/cfg/config.cfg'
shutil.copyfile(path,"asd.cfg")