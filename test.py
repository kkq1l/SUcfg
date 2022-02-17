#converting steam id64 to id3
ID64 = 76561198133783003

y = int(ID64) - 76561197960265728
x = y % 2

ID3 = (((y - x) // 2) * 2) + x

print(ID3)

