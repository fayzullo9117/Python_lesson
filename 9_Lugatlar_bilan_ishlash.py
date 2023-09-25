# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")

# **********AMALIYOT**********

# 1
# python_dict= {
#     'integer':'butun son',
#     'float':'o`nlik son',
#     'if':'shartni tekshirish operatori',
#     'for':'biror amalni qayta qayta bajarish sikli',
#     'bool':'mantiqiy ifoda',
#     'print':'chop etish operatori',
#     'input':'kiritish operatori',
#     'def':'funksiya elon qilish',
#     'list':'ro`yxat'
# }

# for key, value in sorted(python_dict.items()):
#     print(f"{key.title()} - {value}")

# 2

# states = {
#     'aqsh':'washinton',
#     'uzbekiston':'Toshkent',
#     'rossiya':'moskva',
#     'italiya':'rim',
#     'singapur':'sungapur',
#     'tojikiston':'bishkek',
#     'malayziya':'kuala-Lumpur'
# }

# for davlat, poytaxt in sorted(states.items()):
#     print(f"{davlat.title()} - {poytaxt.title()}")

# 3
# states = {
#     'aqsh':'washinton',
#     'uzbekistan':'Toshkent',
#     'rossiya':'moskva',
#     'italiya':'rim',
#     'singapur':'sungapur',
#     'tojikiston':'bishkek',
#     'malayziya':'kuala-Lumpur'
# }
# x = input("Qaysi davlatning poytaxtini bilishni xohlaysiz? ")

# if x in states.keys(): 
#     print(f"{x.title()} ning poytaxti {states[x].title()}")
# else:
#     print("Kechirasiz bizda bunday ma`lumot yo`q")


# 4

menu = {
    'non':5000,
    'choy':5000,
    'palov': 30000,
    'manti':7000,
    'shashlik':15000,
    'sho`rva':25000,
    'moshho`rda':27000,
    'mastava':25000,
    'bishteks':25000,
    'somsa':9000
}
key = []
print("3-xil taom tanlang: ")
for x in range(1,4):
    food = input(f"{x} - taom ")
    key.append(food)

for food in key:
    if food in menu.keys():
        print(f"{food} - {menu[food]}")
    else:
        print("Kechirasiz bizda bunday taom yo`q! ")
    
print(f"Jami:{sum}")