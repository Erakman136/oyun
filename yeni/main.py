#pgzero
import random

WIDTH = 600
HEIGHT = 400

TITLE = "Hayvan Avcısı"
FPS = 30

# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
merhba = Actor("balamak_için_tıkladiyooo", (300, 100))
carpi = Actor("çarpı", (580, 20))
magaza = Actor("mağaza", (300, 200))
koleksiyon = Actor("koleksiyon", (300, 300))
timsah = Actor('timsahmısmıs', (70, 100))
suaygiri = Actor('suaygırımısmısamacokmus', (310, 100))
tkm = Actor('tkmpng', (100, 100))
tas = Actor('taszero', (200, 300))
makas = Actor('erkmanamakasss', (300, 300))
kagit = Actor("kagiterkman", (400, 300))
ticaret_button = Actor("ticaret_buttonerakman", (500, 100))
pc = Actor("computer terminal previewsat", (280, 30))
altin = Actor("sarı", (280, 20))
puan_alma = Actor("1 yıldız sat 1000 puan al", (450, 100))
pctwo = Actor("bilgisiyar", (100, 20))
altin_yildiz = Actor("sarısmfıomnşso", (100, 20))
para = Actor("TL_düzenliamadahaamaçok", (445, 30))
tavsan = Actor("tavşan", (520, 100))
rakun = Actor("rakun",(90, 210))
kuzu = Actor("kuzu", (310, 215))
at = Actor("at", (530, 210))
civciv = Actor("civciv", (70, 300))
dana = Actor("dana", (315, 310))
panda = Actor("panda", (530, 310))
karistir = Actor("bonusdiyoAMA ÇOK MUŞYAAAA", (475, 30))
ejderha = Actor("zyro-imagediiiii", (310, 215))
bitis = Actor("OYUN BİTTİ")

# Değişkenler
puan = 90000
tiklama = 1
mod = 'menü'
ucret_1 = 15
ucret_2 = 200
ucret_3 = 600
durum = None
oyuncu_puani = 0
bilgisayar_puani = 0
hayvanlar = []

