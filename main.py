#def toliq_ism(ism, familya):
#  """Foydalanuvchidan ismi va familyasini so'rab uni ekranga chiqarish"""
#  print(f"Sizning ismingiz {ism}, familyangiz {familya}.") 
#toliq_ism("Abduhalil", "Abdug'aniyev")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
  """Toliq ism qaytaruvchi funksiya"""
  if otasining_ismi:
   toliq_ism = f"{ism} {otasining_ismi} {familiya}"
  else:
    toliq_ism = f"{ism} {familiya}"
  return toliq_ism.title()

talaba1 = toliq_ism_yasa('Ali', "Abdug'niyev")
talaba2 = toliq_ism_yasa('ali','valiev','gani ogli')
print(f"Darsga kelgan talabalar: {talaba1} va {talaba2}\n")


def avto_info(kompaniya, model,rangi, korobka,yili, narxi=None):
  avto = {'kompaniya':kompaniya,
         'model':model,
         'rang':rangi,
         'korobka':korobka,
         'yil':yili,
          'narx':narxi}
  return avto

avto1 =avto_info("GM",'Malibu','Qora','Avtomat',2018)
avto2= avto_info('GM','Malibu','Oq','Mexanika',2017,15000)
avtolar=[avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar: ')
for avto in avtolar:
  if avto['narx']:
    narx=avto['narx']
  else:
    narx="Noma'lum"
  print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")



def oraliq(min,max):
  sonlar = []
  while min<max:
    sonlar.append(min)
    min+=1
    return sonlar

#Funksiyalarni tsiklda ishlatish
print("\nSaytimizdagi avtolar royxatini shakilantiramiz.")
avtolar=[] #salondagi avtolar uchun bo'sh ro'yxat
while True:
  print("\nQuydagi malumotlarni kiriting ",end='' )
  kompaniya=input("Ishlab chiqaruvchi: ")
  model=input("Modeli: ")
  rangi=input("Rangi: ")
  korobka=input("Korobka: ")
  yili=input("Ishlab chiqarilgan yili: ")
  narxi=input("Narxi: ")

  avtolar.append(avto_info(kompaniya, model,rangi,korobka,yili,narxi))
  javob=input("Yana avto qo'shasizmi? (yes/no):")
  if javob=='no':
    break


