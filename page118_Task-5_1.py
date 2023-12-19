'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#TASK = 5.1, 5.1a, 5.1b, 5.1c, 5.1d
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
        },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
        },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

list_of_keys = list(london_co.keys())
list_of_keys_device = list(london_co["r1"].keys())

device = input("Input device {} :".format(list_of_keys))
device = device.lower()

character = input("Input character of the device, one of {} :".format(list_of_keys_device))
character = character.lower()

print(device not in list_of_keys, " => Device was not found in device list")
print(device not in list_of_keys_device, " => Character was not found in characters of device")
print("\n Device is=>", device, "\n Character is=>", character, " =", london_co[device][character])