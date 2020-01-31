import time
import sys
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
def DeepCheck(checkDepth,onlyCheck):


    
    #check if full:
    if checkBoardFull(board):
        gameover("tie")
        #no longer continue
    
    positionsss=dict()
    depth=0
    newBoard=[[i for i in row] for row in board]
    positionsss=AllCheck("AI",depth,newBoard,checkDepth,onlyCheck,0,False)
    return positionsss
def AllCheck(who,depth,newBoard,checkDepth,onlyCheck,alpha,checkAplhaBeta):
    #print(depth,who)
    #printBoard(newBoard)
    cut=False
    beta="no"
    positions=dict()
    for y in range(size):
        for x in range(size):
            if newBoard[y][x]==".":
                score=check(x,y,positions,who,depth,checkDepth,newBoard,onlyCheck,beta,beta!="no")
                positions[score]=(y,x)
                #if depth<=3:
                    #print("*"+str(depth)+"*")
                if who=="AI":
                    beta=max(positions.keys())
                elif who=="playerAI":
                    beta=min(positions.keys())
                if checkAplhaBeta:
                    
                    if who=="AI" and beta>alpha and checkAplhaBeta:
                        cut=True
                        #print("cut",depth)
                        break
                    elif who=="playerAI" and beta<alpha and checkAplhaBeta:
                        cut=True
                        #print("cut",depth)
                        break
                    else:
                        pass
                        #print("no cut")
        if cut:
            break
      
    if depth==0:
        print(positions)
        return positions
    else:
        #print(positions)
        if positions!=dict():
            if who=="playerAI":
                #print(min(positions.keys()))
                return min(positions.keys())
            if who=="AI":
                #print(max(positions.keys()))
                return max(positions.keys())
        print("what!?",depth)
        return 0
def check(x,y,positions,who,depth,checkDepth,newBoard,onlyCheck,beta,checkAplhaBeta):
    end=False
    #試著下一顆棋
    aWholeNewBoard=[[i for i in row]for row in newBoard]
    if not onlyCheck:#要再改，怪怪的
        if who=="playerAI":
            aWholeNewBoard[y][x]="O"
        elif who=="AI":
            aWholeNewBoard[y][x]="X"
    #if not onlyCheck:
        #printBoard(aWholeNewBoard)
    pos=0
    pos,end1=vertical(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end2=horizontal(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end3=slideUP(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end4=slideDOWN(aWholeNewBoard,pos,who,depth,onlyCheck)
    if end1 or end2 or end3 or end4:
        end=True

    if who=="playerAI":
        #newBoard[y][x]="."#還原棋盤
        if end or checkBoardFull(aWholeNewBoard) or depth+1>=checkDepth:
            #print("small checking ends",pos)
            return pos
        else:
            return AllCheck("AI",depth+1,aWholeNewBoard,checkDepth,onlyCheck,beta,checkAplhaBeta)
    elif who=="AI":
        if end or checkBoardFull(aWholeNewBoard) or depth+1>=checkDepth:
            #print("small checking ends",pos)
            return pos
        else:
            return AllCheck("playerAI",depth+1,aWholeNewBoard,checkDepth,onlyCheck,beta,checkAplhaBeta)


def vertical(b,pos,who,depth,onlyCheck):
    for x in range(size):
        line = [b[y][x] for y in range(size)]
        piecePos=[(y,x) for y in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
def horizontal(b,pos,who,depth,onlyCheck):
    for y in range(size):
        line = [b[y][x] for x in range(size)]
        piecePos=[(y,x) for x in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
def slideUP(b,pos,who,depth,onlyCheck):
    for k in range(0+4,(size*2-1)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x+y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x+y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
def slideDOWN(b,pos,who,depth,onlyCheck):
    for k in range((-(size-1))+4,(size)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x-y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x-y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
        #print(line)
        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
def analyze(line,b,piecePos,pos,who,depth,onlyCheck):
        #playerAI = O   AI = X
        

        s,e="X","O"


        how=(1/10)**depth
        checkend=False

            
        if e*5 in line:#剛剛下的是自己的棋，此處已經檢查過了
            if depth==0 and onlyCheck:
                gameover("win")
            pos-=1000000000 * how
            print("too bad")
            checkend=True
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
                pos-=10000000 * how
            elif endPiece==".":
                pos-=10000000 * how

            
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
                pos-=1000000 * how
            elif startPiece==".":
                pos-=10000 * how
            elif endPiece==".":
                pos-=10000 * how

            
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
                pos-=100 * how
            elif startPiece==".":
                pos-=50 * how
            elif endPiece==".":
                pos-=50 * how
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
                pos-=3 * how
                #print(pos[2])
            elif startPiece==".":
                pos-=1 * how
            elif endPiece==".":
                pos-=1 * how




                

                
        if s*5 in line:#need improving #贏了也照下
            if depth==0 and onlyCheck:
                gameover("lose")
            
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

                
            pos+=1000000000 * how
            print("too good")
            checkend=True



                
                



        

            
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
                pos+=2000 * how
            elif startPiece==".":
                pos+=500 * how
            elif endPiece==".":
                pos+=500 * how

            
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
                pos+=1000 * how
            elif startPiece==".":
                pos+=10 * how
            elif endPiece==".":
                pos+=10 * how
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
                pos+=5 * how
                #print(pos[2])
            elif startPiece==".":
                pos+=2 * how
            elif endPiece==".":
                pos+=2 * how
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
                pos+=2 * how
                #print(pos[2])
            elif startPiece==".":
                pos+=1 * how
            elif endPiece==".":
                pos+=1 * how

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
                pos-=500000 * how
                #print(pos[2])
            elif startPiece==".":
                pos-=5000 * how
            elif endPiece==".":
                pos-=5000 * how




                
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
                pos-=1000000 * how
                #print(pos[2])
            elif startPiece==".":
                pos-=10000 * how
            elif endPiece==".":
                pos-=10000 * how
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
                pos-=1000000 * how
                #print(pos[2])
            elif startPiece==".":
                pos-=10000 * how
            elif endPiece==".":
                pos-=10000 * how
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
                
            pos-=10000000 * how
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
                
            pos-=10000000 * how
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
                
            pos-=10000000 * how

        #up#########################################################################
        return pos,checkend



        
def ai(positions,who,board):
    if positions!=dict():
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
    return board 
def gameover(text):
    if text=="win":
        print("U win!!!")
    elif text=="lose":
        print("haha u lose!!!")
    elif text=="tie":
        print("the board is full!!!")
        print("LOOK WHAT U'VE DONE!!!")
    time.sleep(5)
    print("end!")
    sys.exit()


#size=9
size=setSize()
CheckDepth=4
board=[["." for i in range(size)] for i in range(size)]
printBoard(board)
while 1:
    #player
    player()
    printBoard(board)
    #test board full check code:
    #board=[["滿" for i in range(size)] for i in range(size)]
    positions=DeepCheck(1,True)
    

    #AI
    positions=DeepCheck(CheckDepth,False)
    #time.sleep(3)
    clear()
    board=ai(positions,"AI",board)
    printBoard(board)
    positions=DeepCheck(1,True)

    






