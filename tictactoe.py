import random

def game_1():
    pos=[0,1,2,3,4,5,6,7,8]
    def gameboard():
        print('''
                |      |    
             {}  |   {}  |   {}
                |      |   
         ----------------------
                |      |    
             {}  |   {}  |   {}
                |      |    
         ----------------------
                |      |    
             {}  |   {}  |   {}
                |      |    
         
         '''.format(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8]))

    def winner(char, pos1, pos2, pos3):
        if pos[pos1] == char and pos[pos2] == char and pos[pos3] == char:
                return True

    def check_condition(char):
            if winner(char, 0, 1, 2):
                return True
            elif winner(char, 3, 4, 5):
                return True
            elif winner(char, 6, 7, 8):
                return True
            elif winner(char, 1, 4, 7):
                return True
            elif winner(char, 2, 5, 8):
                return True
            elif winner(char, 0, 4, 8):
                return True
            elif winner(char, 2, 4, 6):
                return True

    preoccupied = []
    def isboardfull():
        if len(preoccupied)==9:
            return True

    def playagain():
        uj = input('DO YOU WANT TO PLAY AGAIN:{yes or no}:')
        if uj=='yes:':
            #print('sorry')
            game_1()

        else:
            if uj=='no':
                print('thankyou!')
                exit()

    def game():
        print("************Welcome to TIC TAC TOE ***********")
        userchoice=input('SO YOU WANT TO BE X OR O: ')
        cpuchoice=''
        if userchoice == 'X':
            cpuchoice='O'
        elif userchoice == 'O':
            cpuchoice ='X'
        print('Userchoice:',userchoice,'CPUChoice:',cpuchoice)
        #turn=goesfirst()
        while True:
            #if turn=='PLAYER YOUR CHANCE!':
                gameboard()
                userposition=int(input('ENTER YOUR POSITION:'))
                if userposition in preoccupied:
                    print('Oops!This position is occupied')
                    continue
                pos[userposition]=userchoice
                preoccupied.append(userposition)
                #print(preoccupied)
                if check_condition(userchoice) == True:
                    gameboard()
                    print("***********Hurray!!YOU WON *********")
                    playagain()
                    break

                while True:
                    cpuposition =random.randint(0,8)
                    if cpuposition in preoccupied:
                        print('Oops CPU !The position ',cpuposition,'is occupied,choose another!')
                        continue
                    else:
                         pos[cpuposition] = cpuchoice
                         preoccupied.append(cpuposition)
                         print(preoccupied)
                         if check_condition(cpuchoice) == True:
                             gameboard()
                             print("******Ohhhh!!CPU WINS *****")
                             playagain()
                             break
                if isboardfull() == True:
                        print('Game is a tie')
                        playagain()
                        break
    game()

game_1()