def printboard():
    zero='X' if P1[0] else('O' if P2[0] else 0)
    one='X' if P1[1] else('O' if P2[1] else 1)
    two='X' if P1[2] else('O' if P2[2] else 2)
    three='X' if P1[3] else('O' if P2[3] else 3)
    four='X' if P1[4] else('O' if P2[4] else 4)
    five='X' if P1[5] else('O' if P2[5] else 5)
    six='X' if P1[6] else('O' if P2[6] else 6)
    seven='X' if P1[7] else('O' if P2[7] else 7)
    eight='X' if P1[8] else('O' if P2[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")
def sum(a,b,c):
    return a+b+c
def checkwin(P1,P2):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(P1[win[0]],P1[win[1]],P1[win[2]])==3):
            print("Player 1 won the match")
            return 1
        if(sum(P2[win[0]],P2[win[1]],P2[win[2]])==3):
            print("Player 2 won the match")
            return 0
    return -1
P1=[0,0,0,0,0,0,0,0,0]
P2=[0,0,0,0,0,0,0,0,0]
turn = 1
print("Welcome To Tic Tac Toe")
while(True):
    printboard()
    if(turn == 1):
        print("P1's Chance")
        value= int(input("Please enter a value:"))
        P1[value]=1
    else:
        print("P2's Chance")
        value= int(input("Please enter a value:"))
        P2[value]=1
    cw=checkwin(P1,P2)
    if(cw!=-1):
        print("Match Over")
        break
    turn = 1 - turn