def draw():
    global mod, hayvanlar
    if mod == 'menü':
        
        arkaplan.draw()
        merhba.draw()
        screen.draw.text(str(puan), center=(30, 20), color="white", fontsize=24)

        magaza.draw()
        koleksiyon.draw()
        tkm.draw()
        ticaret_button.draw()
   
    elif mod == 'oyun':    
        arkaplan.draw()
        hayvan.draw()
        screen.draw.text(puan, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(ucret_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(ucret_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("Her 2 saniye için 50$", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(ucret_3, center=(450, 310), color="black", fontsize = 20)
        carpi.draw()
    elif mod == 'mağaza':
        arkaplan.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 24)
        rakun.draw()
        kuzu.draw()
        at.draw()
        civciv.draw()
        dana.draw()
        panda.draw()
        
        

        

        timsah.draw()
        if timsah in hayvanlar:
            screen.draw.text('ALINDI', center = (70, 100), color = 'red', fontsize = 32)
        else:
            screen.draw.text('500$', center = (70, 100), color = 'red', fontsize = 32)
        
  
        suaygiri.draw()
        if suaygiri in hayvanlar:
            screen.draw.text('ALINDI!', center = (310, 100), color = 'red', fontsize = 32)
        else:
            screen.draw.text('2500$', center = (310, 100), color = 'red', fontsize = 32) 
            
        tavsan.draw()
        if tavsan in hayvanlar:
            screen.draw.text('ALINDI', center = (520, 100), color = 'red', fontsize = 32)
        else:
            screen.draw.text('4500$', center = (520, 100), color = 'red', fontsize = 32)
            
        rakun.draw()
        if rakun in hayvanlar:
            screen.draw.text('ALINDI', center = (90, 210), color = 'red', fontsize = 32)
        else:
            screen.draw.text('7500$', center = (90, 210), color = 'red', fontsize = 32)
        
        kuzu.draw()
        if kuzu in hayvanlar:
            screen.draw.text('ALINDI', center = (310, 215), color = 'red', fontsize = 32)
        else:
            screen.draw.text('9500$', center = (310, 215), color = 'red', fontsize = 32)
        
        at.draw()
        if at in hayvanlar:
            screen.draw.text('ALINDI', center = (530, 210), color = 'red', fontsize = 32)
        else:
            screen.draw.text('11500$', center = (530, 210), color = 'red', fontsize = 32)
            
        civciv.draw()
        if civciv in hayvanlar:
            screen.draw.text('ALINDI', center = (70, 300), color = 'red', fontsize = 32)
        else:
            screen.draw.text('13000$', center = (70, 300), color = 'red', fontsize = 32)
            
        dana.draw()
        if dana in hayvanlar:
            screen.draw.text('ALINDI', center = (315, 310), color = 'red', fontsize = 32)
        else:
            screen.draw.text('15000$', center = (315, 310), color = 'red', fontsize = 32)
            
        panda.draw()
        if panda in hayvanlar:
            screen.draw.text('ALINDI', center = (530, 310), color = 'red', fontsize = 32)
        else:
            screen.draw.text('17000$', center = (530, 310), color = 'red', fontsize = 32)
            
        carpi.draw()
        if len(hayvanlar) == 9:
            karistir.draw()
            
    elif mod == 'koleksiyon':
        arkaplan.draw()
        carpi.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 24)
        for i in range(len(hayvanlar)):
            hayvanlar[i].draw()
            screen.draw.text('+2$', center = (70,160), color = 'green', fontsize = 32)
            screen.draw.text('+3$', center = (310, 160), color = 'green', fontsize = 32)
            screen.draw.text('+6$', center = (520, 160), color = 'green', fontsize = 32)
            screen.draw.text('+10$', center = (80, 250), color = 'green', fontsize = 32)
            screen.draw.text('+15$', center = (310, 260), color = 'green', fontsize = 32)
            screen.draw.text('+25$', center = (530, 260), color = 'green', fontsize = 32)
            screen.draw.text('+40$', center = (70, 360), color = 'green', fontsize = 32)
            screen.draw.text('+55$', center = (315, 360), color = 'green', fontsize = 32)
            screen.draw.text('+70$', center = (530, 360), color = 'green', fontsize = 32)
    elif mod == 'taş-kağıt-makas':
        arkaplan.draw()
        carpi.draw()
        screen.draw.text(oyuncu_puani, center=(130, 20), color="white", fontsize = 24)
        screen.draw.text(bilgisayar_puani, center=(330, 20), color="white", fontsize = 24)
        altin_yildiz.draw()
        tas.draw()
        makas.draw()
        kagit.draw()
        pc.draw()
 
        if durum == 'beraber':
            screen.draw.text('berabere', center = (300,100), color = 'black', fontsize = 32)
        if durum == 'kazandınız':
            screen.draw.text('kazandiniz', center = (300,100), color = 'green', fontsize = 32)
        if durum == 'kaybettiniz':
            screen.draw.text('kaybettin', center = (300,100), color = 'red', fontsize = 32)
            
        
    elif mod == 'Ticaret':
        arkaplan.draw()
        carpi.draw()
        screen.draw.text(bilgisayar_puani, center=(30, 20), color="white", fontsize = 24)
        puan_alma.draw()
        screen.draw.text(oyuncu_puani, center = (330, 20), color = 'white', fontsize = 32) 
        altin.draw()
        pctwo.draw()
        screen.draw.text(puan, center = (500, 20), color = 'white', fontsize = 32)
        para.draw()
        
     
        
        
        
def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def bonus_3_icin():
    global puan
    count += 50

def on_mouse_down(button, pos):
    global puan, tiklama
    global mod, oyuncu_puani, bilgisayar_puani
    global ucret_1, ucret_2, ucret_3, durum, hayvanlar
    
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
        if carpi.collidepoint(pos):
            mod = 'Ticaret'
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
       # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 *= 2
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 2)
                puan -= ucret_2
                ucret_2 *= 2
        # bonus_3 button tıklandığında
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 2)
                puan -= ucret_3 
                ucret_3 *= 2
       
       
                
                
    if button == mouse.LEFT and mod == "taş-kağıt-makas":
        if carpi.collidepoint(pos):
            mod = 'menü'
        elif tas.collidepoint(pos):
            b_secim = random.randint(0, 2)
            if b_secim == 0:
                b_secim = 'taş'
                durum = 'beraber'
            elif b_secim == 1:
                b_secim = 'kağıt'
                durum = 'kaybettiniz'
                oyuncu_puani -= 1  # Oyuncu kaybettiği için puanını azalt
                bilgisayar_puani += 1
            else:
                b_secim = 'makas'
                durum = 'kazandınız'
                oyuncu_puani += 1
                bilgisayar_puani -= 1
        elif kagit.collidepoint(pos):
            b_secim = random.randint(0, 2)
            if b_secim == 0:
                b_secim = 'taş'
                durum = 'kazandınız'
                oyuncu_puani += 1
                bilgisayar_puani -= 1 
            elif b_secim == 1:
                b_secim = 'kağıt'
                durum = 'beraber'
            else:
                b_secim = 'makas'
                durum = 'kaybettiniz'
                oyuncu_puani -= 1  # Oyuncu kaybettiği için puanını azalt
                bilgisayar_puani += 1
                
        elif makas.collidepoint(pos):
            b_secim = random.randint(0, 2)
            if b_secim == 0:
                b_secim = 'taş'
                durum = 'kaybettiniz'
                oyuncu_puani -= 1  # Oyuncu kaybettiği için puanını azalt
                bilgisayar_puani += 1
            elif b_secim == 1:
                b_secim = 'kağıt'
                durum = 'kazandınız'
                bilgisayar_puani -= 1
                oyuncu_puani += 1
            else:
                b_secim = 'makas'
                durum = 'beraber'
           

                
            

    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if merhba.collidepoint(pos):
            mod = 'oyun'
        elif magaza.collidepoint(pos):
            mod = 'mağaza'
        elif koleksiyon.collidepoint(pos):
            mod = 'koleksiyon'
            #taş kağıt makas
        elif tkm.collidepoint(pos):
            mod = 'taş-kağıt-makas'
        elif ticaret_button.collidepoint(pos):
            mod = 'Ticaret'
    #MAĞAZA MODU
    elif mod == 'mağaza' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        elif timsah.collidepoint(pos) and puan >= 500 and timsah not in hayvanlar:
            puan -= 500
            hayvan.image = 'timsahmısmıs'
            tiklama = 2
            hayvanlar.append(timsah)
        elif suaygiri.collidepoint(pos) and puan >= 2500 and suaygiri not in hayvanlar:
            puan -= 2500
            hayvan.image = 'suaygırı'
            tiklama = 30
            hayvanlar.append(suaygiri)
        elif tavsan.collidepoint(pos) and puan >= 4500 and tavsan not in hayvanlar:
            puan -= 4500
            hayvan.image = 'tavşan'
            tiklama = 6
            hayvanlar.append(tavsan)
        elif rakun.collidepoint(pos) and puan >= 4500 and rakun not in hayvanlar:
            puan -= 7500
            hayvan.image = 'rakun'
            tiklama = 10
            hayvanlar.append(rakun)
        elif kuzu.collidepoint(pos) and puan >= 4500 and kuzu not in hayvanlar:
            puan -= 9500
            hayvan.image = 'kuzu'
            tiklama = 15
            hayvanlar.append(kuzu)
        elif at.collidepoint(pos) and puan >= 4500 and at not in hayvanlar:
            puan -= 11500
            hayvan.image = 'at'
            tiklama = 25
            hayvanlar.append(at)
        elif civciv.collidepoint(pos) and puan >= 4500 and civciv not in hayvanlar:
            puan -= 13000
            hayvan.image = 'civciv'
            tiklama = 40
            hayvanlar.append(civciv)
        elif dana.collidepoint(pos) and puan >= 4500 and dana not in hayvanlar:
            puan -= 15000
            hayvan.image = 'dana'
            tiklama = 55
            hayvanlar.append(dana)
        elif panda.collidepoint(pos) and puan >= 4500 and panda not in hayvanlar:
            puan -= 17000
            hayvan.image = 'panda'
            tiklama = 70
            hayvanlar.append(panda)
        elif karistir.collidepoint(pos):
            hayvanlar = []
            bitis.draw()
          
            
            
                
            
    #KOLEKSİYON MODU
    elif mod == 'koleksiyon' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
            
    #TİCARET MODU
    elif mod == 'Ticaret' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        if puan_alma.collidepoint(pos) and oyuncu_puani >= 1:
            oyuncu_puani -= 1
            puan += 1000
            bilgisayar_puani -= bilgisayar_puani