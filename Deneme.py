
#1.Gün

#print("Hello\nWorld") Alt satıra geçiyo
#print("Hello\tWorld") Boşluk bırakıyo
#print(mesaj.upper())  Hepsini büyük yazıyo
#print(mesaj.lower())  Hepsini küçük yazıyo
#print(mesaj.capitalize()) Baş harfini büyüyk yazıyo
#print(mesaj.startswith("T")) Hangi harfle başladığını kontrol ediyo
#print(mesaj.endswith("n"))    Hangi harfle bittiğini kontrol ediyo
#print("{} , {}  dedi...".format(isim,mesaj)) Kümeleri dolduruyo
 
#2.Gün

#sayi1 = 5
#sayi2 = 3.8
#print(type(sayi1))  İnteger
#print(type(sayi2))  Float

#print(3 ** 4)  Üslü sayı

#print(abs(-31)) Mutlak değer

#sayi = 22 / 7 
#print(round(sayi))  Yuvarlıyo

#print((3 + 2) * 4 + 3) İşlem önceliği

#print(3 == 3) Eşittir

#sayi1 = 7
#sayi2 = 10
#sayi3 = 10
#print(sayi1 < sayi2) Küçüktür
#print(sayi1 > sayi2) Büyükür
#print(sayi1 != sayi2) Eşit değilmi
#print(sayi2 <= sayi3) Küçük eşittir

#sayi1= "100"
#sayi2 = 100
#sayi3 = int(sayi1)
#print(type(sayi1)) String
#print(type(sayi2)) İnteger
#print(sayi1 == sayi2) False
#print(sayi3 == sayi2) True

#sayi1 = int(3.9) 
#print(sayi1) Yuvarlama yok 
#sayi1 = round(3.6)
#print(sayi1)  Yuvarlama var

#sayi = 123
#sayi2 = str(sayi)
#print(sayi2) 123
#print(sayi)  123
#print(type(sayi2)) String
#-------------------------------------------------------------------------------------------------------------------------------------
#3.Gün

#renkler = ["Siyah" , "Beyaz" , "Sarı" , "Mavi" , "Yeşil"]
#print(len(renkler))  Listede kaç tane eleman olduğunu gösteriyo.
#print(renkler[2:])  2 den başla sonuna kadar devam et
#print(renkler[1:4])  1 den 4 e kadar yazdır
#print(renkler[::2])  Listeyi parçalamak

#renkler = ["Siyah" , "Beyaz" , "Sarı" , "Mavi" , "Yeşil"]
#renkler.append("Gri") 
#print(renkler) Listenin sonuna "Gri" ekledi
#renkler.insert(0,"Gri") 
#print(renkler) Listenin başına "Gri" ekledi
#renkler.remove("Sarı") 
#print(renkler) Listeden "Sarı" elemanını sildi
#renkler2 = ["Turuncu" , "Pembe"]
#renkler.extend(renkler2)
#print(renkler) "Turuncu" ve "Pembe" elemanını ekledi 
#renkler.pop()
#print(renkler)  Son  elemanı sildi 
#silinen = renkler.pop()
#print(renkler)
#print(silinen) Silinen elemanı gösterdi
#---------------------------------------------------------------------------------------------------------------------------------------
#4. Gün

#demet = ("Sarı" , "Mavi" , "Yeşil" , "Kırmızı" , "Siyah")
#print(type(demet))  Tuple
#print(len(demet))   5
#for renk in demet:
    #print(renk)  Teker teker bütün elemanları yazdırır

#kume = {"Sarı" , "Mavi" , "Yeşil" , "Kırmızı" , "Siyah"}
#print(type(kume))  Set
#print(len(kume))  5
#for renk in kume:
    #print(renk)  Teker teker bütün elemenları yazdırır
#print(kume)
#kume.add("Pembe")
#print(kume)  Pembe elemanını ekledi
#kume.remove("Sarı")
#print(kume)  Sarı elamanını sildi
#kume.discard("Gri")
#print(kume)  Error vermedi 

#kume1 = {"Sarı" , "Mavi" , "Yeşil" , "Kırmızı" , "Siyah"}
#kume2 = {"Sarı" , "Mavi" , "Yeşil" , "Beyaz" , "Gri"}
#print(kume1.intersection(kume2))  kume1 ile kume2 nin ortak elemanlarını yazdırdı        Sarı,Mavi,Yeşil
#print(kume1.union(kume2))  2 küme arasındaki elemanları birleştirdi     Sarı,Mavi,Yeşil,Kırmızı,Siyah,Gri,Beyaz
#print(kume1.difference(kume2))  küme1 ile küme2 nin farkını gösyeriyo      Siyah ve Kırmızı
#print("sarı" in kume1) Herhangi bir elemanı bir kümede yada demette olup olmadığını kontrol ediyor   True
#print("Beyaz" in kume1) False
#print("Beyaz" in kume1.union(kume2))  Beyaz elemanı kümelerin birleşiminde varsa true değerini vercek yok ise false değerini vercek       True

#bosliste1 = []
#bosliste2 = list()   Boş bir liste

#bosdemet1 = ()
#bosdemet2 = tuple()  Boş bir demet

#boskume1 = set()     Boş bir küme
#boskume2 = {}        BU BİR SÖZLÜKTÜR

#python = set()










