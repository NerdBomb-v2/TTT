from random import choice
class TTT:
    def __init__(self) -> None:
        self.table=[[None,None,None],[None,None,None],[None,None,None]]
        self.move=0
        self.ai_def_num = None
        self.winner = None
        self.Ai_move=False
        self.ai_choice=[None,None]
    @property
    def row1(self):
        return self.table[0]
    @property
    def row2(self):
        return self.table[1]
    @property
    def row3(self):
        return self.table[2]
    @property
    def col1(self):
        return list(row[0] for row in self.table)
    @property
    def col2(self):
        return list(row[1] for row in self.table)
    @property
    def col3(self):
        return list(row[2] for row in self.table)
    @property
    def d1(self):
        return [self.table[0][0],self.table[1][1],self.table[2][2]]
    @property
    def d2(self):
        return [self.table[0][2],self.table[1][1],self.table[2][0]]
    
    def corner(self,player):
        corners = [self.table[0][0],self.table[0][2],self.table[2][0],self.table[2][2]]
        middles = [self.table[0][1],self.table[1][0],self.table[1][2],self.table[2][1]]
        if (corners.count(None)>=2) and ((corners[0]!=corners[3] or corners[1]!=corners[2])or(corners.count(None)==4)):
            if corners[0]==None:
                if player=='O':
                    self.set_tick(1,1)
                elif player=='X':
                  self.set_cross(1,1)
            elif corners[1]==None:
                if player=='O':
                    self.set_tick(1,3)
                elif player=='X':
                  self.set_cross(1,3)
            elif corners[2]==None:
                if player=='O':
                    self.set_tick(3,1)
                elif player=='X':
                  self.set_cross(3,1)
            elif corners[3]==None:
                if player=='O':
                    self.set_tick(3,3)
                elif player=='X':
                  self.set_cross(3,3)
            return True
        elif (corners.count(None)<=2):
             if middles[0]==None:
                if player=='O':
                    self.set_tick(1,2)
                elif player=='X':
                  self.set_cross(1,2)
             elif middles[1]==None:
                if player=='O':
                    self.set_tick(2,1)
                elif player=='X':
                  self.set_cross(2,1)
             elif middles[2]==None:
                if player=='O':
                    self.set_tick(2,3)
                elif player=='X':
                  self.set_cross(2,3)
             elif middles[3]==None:
                if player=='O':
                    self.set_tick(3,2)
                elif player=='X':
                  self.set_cross(3,2)
             return True
        else:
            return False
    
    def ttt_seq(self,x):
        if (x[0] == x[1] == x[2]) and (x[0]!=None):
            self.winner = x[0]
            return (x[0] == x[1] == x[2]) and (x[0]!=None)
        
    def reset(self):
        self.table=[[None,None,None],[None,None,None],[None,None,None]]

    def def_seq(self,x):
        try:
            if (x.count(True)==2) or (x.count(False)==2) and (x.count(None)==1):
                self.ai_def_num = x.index(None)
                return True
            else:
                return None
        except:
            return None
    def defend_row(self,player):
        if self.def_seq(self.row1):
            if player=='O':
                self.set_tick(1,self.ai_def_num+1)
            elif player=='X':
                self.set_cross(1,self.ai_def_num+1)
            return True
        elif self.def_seq(self.row2):
            if player=='O':
                self.set_tick(2,self.ai_def_num+1)
            elif player=='X':
                self.set_cross(2,self.ai_def_num+1)
            return True
        elif self.def_seq(self.row3):
            if player=='O':
                self.set_tick(3,self.ai_def_num+1)
            elif player=='X':
                self.set_cross(3,self.ai_def_num+1)
            return True
    def defend_col(self,player):
        if self.def_seq(self.col1):
            if player=='O':
                self.set_tick(self.ai_def_num+1,1)
            elif player=='X':
                self.set_cross(self.ai_def_num+1,1)
            return True
        elif self.def_seq(self.col2):
            if player=='O':
                self.set_tick(self.ai_def_num+1,2)
            elif player=='X':
                self.set_cross(self.ai_def_num+1,2)
            return True
        elif self.def_seq(self.col3):
            if player=='O':
                self.set_tick(self.ai_def_num+1,3)
            elif player=='X':
                self.set_cross(self.ai_def_num+1,3)
            return True
    def defend_dg(self,player):
        if self.def_seq(self.d1):
            if player=='O':
                self.set_tick(self.ai_def_num+1,self.ai_def_num+1)
            elif player=='X':
                self.set_cross(self.ai_def_num+1,self.ai_def_num+1)
            return True
        elif self.def_seq(self.d2):
            if self.ai_def_num==0:
                b=2
            if self.ai_def_num==1:
                b=1
            if self.ai_def_num==2:
                b=0
            if player=='O':
                self.set_tick(self.ai_def_num+1,b+1)
            elif player=='X':
                self.set_cross(self.ai_def_num+1,b+1)
            return True

    def rand_move(self,player):
        while ((None in self.table[0]) or (None in self.table[1]) or (None in self.table[2])):
            x = choice([1,2,3])
            y = choice([1,2,3])
            if self.table[x-1][y-1]==None:
                if player=='O':
                    self.set_tick(x,y)
                elif  player=='X':
                    self.set_cross(x,y)
                break
        
    def ai_move(self,Player):
        self.Ai_move=True
        if not (self.defend_row(Player) or self.defend_col(Player) or self.defend_dg(Player)): 
            if self.table[1][1]==None:
                if Player=='O':
                    self.set_tick(2,2)
                elif Player=='X':
                  self.set_cross(2,2)
            elif self.corner(Player):
                pass
            else:
                self.rand_move(Player)
            
    def check_straight(self):
        return self.ttt_seq(self.row1) or self.ttt_seq(self.row2) or self.ttt_seq(self.row3) or self.ttt_seq(self.col1) or self.ttt_seq(self.col2) or self.ttt_seq(self.col3)
    
    def check_diagonal(self):
        return self.ttt_seq(self.d1) or self.ttt_seq(self.d2)
            
    
    def check(self)-> bool:
        return self.check_diagonal() or self.check_straight()

    def check_pos(self,row,col):
        if (0<=row<=2) and (0<=col<=2) and self.table[row][col]==None:
            return True
        else:
            return False
    
    def set_cross(self,row,col):
        if self.winner==None:
            if self.check_pos(row-1,col-1):
                self.table[row-1][col-1]=False
                self.move+=1
                if self.Ai_move==True:
                    print(row,col)
                    self.ai_choice=[row,col]
                    self.Ai_move=False
                self.check_straight()
                self.check_diagonal()
                return True
            else:
                print('Wrong input',row,col)
                return False
        else:
            print("can't play more the winner is -",self.winner)
    def set_tick(self,row,col):
        if self.winner==None:
            if self.check_pos(row-1,col-1):
                self.table[row-1][col-1]=True
                self.move+=1
                if self.Ai_move==True:
                    print(row,col)
                    self.ai_choice=[row,col]
                    self.Ai_move=False
                self.check_straight()
                self.check_diagonal()
                return True
            else:
                print('Wrong input',row,col)
                return False
        else:
            print("can't play more the winner is -",self.winner)
    def __str__(self) -> str:
        res='  1___2___3 \n'
        res+= f'1|{str(self.table[0][0]):<5}  {str(self.table[0][1]):^5} {str(self.table[0][2]):>5}|\n'
        res+=' |_________|\n'
        res+=f'2|{str(self.table[1][0]):<5}  {str(self.table[1][1]):^5} {str(self.table[1][2]):>5}|\n'
        res+=' |_________|\n'
        res+=f'3|{str(self.table[2][0]):<5}  {str(self.table[2][1]):^5} {str(self.table[2][2]):>5}|\n'
        res+=' |_________|\n'
        res=res.replace('True','O')
        res=res.replace('False',' X')
        res=res.replace('None','.')
        return res
