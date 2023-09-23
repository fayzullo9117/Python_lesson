# car = {
#     'model':'BMW',
#     'color':'blue',
#     'year':2022,
#     'oil':['benzin','dizel','gaz']
# }

# print(car['year'])
# print(car['model'])

# BO`SH LUG`AT

# talaba = {}

# talaba['ism'] = 'qobil rasulov'
# talaba['kurs'] = '4'
# talaba['yosh'] = 21
# print(talaba)
# talaba['kurs'] = 3
# print(f"Talaba {talaba['ism'].title()} {talaba['kurs']}-kurs")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# phone = telefonlar['ali']
# print(f"Alining telefon raqami {phone}")

# phone = telefonlar.get('vali','Bunday ism mavjud emas')
# print(phone)
# phone1 = telefonlar.get('hasan')
# print(phone1)

# ************AMALIYOT***********

# 1
# friend = {
#     'name':'Mansurov obid',
#     'age':21,
#     'job':'student',
#     'manzil': 'Fargona vil'
# }

# print(f"Do`stimning ismi {friend['name'].title()}, yoshi {friend['age']},U {friend['manzil']} da yashaydi.Uning kasbi {friend['job']}")

# 2
# foods = {
#     'ali':'qozon kabob',
#     'vali':'palov',
#     'gani':'besh barmoq',
#     'salim':'xonim',
#     'karim': 'lag`mon'    
# }
# print(f"Alining sevimli taomi {foods['ali'].title()}")
# print(f"Alining sevimli taomi {foods['vali'].title()}")
# print(f"Alining sevimli taomi {foods['salim'].title()}")

# 3
python_dict = {
    'int':"Butun sonlar to`plami",
    'float':'Haqiqiy sonlar to`plami',
    'string':'Belgilar toplami',
    'if_else':'Shart operatori',
    'for':'Takrorlash operator'
}

word = input("Kalit so`zni kiriting: ")
print(python_dict.get(word,"Bunday so`z mavjud emas!"))

if word in python_dict:
    print(f"{word} - {python_dict[word]} ")
else:
    print("Bunday so`z mavjud emas!")
    



