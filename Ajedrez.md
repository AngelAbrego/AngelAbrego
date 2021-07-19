"""Convenciones: las posiciones se hacen fila-columna desde la parte inferior izquierda y ambos son números.
Esto corresponde al sistema de números alfa del ajedrez tradicional, mientras que es útil desde el punto de vista computacional.
Se especifican como tuplas"""

BLANCO = "Blanco"
NEGRO = "Negro"




class Game:
    
    def __init__(self):
        self.playersturn = NEGRO
        self.message = "Aqui iran las indicaciones"
        self.gameboard = {}
        self.placePieces()
        print("programa de ajedrez. ingrese movimientos en notación algebraica separados por espacio")
        self.main()

        
    def placePieces(self):

        for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(BLANCO,uniDict[BLANCO][Pawn],1)
            self.gameboard[(i,6)] = Pawn(NEGRO,uniDict[NEGRO][Pawn],-1)
            
        placers = [Torre,Caballo,alfil,Reina,Rey,alfil,Caballo,Torre]
        
        for i in range(0,8):
            self.gameboard[(i,0)] = placers[i](BLANCO,uniDict[BLANCO][placers[i]])
            self.gameboard[((7-i),7)] = placers[i](NEGRO,uniDict[NEGRO][placers[i]])
        placers.reverse()

        
    def main(self):
        
        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startpos,endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "No se encontro la pieza;indice probablemente fuera de rango"
                target = None
                
            if target:
                print("found "+str(target))
                if target.Color != self.playersturn:
                    self.message = "no puedes mover esa pieza en este turno"
                    continue
                if target.isValid(startpos,endpos,target.Color,self.gameboard):
                    self.message = "eso es un movimiento válido"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    self.isCheck()
                    if self.playersturn == NEGRO:
                        self.playersturn = BLANCO
                    else : self.playersturn = NEGRO
                else : 
                    self.message = "Movimiento invalido" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
            else : self.message = "no hay pieza en ese espacio"
                    
    def isCheck(self):
        # averiguar dónde están los reyes, verifique todas las piezas de color opuesto contra esos reyes, luego si cualquiera de ellos recibe un golpe, verifique si es jaque mate
        king = Rey
        kingDict = {}
        pieceDict = {NEGRO : [], BLANCO : []}
        for position,piece in self.gameboard.items():
            if type(piece) == Rey:
                kingDict[piece.Color] = position
            print(piece)
            pieceDict[piece.Color].append((piece,position))
        #Blanco
        if self.canSeeKing(kingDict[BLANCO],pieceDict[NEGRO]):
            self.message = "EL jugador Blanco esta en jaque"
        if self.canSeeKing(kingDict[NEGRO],pieceDict[BLANCO]):
            self.message = "EL jugador Negro esta en jaque"
        
        
    def canSeeKing(self,kingpos,piecelist):
        #comprueba si alguna pieza en la lista de piezas (que es una matriz de (pieza, posición) tuplas) puede ver al rey en kingpos
        for piece,position in piecelist:
            if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                return True
                
    def parseInput(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return (a,b)
        except:
            print("Error la entrada de decodificación. Inténtalo de nuevo")
            return((-1,-1),(-1,-1))
    
    """def validateInput(self, *kargs):
        for arg in kargs:
            if type(arg[0]) is not type(1) or type(arg[1]) is not type(1):
                return False
        return True"""
        
    def printBoard(self):
        print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for i in range(0,8):
            print("-"*32)
            print(chr(i+97),end="|")
            for j in range(0,8):
                item = self.gameboard.get((i,j)," ")
                print(str(item)+' |', end = " ")
            print()
        print("-"*32)
            
           
        
    """clase de juego. contiene los siguientes miembros y métodos:
    dos conjuntos de piezas para cada jugador
    Matriz de 8x8 piezas con referencias a estas piezas
    una función de análisis, que convierte la entrada del usuario en una lista de dos tuplas que denotan los puntos de inicio y finalización
    una función de jaque mate Existe que comprueba si alguno de los jugadores está en jaque mate
    una función checkExists que comprueba si alguno de los jugadores está en jaque (woah, acabo de recibir ese nonsequitur)
    un bucle principal, que toma entrada, la ejecuta a través del analizador, pregunta a la pieza si el movimiento es válido y mueve la pieza si lo es. si el movimiento entra en conflicto con otra pieza, esa pieza se elimina. ischeck (mate) se ejecuta, y si hay un jaque mate, el juego imprime un mensaje sobre quién gana
    """

class Piece:
    
    def __init__(self,color,name):
        self.name = name
        self.position = None
        self.Color = color
    def isValid(self,startpos,endpos,Color,gameboard):
        if endpos in self.availableMoves(startpos[0],startpos[1],gameboard, Color = Color):
            return True
        return False
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def availableMoves(self,x,y,gameboard):
        print("ERROR, sin movimiento para la clase base")
        
    def AdNauseum(self,x,y,gameboard, Color, intervals):
        """repite el intervalo dado hasta que se topa con otra pieza.
        si esa pieza no es del mismo color, se agrega ese cuadrado y
        luego se devuelve la lista"""
        answers = []
        for xint,yint in intervals:
            xtemp,ytemp = x+xint,y+yint
            while self.isInBounds(xtemp,ytemp):
                #print(str((xtemp,ytemp))+"is in bounds")
                
                target = gameboard.get((xtemp,ytemp),None)
                if target is None: answers.append((xtemp,ytemp))
                elif target.Color != Color: 
                    answers.append((xtemp,ytemp))
                    break
                else:
                    break
                
                xtemp,ytemp = xtemp + xint,ytemp + yint
        return answers
                
    def isInBounds(self,x,y):
        "comprueba si una posición está en el tablero"
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
    
    def noConflict(self,gameboard,initialColor,x,y):
        "comprueba si una sola posición no entra en conflicto con las reglas del ajedrez"
        if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
        return False
        
    #aqui es donde iran los movimientos de cada una de las piezas

chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

def knightList(x,y,int1,int2):
    """Específicamente para la torre, permuta los valores necesarios alrededor de una posición para pruebas sin conflicto"""
    return [(x+int1,y+int2),(x-int1,y+int2),(x+int1,y-int2),(x-int1,y-int2),(x+int2,y+int1),(x-int2,y+int1),(x+int2,y-int1),(x-int2,y-int1)]
def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]
 


