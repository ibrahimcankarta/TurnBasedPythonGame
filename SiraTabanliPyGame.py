import time
import random

#giriş bölümü
print("------soldiers of python'a hoş geldiniz------")
time.sleep(1)
print("Oyunu size tanıtmak için buradayım")
time.sleep(2)
print(" soldiers of python sıra tabanlı bir python oyunudur.")
time.sleep(2)
oyun=input("oyun hakkında detaylı bilgi için '1' e, oyuna hemen başlamak için başka bir şeye basın")

if oyun == "1" :
    print("Oyunda can, saldırı gücü ve zeka olmak üzere bazı özellikler bulunmaktadır.")
    time.sleep(1)
    print("karakterin nitelik alanlarındaki dağılımları birbirinden farklıdır.")
    time.sleep(2)
    print("Oyun mantığında karakterinizin gücüne ve zekasına göre, gireceği karşılaşmalardan galip çıkma şansı kategoriye göre artabilir veya azabilir.")
else :
    print("Oyuna devam ediliyor")
print("ilk olarak karakteriniz:")
def karakter(*p):
    for s in p:
        print (s)
karakter("Oscar")


class oscarMutant:
    can = 100
    saldiri = 100
    zeka = 0

def oscar2(sayac):
    print("oscar bulmacayı çözdü ve kitabı açmayı başardı.")
    print("kitabın ilk cümlesi şu şekilde: 'Ipsa scientia potestas est.'")

#öldüğünde çalışacak olan fonksiyon.
def bitti():
    print("Ne yazık ki oyunu tamamlayamadınız")
    print("bir dahaki sefer dikkatli olmanızı öneririz")

#Oscar ilk görevi tamamlarsa çalışacak olan fonksiyon.
def oscar1(sayac):
    x=oscarMutant()
    can=x.can
    can=can-sayac


    print("Oscar zinciri dışarıya yolladı ve tırmandı.")
    print("kuyudan çıkmayı başardın")
    print("canın", can)
    print("Oscar yangından sonra 30'lu yaşlarının başına gelene dek yazarlık yaptı.")
    print("Ancak zaman geçtikçe kitaplarının satmamasından usandı ve büyük bir nefretle doldu.")
    time.sleep(2)
    print("dünyadan hırsını alabilmek için karşı konulamaz bir büyücü haline geldi.")
    input("devam etmek için bir tuşa bas")
    i = 1
    while i < 4:
        print(i)
        time.sleep(1)
        i = i + 1

    print("Oscar yıllardır aramakta olduğu bir kitabı bulmuştur.")
    print("Bu kitapta en kadim büyülerin ve lanetlerin sırları yer almaktadır.")
    time.sleep(2)
    print("Ancak kitapçı, dostu Oscar için bir bulmaca hazırlamış ve kitabın üzerine bir soru yazmıştır.")
    print("Python'da fonksiyon kullanırken, parantezin içerisine yazılanların genel adı nedir?")
    print("Cevabı yazmadan önce sana ipucu vermesi için bir büyü yapabilirsin.")
    time.sleep(1)
    buyu = input("büyü %70 ihtimalle işe yarayacaktır. işe yaramazsa kitap biraz hasar alacak. Büyü yapmak ister misin?(E/H)")
    if buyu == "e" or "E":
        q = random.randint(1, 100)


        if q < 70:
            ipucu = ["integer", "sözlük", "parametre"]
            print("büyüyü başarıyla yaptın! İpucu şu şekilde:", ipucu)
            cevap = input("cevabı biliyor musun?")
            if cevap == "parametre" or "Parametre":
                print("bulmacayı çözdün!")
                oscar2(sayac=10)
            else:
                print("Yine olmadı! Kitabı mahvedeceksin! Tekrar dene...")
                cevap1 = input("cevabın nedir?")
                if cevap1 == "parametre" or "Parametre":
                    print("Sonunda doğru cevap!")
                    oscar2(sayac=40)
                else:
                    print("yanlış!")
                    sayac = sayac + 30
                    cevap2 = input("Boşa harcıyorsun, cevap ne Oscar?")
                    if cevap2 == "parametre" or "Parametre":
                        print("kolay olmadı ama cevabı buldun...")
                        oscar2(sayac=70)
                    else:
                        sayac = sayac + 30
                        cevap3 = input("Bu son şansın, cevap nedir?")
                        if cevap3 == "parametre" or "Parametre":
                            print("bu çok uzun sürdü dostum.")
                            oscar2(sayac=100)
                        else:
                            bitti()
        else:
            print("Beceremedin! kitap biraz hasar aldı, ancak hala cevabı yazabilirsin.")
            sayac = sayac + 10
            cevap = input("cevabı biliyor musun?")
            if cevap == "parametre" or "parametre":
                print("bulmacayı çözdün!")
                oscar2(sayac=10)
            else:
                print("Yine olmadı! Kitabı mahvedeceksin! Tekrar dene...")
                cevap1 = input("cevabın nedir?")
                if cevap1 == "parametre" or "Parametre":
                    print("Sonunda doğru cevap!")
                    oscar2(sayac=40)
                else:
                    print("yanlış!")
                    sayac = sayac + 30
                    cevap2 = input("Boşa harcıyorsun, cevap ne Oscar?")
                    if cevap2 == "parametre" or "Parametre":
                        print("kolay olmadı ama cevabı buldun...")
                        oscar2(sayac=70)
                    else:
                        sayac = sayac + 30
                        cevap3 = input("Bu son şansın, cevap nedir?")
                        if cevap3 == "parametre" or "Parametre":
                            print("bu çok uzun sürdü dostum.")
                            oscar2(sayac=100)
                        else:
                            bitti()
    if buyu == "h" or "H":
        cevap = input("cevabı biliyor musun?")
        if cevap == "parametre" or "Parametre":
            print("bulmacayı çözdün!")
            oscar2(sayac=0)
        else:
            print("olmadı! Kitabı mahvedeceksin! Tekrar dene...")
            cevap1 = input("cevabın nedir?")
            if cevap1 == "parametre" or "Parametre":
                print("Sonunda doğru cevap!")
                oscar2(sayac=30)
            else:
                print("yanlış!")
                sayac = sayac + 40
                cevap2 = input("Boşa harcıyorsun, cevap ne Oscar?")
                if cevap2 == "parametre" or "Parametre":
                    print("kolay olmadı ama cevabı buldun...")
                    oscar2(sayac=70)
                else:
                    sayac = sayac + 30
                    cevap3 = input("Bu son şansın, cevap nedir?")
                    if cevap3 == "parametre" or "Parametre":
                        print("bu çok uzun sürdü dostum.")
                        oscar2(sayac=100)
                    else:
                        bitti()


