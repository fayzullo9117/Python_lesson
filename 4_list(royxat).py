# mevalar = ['olma','anor','behi','anjir']
# raqamlar = [1,2,3,4,5,6,7,8,9,0]
# mix = ['salom',2,'%',12,'@']
# # print(mevalar)
# # print(raqamlar)
# # print(type(mix[2]))

# raqamlar[9] = 10
# # print(raqamlar)
# raqamlar.append(0)
# # print(raqamlar)

# cars = []

# cars.append("Lasetti")
# cars.append("Nexia 3")
# cars.append("Coblt")
# cars.insert(0,"Malibu")
# cars.insert(1,"Matiz")
# print(cars)
# del cars[0]
# cars.remove("Nexia 3")
# print(cars)

# AMALIYOT

# names = []

# names.append("Sardor")
# names.append("Sobir")
# names.append("Sarvar")
# names.insert(0,"Hamid")
# names.insert(1,"Holmat")
# names.insert(2,"Hoshim")
# print(names)

# # ##########################

# print(f"Salom {names[2]} ishlaring yaxshimi")
# print(f"Assalom Alekum {names[4]} Juma ayyomingiz muborak bo`lsin")
# print(names[5], "ertaga darsga borasanmi")

# # ##########################

# numbers = [12,2,-34,1.2,3,-4,4.5]

# print(numbers[2] + numbers[3])

# numbers[0] = numbers[3] + numbers[4]
# print(numbers)

# # #########################

# t_shaxslar = ["Temur","To`xtasin","To`lqin","Turobjon"]
# z_shaxslar = ["Zoxid","Zafar","Zarb","Zoyir","Zaynob"]

# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(0)

# print(f"Men t_shaxslarodan {t_shaxs} bilan,\nz_shaxslardan esa {z_shaxs} bilan \nsuhbatlashishni istar edim")

friends = []
friends.append("Salim")
friends.append("Qodirali")
friends.append("Odil")
friends.append("Sobir")
friends.append("Donoyor")

friends.remove("Salim")

friends.insert(0,"Avaz")
friends.insert(3,"Hamid")
friends.insert(-1,"Jalil")

guests = []

friend = friends.pop(1)
guests.append(friend)

friend = friends.pop(3)
guests.append(friend)

friend = friends.pop(4)
guests.append(friend)

print("Mehmonlar: ", guests)

print("Do`stlar: ", friends)
