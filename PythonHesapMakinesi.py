def Hesapla(x,y,islem): #Fonksiyonu olusturdum.
  if islem not in "+-*/": #isleme default degerlerden baska bir sey girilirse eger burayi calistir.
    return print("Lutfen duzgun bir islem belirtin: (+, -, *, /) ") #hatali islemde kullaniciyi uyardim.
# HESAPLAMA ISLEMININ YAPILDIGI BASAMAKLAR 5 - 12
  if islem == "+": 
    print(str(x) + " + " + str(y) + " = " + str(x+y))
  if islem == "-":
    print(str(x) + " - " + str(y) + " = " + str(x-y))
  if islem == "*":
    print(str(x) + " * " + str(y) + " = " + str(x*y))
  if islem == "/":
    print(str(x) + " / " + str(y) + " = " + str(x/y))

while True: #sonsuz fongu baslattim 
  try: # bunun alinda bulunan islemler dogruysa devam et - hataliysa EXCEPT (19.SATIR) satirina gec.
    x = int(input("Lutfen 1.sayiyi giriniz: ")) #1. sayiyi aldim.
    y = int(input("Lutfen 2.sayiyi giriniz: ")) #2. sayiyi aldim.
    islem = input("Lutfen islemi giriniz: (+, -, *, /)") #islemi aldim.
    Hesapla(x,y,islem) #Fonksiyona gonderdim.
  except:
    print("Lutfen duzgun bir sayi giriniz") # hatali sayi girildiginde ekrana uyari verdim.
    