def play():
    game =TTT()
    print(game)
    Player1 = choice(['O','X']); Player2 = ['O','X']; Player2.remove(Player1); Player2 = Player2[0]
    while True:
        if ((None in game.row1) or (None in game.row2) or (None in game.row3)) and game.winner==None:
            try:
                pos= list(map(int, input(' Player1, Enter the row and column , u wanna place your marker(e.g: 2 2) - ').split()))
                if Player1=='O':
                    try:
                        game.set_tick(pos[0],pos[1])
                    except:print('Wrong input :(')
                    print(game)
                elif Player1=='X':
                    try:
                        game.set_cross(pos[0],pos[1])
                    except:print('Wrong input :(')
                    print(game)
                if ((None in game.row1) or (None in game.row2) or (None in game.row3)) and game.winner==None:
                    print('Player2, Enter the row and column , u wanna place your marker(e.g: 2 2) - ',end='')
                    if Player2=='O':
                        game.ai_move(Player2)
                    elif Player2=='X':
                        game.ai_move(Player2)
                    print(game)
            except: print('''
I mean like dont take it seriouly,
but u suck and just spoiled my hardwork,
you have extra super foolish sucking brain which is kinda useless,
I am just sorry, i think i have taken drugs so dont worry about all these words about you :) and move on.
The format is (row no.)(space)(column no.) then enter , pls dont leave the input blank.
''')
        else:
            if game.winner==True:
                print('Zero Won this game :) !')
            elif game.winner==False:
                print('Cross Won this game :) !')
            else:
                print('Noone Won this game :) !')
            game.reset()
            game.winner=None

            cont = input('wanna continue(y/n)?').lower()
            if cont=='y':
                print(game)
            elif cont=='n':
                break
            else:
                print('wrong input!')
                break
if __name__=='__main__':
    play()
