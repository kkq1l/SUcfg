#converting steam id64 to id3
ID64 = 76561198133783003

y = int(ID64) - 76561197960265728
x = y % 2

ID3 = (((y - x) // 2) * 2) + x

print(ID3)

impsys
impwinreg
>>>
>>>
try:
h= winreg.OpenKey(winreg.HKEY_LOCAL_MACHI"SOFTWARE\WOW6432Node\Valve\Steam")
except:
h= None
print(sys.exc_info())
...
hkey
<PyHobjat 0x00000154FF5D0390>
>>>
try:
steam_p= winreg.QueryValueEx(hk"InstallPath")
except:
steam_p= None
print(sys.exc_info())
...
steam_path
('C:\\ProgFi(x86)\\Stea1)
steam_path[0]
'C:\\ProgFi(x86)\\Steam'
steam_path== winreg.REG_SZ
True
>>>
winreg.CloseKey(hkey)