import time
import sys
def printBoard(board):
    for row in board:
        print("\t".join(row))
        print()
def setSize():
    print("plz enter the size of board.(n in size(nxn))(allowed size=5 to 20)")
    while True:
        a=input()
        try:
            a=int(a)
        except ValueError:
            print("not num!")
            continue
        if a>20:
            print("too BIG!!!")
            continue
        elif a<5:
            print("too SMALL!!!")
            continue
        return a
def clear():
    for i in range(100):
        print()
def player():
    print("plz enter ur pos.")
    while True:
        a=input()
        if a.find(" ")==-1 or len(a) > 20:
            print("wrong!!")
            continue
        try:
            x,y = [int(i)-1 for i in a.split()]
            #print(x,y)
        except ValueError:
            print("not num!")
            continue
        #x,y=====0~size-1
        if x<0 or y<0 or x>size-1 or y>size-1:
            print("UR WEIRD NUM NOT ALLOWED!!!")
            continue
        #print(122)
        if not checkNoPiece(y,x):
            print("There is already a piece.")
            continue
        break
    board[y][x]="O"
def checkNoPiece(y,x):
    return board[y][x]=="."
def checkBoardFull(board):
    isFull = True
    for row in board:
        for piece in row:
            if piece==".":
                isFull=False
    return isFull
def AllCheck():
    #check if full:
    if checkBoardFull(board):
        gameover("tie")
        #no longer continue
    positions=dict()
    for y in range(size):
        for x in range(size):
            if board[y][x]==".":
                check(x,y,positions)
    print(positions)
    return positions
def check(x,y,positions):
    newBoard=[[i for i in row] for row in board]
    newBoard[y][x]="X"
    pos=0
    pos=vertical(newBoard,pos)
    pos=horizontal(newBoard,pos)
    pos=slideUP(newBoard,pos)
    pos=slideDOWN(newBoard,pos)
    #>>>>>>>print(pos,end="\t")!!!!!!!!!!!!!!!!
    #for y in range(size):
        #for x in range(size):
    #bestPoint=max(pos.keys())
    #bestPos=pos[bestPoint]
    #positions[max(pos.keys())]=(y,x)
    positions[pos]=(y,x)


def vertical(b,pos):
    for x in range(size):
        line = [b[y][x] for y in range(size)]
        piecePos=[(y,x) for y in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos)
    return pos
def horizontal(b,pos):
    for y in range(size):
        line = [b[y][x] for x in range(size)]
        piecePos=[(y,x) for x in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos)
    return pos
def slideUP(b,pos):
    for k in range(0+4,(size*2-1)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x+y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x+y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos)
    return pos
def slideDOWN(b,pos):
    for k in range((-(size-1))+4,(size)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x-y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x-y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos)
    return pos
def analyze(line,b,piecePos,pos):
        if "O"*5 in line:
            gameover("win")
        if "O"*4 in line:#need improving
            start=line.find("O"*4)-1
            end=start+5
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece==".":
                pos-=10000000
            elif endPiece==".":
                pos-=10000000

            
        if "O"*3 in line:
            start=line.find("O"*3)-1
            end=start+4
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos-=1000000
            elif startPiece==".":
                pos-=10000
            elif endPiece==".":
                pos-=10000

            
        if "O"*2 in line:
            start=line.find("O"*2)-1
            end=start+3
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos-=100
            elif startPiece==".":
                pos-=50
            elif endPiece==".":
                pos-=50
        if "O"*1 in line:
            start=line.find("O"*1)-1
            end=start+2
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos-=3
                #print(pos[2])
            elif startPiece==".":
                pos-=1
            elif endPiece==".":
                pos-=1




                
        if "X"*6 in line:
            gameover("lose")
        if "X"*5 in line:#need improving
            start=line.find("X"*5)-1
            end=start+6
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"




            #check if gameover(X在頭和尾，剛好五顆)
            if startPiece=="N" and endPiece=="N":
                gameover("lose")




            
                
            pos+=100000000


        

            
        if "X"*4 in line:
            start=line.find("X"*4)-1
            end=start+5
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"



            


                
            if startPiece=="." and endPiece==".":
                pos+=2000
            elif startPiece==".":
                pos+=500
            elif endPiece==".":
                pos+=500

            
        if "X"*3 in line:
            start=line.find("X"*3)-1
            end=start+4
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos+=1000
            elif startPiece==".":
                pos+=10
            elif endPiece==".":
                pos+=10
        if "X"*2 in line:
            start=line.find("X"*2)-1
            end=start+3
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos+=5
                #print(pos[2])
            elif startPiece==".":
                pos+=2
            elif endPiece==".":
                pos+=2
        if "X"*1 in line:
            start=line.find("X"*1)-1
            end=start+2
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"

                
            if startPiece=="." and endPiece==".":
                pos+=2
                #print(pos[2])
            elif startPiece==".":
                pos+=1
            elif endPiece==".":
                pos+=1

        #below can use or to detect and then use mid=find(".") to get the right pos 
        if "O.O" in line:
            start=line.find("O.O")-1
            end=start+4
            mid=start+2
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            if startPiece=="." and endPiece==".":
                pos-=500000
                #print(pos[2])
            elif startPiece==".":
                pos-=5000
            elif endPiece==".":
                pos-=5000




                
        if "OO.O" in line:
            start=line.find("OO.O")-1
            end=start+5
            mid=start+3
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            if startPiece=="." and endPiece==".":
                pos-=1000000
                #print(pos[2])
            elif startPiece==".":
                pos-=10000
            elif endPiece==".":
                pos-=10000
        if "O.OO" in line:
            start=line.find("O.OO")-1
            end=start+5
            mid=start+2
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            if startPiece=="." and endPiece==".":
                pos-=1000000
                #print(pos[2])
            elif startPiece==".":
                pos-=10000
            elif endPiece==".":
                pos-=10000
        if "OO.OO" in line:
            start=line.find("OO.OO")-1
            end=start+6
            mid=start+3
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            pos-=10000000
        if "OOO.O" in line:
            start=line.find("OOO.O")-1
            end=start+6
            mid=start+4
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            pos-=10000000
        if "O.OOO" in line:
            start=line.find("O.OOO")-1
            end=start+6
            mid=start+2
            
            
            if start>=0:
                startPos=piecePos[start]
                startPiece=b[startPos[0]][startPos[1]]
            else:
                startPiece="N"
            if end<=len(line)-1:
                endPos=piecePos[end]
                endPiece=b[endPos[0]][endPos[1]]
            else:
                endPiece="N"
            midPos=piecePos[mid]
                
            pos-=10000000

        #up#########################################################################
        return pos



        
def ai(positions):
    if positions!={}:
        besty,bestx=positions[max(positions.keys())]
        #print(positions)
        board[besty][bestx]="X"
    else:
        print("the AI of this game is too stupid to decide where to place its pawn.")
        print("So it's time for u to defeat it.")
    pass 
def gameover(text):
    if text=="win":
        print("you win!!!")
    elif text=="lose":
        print("hahaha u lose!!!")
    elif text=="tie":
        print("the board is full!!!")
        print("LOOK WHAT U'VE DONE!!!")
    time.sleep(5)
    print("end!")
    sys.exit()
#global positions
positions=dict()
#size=9
size=setSize()
board=[["." for i in range(size)] for i in range(size)]
printBoard(board)
while 1:
    player()
    #test board full check code:
    #board=[["滿" for i in range(size)] for i in range(size)]
    printBoard(board)
    positions=AllCheck()
    #time.sleep(3)
    clear()
    ai(positions)
    printBoard(board)
    positions=AllCheck()