class Caballo(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in knightList(x,y,2,1) if self.noConflict(gameboard, Color, xx, yy)]
        
class Torre(Piece):
    def availableMoves(self,x,y,gameboard ,Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)
        
class alfil(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)
        
class Reina(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals+chessDiagonals)
        
class Rey(Piece):
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return [(xx,yy) for xx,yy in kingList(x,y) if self.noConflict(gameboard, Color, xx, yy)]
        
class Pawn(Piece):
    def __init__(self,color,name,direction):
        self.name = name
        self.Color = color
        #por supuesto, la pieza más pequeña es la más difícil de codificar. la dirección debe ser 1 o -1, debe ser -1 si el peón viaja "hacia atrás"
        self.direction = direction
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        answers = []
        if (x+1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction) : answers.append((x+1,y+self.direction))
        if (x-1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction) : answers.append((x-1,y+self.direction))
        if (x,y+self.direction) not in gameboard and Color == self.Color : answers.append((x,y+self.direction))# la condición es asegurarse de que el movimiento de no captura(el unico que no hace mucho en el juego) no se utiliza en el cálculo del jaque mate
        return answers

uniDict = {BLANCO : {Pawn : "♙", Torre : "♖", Caballo : "♘", alfil : "♗", Rey : "♔", Reina : "♕" }, NEGRO : {Pawn : "♟", Torre : "♜", Caballo : "♞", alfil : "♝", Rey : "♚", Reina : "♛" }}
        

        


Game()
