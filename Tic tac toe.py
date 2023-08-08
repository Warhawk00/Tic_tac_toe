s1 = ("1  2  3\n4  5  6\n7  8  9\n")
player_1 = input("Name of player 1 - ")
player_2 = input("Name of player 2 - ")
l = ["0"]
while True:
    a = input("What would you chose {} X or O -".format(player_1))
    if a == "X":
        b = "O"
        break
    elif a == "O":
       b = "X"
       break
else:
    print("Write X or O ", player_1)
if a == "X" or a =="O":
    c = 0
    print(s1)
    while True:
        c = c+1
        p1 = input( "Enter the number on which you want to place {} {} - ".format(a , player_1))
        s1 = s1.replace( p1, a) 
        print(s1)
        w1 = a+a+a
        if s1[0:7:3] == w1 or s1[8:15:3] == w1 or s1[16:23:3] == w1 or s1[0::11] == w1: 
            print(player_1, "won")
            break
        elif s1[3:23:8] == w1 or s1[0:23:8] == w1 or s1[6:23:8] == w1 or s1[6:17:5] == w1:
            print(player_1 ,"won")
            break
        if c== 9:
            print("Its a tie")
            break
        c = c+1
        p2 = input("Enter the number on which you want to place {} {} -".format(b , player_2))
        s1 = s1.replace(p2,b) 
        print(s1)
        w2 = b+b+b
        if s1[0:7:3] == w2 or s1[8:15:3] == w2 or s1[16:23:3] == w2 or s1[0::11] == w2: 
            print(player_2, "won")
            break
        elif s1[3:23:8] == w2 or s1[0:23:8] == w2 or s1[6:23:8] == w2 or s1[6:17:5] == w2:
            print(player_2 ,"won")
            break
