import random

# Kompüterin seçdiyi gizli ədəd
gizli = random.randint(1, 100)
say=0
print("GUESS THE NUMBER yəni Rəqəm tapmaq oyununa xoş gəlmisiniz (tapılacaq olan ədəd 1-100 arasında gizlənib)")
while say<100: 
   oyuncu=int(input("Bir ədəd daxil edin-->"))
   say+=1
   if gizli==oyuncu: 
    print("Siz düz tapdınız") 
    break 
   elif gizli<oyuncu:
    print("teklif edilen ədəd gizli rəqəmdən böyükdür")
   elif gizli>oyuncu:
    print("teklif edilen ədəd gizli rəqəmdən kiçikdir ")
    










 

        
    




