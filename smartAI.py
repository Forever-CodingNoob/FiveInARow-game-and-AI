import time
import sys
import random
def printBoard(board):
    for row in board:
        print("\t".join(row))
        print()
def setSpeed():
    print("plz enter speed of AI.(1~100)")
    while True:
        a=input()
        try:
            a=int(a)
        except ValueError:
            print("not num!")
            continue
        if a>100:
            print("too BIG!!!")
            continue
        elif a<1:
            print("too SMALL!!!")
            continue
        return a
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
def AllCheck(who,board):
    #check if full:
    if checkBoardFull(board):
        gameover("tie")
        #no longer continue
    positions=dict()
    for y in range(size):
        for x in range(size):
            if board[y][x]==".":
                check(x,y,positions,who,board)
    print(positions)
    return positions
def check(x,y,positions,who,board):
    newBoard=[[i for i in row] for row in board]
    if who=="playerAI":
        newBoard[y][x]="O"
    elif who=="AI":
        newBoard[y][x]="X"
    pos=0
    pos=vertical(newBoard,pos,who)
    pos=horizontal(newBoard,pos,who)
    pos=slideUP(newBoard,pos,who)
    pos=slideDOWN(newBoard,pos,who)
    #>>>>>>>print(pos,end="\t")!!!!!!!!!!!!!!!!
    #for y in range(size):
        #for x in range(size):
    #bestPoint=max(pos.keys())
    #bestPos=pos[bestPoint]
    #positions[max(pos.keys())]=(y,x)
    positions[pos]=(y,x)


def vertical(b,pos,who):
    for x in range(size):
        line = [b[y][x] for y in range(size)]
        piecePos=[(y,x) for y in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos,who)
    return pos
def horizontal(b,pos,who):
    for y in range(size):
        line = [b[y][x] for x in range(size)]
        piecePos=[(y,x) for x in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos,who)
    return pos
def slideUP(b,pos,who):
    for k in range(0+4,(size*2-1)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x+y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x+y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos,who)
    return pos
def slideDOWN(b,pos,who):
    for k in range((-(size-1))+4,(size)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x-y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x-y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos=analyze(line,b,piecePos,pos,who)
    return pos
def analyze(line,b,piecePos,pos,who):
        #playerAI = O   AI = X
        if who=="AI":
            s,e="X","O"
            enemy="playerAI"
            score=[i for i in AiScore]
        elif who=="playerAI":
            s,e="O","X"
            enemy="AI"
            score=[i for i in PlayerAiScore]





            
        if e*5 in line:
            gameover(enemy)
        if e*4 in line:#need improving
            start=line.find(e*4)-1
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
                pos+=score[0]
            elif endPiece==".":
                pos+=score[0]

            
        if e*3 in line:
            start=line.find(e*3)-1
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
                pos+=score[1]
            elif startPiece==".":
                pos+=score[2]
            elif endPiece==".":
                pos+=score[2]

            
        if e*2 in line:
            start=line.find(e*2)-1
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
                pos+=score[3]
            elif startPiece==".":
                pos+=score[4]
            elif endPiece==".":
                pos+=score[4]
        if e*1 in line:
            start=line.find(e*1)-1
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
                pos+=score[5]
                #print(pos[2])
            elif startPiece==".":
                pos+=score[6]
            elif endPiece==".":
                pos+=score[6]




                
        if s*6 in line:
            gameover(who)
        if s*5 in line:#need improving
            start=line.find(s*5)-1
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
                gameover(who)


                
                
            pos+=score[7]


        

            
        if s*4 in line:
            start=line.find(s*4)-1
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
                pos+=score[8]
            elif startPiece==".":
                pos+=score[9]
            elif endPiece==".":
                pos+=score[9]

            
        if s*3 in line:
            start=line.find(s*3)-1
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
                pos+=score[10]
            elif startPiece==".":
                pos+=score[11]
            elif endPiece==".":
                pos+=score[11]
        if s*2 in line:
            start=line.find(s*2)-1
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
                pos+=score[12]
                #print(pos[2])
            elif startPiece==".":
                pos+=score[13]
            elif endPiece==".":
                pos+=score[13]
        if s*1 in line:
            start=line.find(s*1)-1
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
                pos+=score[14]
            elif endPiece==".":
                pos+=score[14]

        #below can use or to detect and then use mid=find(".") to get the right pos 
        if e+"."+e in line:
            start=line.find(e+"."+e)-1
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
                pos+=score[15]
                #print(pos[2])
            elif startPiece==".":
                pos+=score[16]
            elif endPiece==".":
                pos+=score[16]




                
        if e+e+"."+e in line:
            start=line.find(e+e+"."+e)-1
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
                pos+=score[17]
            elif endPiece==".":
                pos+=score[17]
        if e+"."+e+e in line:
            start=line.find(e+"."+e+e)-1
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
                pos+=score[18]
            elif endPiece==".":
                pos+=score[18]
        if e+e+"."+e+e in line:
            start=line.find(e+e+"."+e+e)-1
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
                
            pos+=score[19]
        if e+e+e+"."+e in line:
            start=line.find(e+e+e+"."+e )-1
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
                
            pos+=score[20]
        if e+"."+e+e+e in line:
            start=line.find(e+"."+e+e+e)-1
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
                
            pos+=score[21]

        #up#########################################################################
        return pos



        
def ai(positions,who,board):
    if positions!={}:
        besty,bestx=positions[max(positions.keys())]
        #print(positions)

        #whose turn
        if who=="AI":
            board[besty][bestx]="X"
        elif who=="playerAI":
            board[besty][bestx]="O"
    else:
        print("the AI of this game is too stupid to decide where to place its pawn.")
        print("So it's time for u to defeat it.")
    pass 
def gameover(text):
    global PlayerAiScore
    global AiScore
    if text=="playerAI":
        print("playerAI wins!!!")
        
        AiScore=[random.randint(-100000000,100000000) for i in range(22)]
    elif text=="AI":
        print("AI wins!!!")
        
        PlayerAiScore=[i for i in AiScore]
    elif text=="tie":
        print("the board is full!!!")
        print("LOOK WHAT AIs'VE DONE!!!")
        AiScore=[random.randint(-100000000,100000000) for i in range(22)]
    print(AiScore)
    #time.sleep(0.5)
    print("end!")
    Start(board)



def Start(board):
    
    board=[["." for i in range(size)] for i in range(size)]
    printBoard(board)
    while 1:
        #playerAI
        positions=AllCheck("playerAI",board)
        time.sleep(1/speed)
        ai(positions,"playerAI",board)
        #test board full check code:
        #board=[["滿" for i in range(size)] for i in range(size)]
        printBoard(board)

        

        #AI
        positions=AllCheck("AI",board)
        time.sleep(1/speed)
        #time.sleep(3)
        #clear()
        ai(positions,"AI",board)
        printBoard(board)
        #positions=AllCheck()


#global positions
positions=dict()
#size=9
board=list()
size=setSize()
speed=setSpeed()

AiScore=list()
PlayerAiScore=list()
AiScore=[-10000000,-1000000,-10000,-100,-50,-3,-1,100000000,2000,500,1000,10,5,2,1,-500000,-5000,-10000,-10000,-10000000,-10000000,-10000000]
PlayerAiScore=[-10000000,-1000000,-10000,-100,-50,-3,-1,100000000,2000,500,1000,10,5,2,1,-500000,-5000,-10000,-10000,-10000000,-10000000,-10000000]
Start(board)
    






