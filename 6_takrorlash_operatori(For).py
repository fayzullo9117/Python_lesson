# guests = ['Ali','Vali','Qodirali','Odil','Nusrat','Hamid','Obit','Sobit']
# for guest in guests:
#     print(guest)

# numbers = list(range(1,11))
# square_of_numbers = []
# for num in numbers:
#     # print(f"{num} ning kvadrati {num**2} ga teng")
#     square_of_numbers.append(num**2)

# print(square_of_numbers)
# print(numbers)

# names = ['Salim','Olim','Odil','Qodir','Sobit']
# n = 0
# for name in names:
#     print(f"Assalom alekum {name}.Siz talaba bo`ldingiz tabriklaymiz!")
#     n+=1
# print(f"Kod {n} marta takrorlandi")

# for num in range(11,100,2):
#     print(num**3)
# cinema = []
# print("Sevimli 5 kinoyingiz nomini kiriting:")
# for x in range(1,6):
#     kino_name = input(f"{x} - kino: ")
#     cinema.append(kino_name)
# print(cinema)

num = int(input("Bugun nechta odam bilan suhbat qildingiz: "))
names = []
for x in range(1,num+1):
    name = input(f"{x} - suhbat qilgan odamingiz kim edi: ")
    names.append(name)
print(names)