# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# cars = [car0,car1,car2]

# for car in cars:
#     print(f"{car['model'].title()} {car['rang']} rang"
#           f"{car['yil']}-yil, {car['narh']}$")

# print(cars[0]['model'])

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(til.upper(), end=' ')

# **********AMALIYOT**********

shaxs0  = {
    'ism':"Abu abdulloh Muhammad ibn ismoil",
    'tyili':818,
    'shahar':"buxoro",
    'yoshi': 60,
    'asarlari':['al-jome as-sahih','al-adab al-mufrat','at-tarix as-sag`ir']
}

shaxs1 = {
    "ism":'Abdulla Qodiriy',
    'tyili':1894,
    'shahar':'toshkent',
    'yoshi':44,
    'asarlari':['otkan kunlar','mehrobdan chayon','obit ketmon']
}
shaxs2 = {
    'ism': 'erkin vohidov',
    'tyili':1936,
    'shahar':'farg`ona',
    'yoshi': 80,
    'asarlari':['tong nafasi','qoshiqlarim siri','o`zbegim','qiziquvchan matmusa']
}

shaxs3 = {
    'ism':'Alisher navoiy',
    'tyili':1441,
    'shahar':'xirot',
    'yoshi':60,
    'asarlari':['Xamsa','lison ut-tayr','mahbub ul-qulub']
}


greet_humans = [shaxs0,shaxs1,shaxs2,shaxs3]

for x in greet_humans:
    print(f"{x['ism'].title()} {x['tyili']}-yilda {x['shahar'].title()}da tavallud topgan.{x['yoshi']} yil umr ko`rgan")
    for asar in x['asarlari']:
        print(asar.title())