#Autors:Juta Smirnova
#Datums: 19.10.2022
# Programma, kas sasveicinās ar lietotāju

print ("Hello")

#mainīgajā vards saglabā lietotāja ievadīto vārdu

# ar if ... else ... sazarojmu izvadit dzimuman attiecigo uzrunu : Sveiks (vīriešiem) , Sveika (sievietēm)

# izvada rezultātu konsolē (out p)
#Saglabā lietotāja ievadīto informāciju mainīgajā
print("Laipni lūgti! Es esmu programma ,kas velas ar tevi ieazīties ; \ n")

vards = input("Ievadi vardu")
print("Tu ieadiji", vards)
vards=input("Lūdzu ievadi savu vārdu un nospied ENTER")

if vards[0] == "Z":
  print("ggggg")
  print("Tu esi alfabēta augšgalā")
elif vards[0] == "Z":
  print("Tu esi alfabēta apakšā")
else: 
  print("Tu esi kaut kur pa vidu")
