# num = 1
# while num <= 5:
#     print(num,end=' ')
#     num += 1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Yoqtirgan kitoblaringiz nomini kiriting \nva yakunlasj uchun stop so`zini yozing")
# qiymat = ''
# num = 1
# while qiymat.lower() != 'stop':
#     qiymat = input()

print("Chipta narxini bilish uchun yoshingizni kiriting: ")
value = ''
while value != 'exit' or value != 'quit':
    value = input()
    if int(value) > 0:
        if int(value) < 7:
            print("7 yoshgacha bolalar uchun chipta narxi 2000 so`m")
        elif int(value) >= 7 and int(value) < 18:
            print("7 yoshdan 18 yosh oraligidagi bolalar uchun chipta narxi 3000 so`m")
        elif int(value) >= 18 and int(value) < 65:
            print("18 yoshdan 65 yosh oralig`idagilar uchun chipta narxi 10000 so`m")
        else:
            print("65 yoshdan yuqori yoshdagilar uchun chipta narxi bepul")
    else:
        print("Xatolik kuzatildi iltimos boshqa qiymat kiriting")
