import time
import sys
import colored
#印出棋盤
def printBoard(board,width):
    print("\t",end="")
    for i in range(size):
        print(str(i+1),end=" "*(width-(len(str(i+1))-1)))
    print("\n")#換兩行==print()print()
    for rowNum in range(size):
        print(str(rowNum+1),end="\t")
        for pieceNum in range(size):
            piece=board[rowNum][pieceNum]
            if piece=="O":
                THISfcolor=colored.fg("green")
            elif piece=="X":
                THISfcolor=colored.fg("red_1")
            elif piece==".":
                THISfcolor=fcolor
            print(THISfcolor+bcolor+piece+reset,end="")
            if not pieceNum==size-1: #不是最後一個旗子
                print(fcolor+bcolor+" " * width+reset,end="")
        print()

        #print(fcolor+bcolor+(" "*width).join(board[rowNum])+reset)

        print("\t"+fcolor+bcolor+" "*(width*(size-1)+size)+reset)
#設定棋盤大小
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
#清空畫面(感謝徐晧倫)
def clear():
    for i in range(100):
        print()
#玩家下棋
def player():
    print("plz enter ur pos.")
    while True:
        a=input()
        if a.find(" ")==-1 or len(a) > 5:
            print("wrong!!")
            continue
        try:
            x,y = [int(i)-1 for i in a.split()]
        except ValueError:
            print("not num!")
            continue
        #x,y=====0~size-1
        if x<0 or y<0 or x>size-1 or y>size-1:
            print("UR WEIRD NUM NOT ALLOWED!!!")
            continue
        if not checkNoPiece(y,x):
            print("There is already a piece.")
            continue
        break
    board[y][x]="O"
#檢查是否下在沒棋子之處
def checkNoPiece(y,x):
    return board[y][x]=="."
#檢查棋盤是否已滿
def checkBoardFull(board):
    isFull = True
    for row in board:
        for piece in row:
            if piece==".":
                isFull=False
    return isFull
#以minimax搜索最佳下棋位置
def DeepCheck(checkDepth,onlyCheck):
    
    if checkBoardFull(board):
        gameover("tie")

    positionsss=dict()
    depth=0
    newBoard=[[i for i in row] for row in board]
    positionsss=AllCheck("AI",depth,newBoard,checkDepth,onlyCheck,0,False)
    return positionsss
#檢查一層的所有可下棋位置
def AllCheck(who,depth,newBoard,checkDepth,onlyCheck,alpha,checkAplhaBeta):
    cut=False
    beta="no"
    positions=dict()
    #所有可下棋位置
    for y in range(size):
        for x in range(size):
            if newBoard[y][x]==".":
                #計算下在各格的分數
                score=check(x,y,positions,who,depth,checkDepth,newBoard,onlyCheck,beta,beta!="no")
                #存入dictionary
                positions[score]=(y,x)
                #存較大層之最大or最小分數
                if who=="AI":
                    beta=max(positions.keys())
                elif who=="playerAI":
                    beta=min(positions.keys())
                #alpha-beta剪枝
                if checkAplhaBeta:
                    if who=="AI" and beta>alpha and checkAplhaBeta:
                        cut=True
                        break
                    elif who=="playerAI" and beta<alpha and checkAplhaBeta:
                        cut=True
                        break
        if cut:
            break
    #回傳總分
    if depth==0:
        #print(positions)
        return positions
    else:
        #回傳各層最大or最小分數
        if positions!=dict():
            if who=="playerAI":
                return min(positions.keys())
            if who=="AI":
                return max(positions.keys())
        return 0