#Oscar'ın ilk görevinin fonksiyonu.
def oscar():
    print("Oscar ailesine sadık, mutlu bir kediydi")
    print("Ancak yıllar önce bir yangında sahibini kaybetti")
    print("Yangından sonra oradan nasıl çıktığını hiç kimse çözemedi")
    time.sleep(1)
    print("Tüm ev kül olmasına rağmen oradan sağ kurtulmayı başardı.")
    print("Oscar'ın arayışında onunla birlikte olacaksın... ")
    a=input("Oyuna başlamak için bir tuşa basın")
    i=1
    while i<4:
        print(i)
        time.sleep(1)
        i=i+1
    print("Başlıyoruz")
    kuyu=input("Oscar karanlığın içinde bir kuyuda uyandı. Kuyunun duvarları kaygan görünüyor, tırmanmayı denemek ister misin? (E/H) şans=%10")
    if kuyu == "e" or "E":
        q=random.randint(1,100)
        sayac=0
        if q>89:
            print("Tırmanmayı başardın")
            oscar1(sayac=0)
        else :
            sayac=sayac+10
            print("Tırmanmayı başaramadın")
            print("biraz canın yandı")
            print("yerde demirlere bağlı bir zincir gördün")
            time.sleep(1)
            print("zincir 6 harften oluşan bir şifre ile demirlere kilitlenmiş")
            time.sleep(1)
            print("kilidin üzerinde bir soru var: '''python'da modül yüklemek için kullanılan sözcük nedir?'''")
            cevap = input("cevabı biliyor musun?")
            if cevap == "import":
                print("kilidi çözdün!")
                oscar1(sayac=10)
            else:
                print("yanlış cevabın yüzünden kilit sana elektrik verdi! biraz canın azaldı. Tekrar dene...")
                cevap1 = input("cevabın nedir?")
                if cevap1 == "import":
                    print("Sonunda doğru cevap!")
                    oscar1(sayac=40)
                else:
                    print("yanlış!")
                    sayac=sayac+30
                    cevap2=input("canın azalıyor, tekrar dene...")
                    if cevap2=="import":
                        print("kolay olmadı ama cevabı buldun...")
                        oscar1(sayac=70)
                    else:
                        sayac=sayac+30
                        cevap3=input("Bu son şansın oscar, cevap nedir?")
                        if cevap3 == "import":
                            print("doğru cevap, ancak ne kadar idare edebilirsin bilmiyorum.")
                            oscar1(sayac=100)
                        else:
                            bitti()
    elif kuyu== "h" or "H":
        sayac=0
        print("yerde demirlere bağlı bir zincir gördün")
        time.sleep(1)
        print("zincir 6 harften oluşan bir şifre ile demirlere kilitlenmiş")
        time.sleep(1)
        print("kilidin üzerinde bir soru var: '''python'da modül yüklemek için kullanılan sözcük nedir?'''")
        cevap = input("cevabı biliyor musun?")
        if cevap == "import":
            print("kilidi çözdün!")
            oscar1(sayac=0)
        else:
            print("yanlış cevabın yüzünden kilit sana elektrik verdi! biraz canın azaldı. Tekrar dene...")
            cevap1 = input("cevabın nedir?")
            if cevap1 == "import":
                print("Sonunda doğru cevap!")
                oscar1(sayac=30)
            else:
                print("yanlış!")
                sayac = sayac + 40
                cevap2 = input("canın azalıyor, tekrar dene...")
                if cevap2 == "import":
                    print("kolay olmadı ama cevabı buldun...")
                    oscar1(sayac=70)
                else:
                    sayac = sayac + 30
                    cevap3 = input("Bu son şansın oscar, cevap nedir?")
                    if cevap3 == "import":
                        print("doğru cevap, ancak ne kadar idare edebilirsin bilmiyorum.")
                        oscar1(sayac=100)
                    else:
                        bitti()
    else:
        print("yanlış tuşlama yaptınız")

baslat=input("başlamak için adınızı yazınız")
print("oyunumuza hoşgeldin" + baslat)
oscar()






