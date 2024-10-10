from random import randint
 
print("CHAO MUNG CAC BAN DA DEN VOI GAME ''KEO, BUA, BAO''")
print("Hay chon Keo hoac Bua hoac Bao: ")
player = input()
computer = randint(0,2)
 
if computer == 0:
    computer = "Bua"
if computer == 1:
    computer = "Bao"
if computer == 2:
    computer = "Keo"
     
print("+++---+++")
print("Ban chon: " + player)
 
if player == computer:
    print("May chon: " + computer)
    print("+++---+++")
    print("May said: Hoa roi. Lai lan nua nao!")
else:
    if player == "Keo":
        if computer == "Bua":
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thua roi. Ve luyen tap lai di.")
        else:
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thang roi. Hen thoi.")
     
    elif player == "Bua":
        if computer == "Bao":
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thua roi. Ve luyen tap lai di.")
        else:
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thang roi. Hen thoi.")
             
    elif player == "Bao":
        if computer == "Keo":
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thua roi. Ve luyen tap lai di.")
        else:
            print("May chon: " + computer)
            print("+++---+++")
            print("May said: Ban thang roi. Hen thoi.")
    else:
        computer = "Nhap sai roi! Nhap lai di :3!"
        print("May said: " + computer)
        print("+++---+++")