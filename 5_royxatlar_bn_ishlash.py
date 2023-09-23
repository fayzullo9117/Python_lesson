# cars = ["Malibu","Spark","Damas","Audi","Coblt"]
# print(sorted(cars, reverse=True))
# # cars.sort()
# print(cars)

# cars.reverse()
# print(cars)

# raqamlar = list(range(10))
# print(min(raqamlar))
# print(max(raqamlar))
# print(sum(raqamlar))
# print(len(raqamlar))
# print(raqamlar)
# print(raqamlar[0:3])
# raqamlar2 = raqamlar[:]
# raqamlar2.append(10)
# raqamlar2.append(11)
# print(raqamlar)
# print(raqamlar2)

# Tuples

# pifagor = (3,4,5)
# print(pifagor)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# toys = list(toys)

# toys.append('dragon')
# toys.remove('bus')

# toys[1] = 'mcqueen'

# toys = tuple(toys)

# print(toys)

# AMALIYOT
# countries = ['Anglya','Germaniya','Rassiya','Turkiya','Azarbayjan','Koreya','Italiya']
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries,reverse=True))
# print(countries)
# countries.reverse()
# print(countries)

# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# couple = list(range(120,1201,2))
# print(couple)
# print(sum(couple))
# print(max(couple) - min(couple))
# print(len(couple))
# print(couple[:20])
# print("****************************************")
# print(couple[-20:])
# print("****************************************")
# print(couple[530:550])
# print("****************************************")

dishes = ['do`lma','sho`rva','dimlama','shashlik','palov']

breakfast = dishes[:]

breakfast.append("quymod")
breakfast.append("tuxum")
print(dishes)
print(breakfast)

breakfast = tuple(breakfast)
# tuple tipidagi ro'yxat turini o`zgartirib bo`lmaydi
# breakfast[0] = 'qaymoq va non'