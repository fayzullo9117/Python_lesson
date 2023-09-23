matn = "Men onamga ✄ sotib oldim"
print(matn)
matn = "Bu yil ❆ erta yog`di"
print(matn)

ism = 'Samar'
familiya = "Omonov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
# print(ism_sharif(capitalize())) Faqat satr boshidagi so`zning birinchi harfini katta harf bilsn yozadi`

meva = "    olmani    "
print("Men " + meva + " yaxshi ko`raman")
print("Men " + meva.lstrip() + " yaxshi ko`raman")
print("Men " + meva.rstrip() + " yaxshi ko`raman")
print("Men " + meva.strip() + " yaxshi ko`raman")

# Input operator

ism = input("Ism = ")
print(f"Assalom alekum {ism.title()}")

# Amaliyot 
kocha = "Bog`bon"
mahalla = "Sog`bon"
tuman = "Bodomzor"
vil = "Samarqand"

print(f"{kocha.title()} ko`chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {vil.title()} viloyati")

kocha = input("Ko`cha nomi: ")
mahalla = input("Mahalla nomi: ")
tuman = input("Tuman nomi: ")
vil = input("Viloyat nomi: ")

print(f"{kocha.title()} ko`chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {vil.title()} viloyati")
print(f"{kocha.title()} ko`chasi\n {mahalla.title()} mahallasi\n {tuman.title()} tumani\n {vil.title()} viloyati")

matn = (f"{kocha} {mahalla} {tuman} {vil}")

print(matn)

print(f"{kocha.title()} {kocha.upper()} {kocha.lower()} {kocha.capitalize()}")
print(f"{mahalla.title()} {mahalla.upper()} {mahalla.lower()} {mahalla.capitalize()}")
print(f"{tuman.title()} {tuman.upper()} {tuman.lower()} {tuman.capitalize()}")
print(f"{vil.title()} {vil.upper()} {vil.lower()} {vil.capitalize()}")
print(matn.capitalize())