#檢查各格分數
def check(x,y,positions,who,depth,checkDepth,newBoard,onlyCheck,beta,checkAplhaBeta):
    end=False
    #試著下一顆棋
    aWholeNewBoard=[[i for i in row]for row in newBoard]
    if not onlyCheck:
        if who=="playerAI":
            aWholeNewBoard[y][x]="O"
        elif who=="AI":
            aWholeNewBoard[y][x]="X"
    #計算直排、橫排、斜排分數
    pos=0
    pos,end1=vertical(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end2=horizontal(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end3=slideUP(aWholeNewBoard,pos,who,depth,onlyCheck)
    pos,end4=slideDOWN(aWholeNewBoard,pos,who,depth,onlyCheck)
    #是否下滿
    if end1 or end2 or end3 or end4:
        end=True
    #遞迴
    if who=="playerAI":
        if end or checkBoardFull(aWholeNewBoard) or depth+1>=checkDepth:
            return pos
        else:
            return AllCheck("AI",depth+1,aWholeNewBoard,checkDepth,onlyCheck,beta,checkAplhaBeta)
    elif who=="AI":
        if end or checkBoardFull(aWholeNewBoard) or depth+1>=checkDepth:
            return pos
        else:
            return AllCheck("playerAI",depth+1,aWholeNewBoard,checkDepth,onlyCheck,beta,checkAplhaBeta)

#直排
def vertical(b,pos,who,depth,onlyCheck):
    for x in range(size):
        line = [b[y][x] for y in range(size)]
        piecePos=[(y,x) for y in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")

        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
#橫排
def horizontal(b,pos,who,depth,onlyCheck):
    for y in range(size):
        line = [b[y][x] for x in range(size)]
        piecePos=[(y,x) for x in range(size)]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")

        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
#斜排
def slideUP(b,pos,who,depth,onlyCheck):
    for k in range(0+4,(size*2-1)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x+y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x+y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")
     
        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
#斜排
def slideDOWN(b,pos,who,depth,onlyCheck):
    for k in range((-(size-1))+4,(size)-4):
        line = [b[y][x] for x in range(size) for y in range(size) if x-y==k]
        piecePos=[(y,x) for x in range(size) for y in range(size) if x-y==k]
        try:
            line = "".join(line)
        except:
            print("sdszdsd")

        pos,end=analyze(line,b,piecePos,pos,who,depth,onlyCheck)
    return pos,end
#分析情勢再加減分數
def analyze(line,b,piecePos,pos,who,depth,onlyCheck):
        #playerAI = O   AI = X
        

        s,e="X","O"


        how=(1/10)**depth#越下層之分數越接近0，較不會影響總分
        checkend=False

        #判斷情勢
        if e*5 in line:
            if depth==0 and onlyCheck:
                gameover("win")#玩家贏了
            pos-=10000000000 * how
            print("too bad")
            checkend=True
        if e*4 in line:
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

                
            if startPiece=="." or endPiece==".":
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
            elif startPiece=="." or endPiece==".":
                pos-=5000 * how

            
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
            elif startPiece=="." or endPiece==".":
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
            elif startPiece==".":
                pos-=1 * how
            elif endPiece==".":
                pos-=1 * how



        if s*5 in line:
            if depth==0 and onlyCheck:
                gameover("lose")#AI贏了
            pos+=10000000000 * how
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
                pos+=10000000 * how
            elif startPiece=="." or endPiece==".":
                pos+=5000 * how

            
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
            elif startPiece=="." or endPiece==".":
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
            elif startPiece=="." or endPiece==".":
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
            elif startPiece=="." or endPiece==".":
                pos+=1 * how




        if e+"."+e in line:
            start=line.find(e+"."+e)-1
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
                pos-=500000 * how
            elif startPiece==".":
                pos-=5000 * how
            elif endPiece==".":
                pos-=5000 * how




                
        if e+e+"."+e in line:
            start=line.find(e+e+"."+e)-1
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
                pos-=1000000 * how
            elif startPiece==".":
                pos-=10000 * how
            elif endPiece==".":
                pos-=10000 * how
        if e+"."+e+e in line:
            start=line.find(e+"."+e+e)-1
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
                pos-=1000000 * how
            elif startPiece==".":
                pos-=10000 * how
            elif endPiece==".":
                pos-=10000 * how
        if e+e+"."+e+e in line:

                
            pos-=10000000 * how
        if e+e+e+"."+e in line:
                
            pos-=10000000 * how
        if e+"."+e+e+e in line:

                
            pos-=10000000 * how




        return pos,checkend
#AI下棋
def ai(positions,board):
    if positions!=dict():
        besty,bestx=positions[max(positions.keys())]

        board[besty][bestx]="X"

    else:
        print("the AI of this game is too stupid to decide where to place its pawn.")
        print("So it's time for u to defeat it.")
    return board
#遊戲結束
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
    sys.exit()#end script


#初始化
size=setSize()
CheckDepth=1

board=[["." for i in range(size)] for i in range(size)]
boardWidth=3
fcolor=colored.fg("black")
bcolor=colored.bg("white")
reset=colored.attr("reset")
boardSpaceAmount=size**2
print(f"boardSpaceAmount:{boardSpaceAmount}")
printBoard(board,boardWidth)
#循環進行遊戲
while 1:
    #玩家下棋
    player()
    boardSpaceAmount-=1
    printBoard(board,boardWidth)
    positions=DeepCheck(1,True)
    

    
    #訂定AI搜尋深度
    CheckDepth=int(-0.05 * boardSpaceAmount +7)#or+6
    if CheckDepth<1:
    	CheckDepth=1
    print(f"CheckDepth : {CheckDepth}")
    #AI下棋
    print("loading...")
    positions=DeepCheck(CheckDepth,False)
    clear()
    board=ai(positions,board)
    boardSpaceAmount-=1
    printBoard(board,boardWidth)
    positions=DeepCheck(1,True)
