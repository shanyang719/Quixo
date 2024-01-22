

import random
import math
import numpy as np
import copy

def check_move(board, turn, index, push_from):
    
    size=int(math.sqrt(len(board)))
    nboard=np.array(board).reshape(size,size)
    #converts list to matrix
    top_row=range(0,size)
    bottom_row=range(size*(size-1),size*size)
    
    row = int(index/size)
    col =index-row*size
    
    
    if (index+1)%size!=0 and index not in top_row and index not in bottom_row and index%size!=0:
        #choosing index not from the edge of board
        return False
    
    elif nboard[row][col]==2 and turn==1:
        #player turn but touching opponents piece      
        return False
    
    elif nboard[row][col]==1 and turn==2:
        #opponents turn but touching player's piece
        return False
     
    elif index==0 and push_from!='R' and push_from!='r' and push_from!='B' and push_from!='b':
    #index is in top left corner and invalid push
        return False
    
    elif index==size-1 and push_from!='L' and push_from!='l' and push_from!='B' and push_from!='b':
    #index is in top right corner and invalid push
        return False
    elif index==size*(size-1) and push_from!='R' and push_from!='r' and push_from!='T' and push_from!='t':
    #index is in bottom left corner and invalid push
        return False
    
    elif index==(size*size)-1 and push_from!='L' and push_from!='l' and push_from!='T' and push_from!='t':
    #index is in bottom right corner and invalid push
        return False
    
    elif index%size!=0 and (index+1)%size!=0 and index not in bottom_row and push_from!='L' and push_from!='l' and push_from!='R' and push_from!='r' and push_from!='B' and push_from!='b':
   # top row index is not in first or last column and invalid push
        return False 
   
    elif index%size!=0 and (index+1)%size!=0 and index not in top_row and push_from!='L' and push_from!='l' and push_from!='R' and push_from!='r' and push_from!='T' and push_from!='t':
   # bottom row index is not in first or last column and invalid push
        return False
    
    elif index not in bottom_row and index not in top_row and (index+1)%size!=0 and push_from!='T' and push_from!='t' and push_from!='B' and push_from!='b' and push_from!='R' and push_from!='r':
    #left column index is not in bottom or top row and invalid push
        return False
    
    elif index not in bottom_row and index not in top_row and index%size!=0 and push_from!='T' and push_from!='t' and push_from!='B' and push_from!='b' and push_from!='L' and push_from!='l':
    #right column index is not in bottom or top row and invalid push
        return False
    
    else:
        
        return True
    board = [item for sublist in nboard for item in sublist]    
    #converts matrix to list
        

def apply_move(board, turn, index, push_from):
    size=int(math.sqrt(len(board)))
    nboard=np.array(board).reshape(size,size)
    #convert list to matrix
    #apply move and return updated board
    row = int(index/size)
    col =index-row*size
    if turn%2==0:
        turn=2
    else:
        turn=1

    while push_from=='T':
        #shift every index in the particular col down
        while row>0:
            nboard[row][col]=nboard[row-1][col]
            row-=1
        
        nboard[0][col]=turn
        board = nboard
        break 
        
    while push_from=='B':
        #shift every index in the particular col up
        while row<(size-1):
            nboard[row][col]=nboard[row+1][col]
            row+=1 
            
        nboard[size-1][col]=turn
        board = nboard
        break
    
    while push_from=='L':
        #shift every index in the particular row right
        while col>0:
            nboard[row][col]=nboard[row][col-1]
            col-=1
            
        nboard[row][0]=turn
        board = nboard
        break
    
    while push_from=='R':
                #shift every index in the particular row left

        while col<(size-1):
            nboard[row][col]=nboard[row][col+1]
            col+=1
        
        nboard[row][size-1]=turn
        board = nboard
        break 
    

    
    
    board = [item for sublist in nboard for item in sublist]
    #convert matrix to list
    
    return board
    return nboard
   


def check_victory(board,who_played):
    
    size=int(math.sqrt(len(board)))
    nboard=np.array(board).reshape(size,size)
    diag = [nboard[r][r] for r in range(size)]
    rdiag = [nboard[r][size-1-r] for r in range(size)]
    returnlist = []

    
    
    for i in range(size):
        if np.array(nboard[i].all() ==1) and (2 not in nboard[i]):
            # print("Congrats! Player 1 won! Horizontal")

            returnlist.append("a") #Appends the letter 'a' to the list if winning condition for player 1 is met

        if np.array(nboard[:,i].all() == 1) and(2 not in nboard[:,i]):
            # print("Congrats! Player 1 won! Vertical")

            returnlist.append("a") #Appends the letter 'a' to the list if winning condition for player 1 is met
           
        if (all(diag) == 1) and (2 not in diag):
            # print("Congrats! Player 1 won! Diagonal")

             returnlist.append("a") #Appends the letter 'a' to the list if winning condition for player 1 is met
            
        if (all(rdiag) == 1) and (2 not in rdiag):
            # print("Congrats! Player 1 won! Reverse Diagonal")

             returnlist.append("a") #Appends the letter 'a' to the list if winning condition for player 1 is met
          
        if (all(diag) == 1) and (1 not in diag):
            # print("Congrats! Player 2 won! Diagonal")

             returnlist.append("b") #Appends the letter 'b' to the list if winning condition for player 2 is met
            
        if (all(rdiag) == 1) and (1 not in rdiag):
            # print("Congrats! Player 2 won! Reverse Diagonal")

            returnlist.append("b") #Appends the letter 'b' to the list if winning condition for player 2 is met
            
        if np.array(nboard[i].all() ==1) and (1 not in nboard[i]):
            # print("Congrats! Player 2 won! Horizontal")

            returnlist.append("b") #Appends the letter 'b' to the list if winning condition for player 2 is met
         
        if np.array(nboard[:,i].all() == 1) and(1 not in nboard[:,i]):
            # print("Congrats! Player 2 won! Vertical")
            returnlist.append("b") #Appends the letter 'b' to the list if winning condition for player 2 is met

    if 'a' in returnlist and 'b' not in returnlist:
        return 1 #player 1 wins
    elif 'b' in returnlist and 'a' not in returnlist:
        return 2 #player 2 wins
    elif 'a' in returnlist and 'b' in returnlist: #If the winning condition for both players are met, the player who played the move loses
        if who_played == 1:
            return 2
        elif who_played == 2:
            return 1
    

    else:
        return 0
        
        

    board = [item for sublist in nboard for item in sublist]
        
       

def computer_move(board, turn, level):
    # implement your function here
    if turn==1:
        who_played=1
    else:
        who_played=2
    size = int(math.sqrt(len(board)))
    pushlist = ["L","B","R","T"]
    indexlist = range(0,size**2)
    while level == 1:
        index = random.choice(indexlist)
        push_from = random.choice(pushlist)
        if check_move(board, turn, index, push_from)==True:

            return (index, push_from)
    
        
    while level==2:
        A=False
        B=False
       
        for rindex in indexlist:
            #check all indexes
            for rpush_from in pushlist:
                #check all push directions
                clone=copy.deepcopy(board)
                #make a copy so that real board isnt affected by 'experiments'
                
                
                checking= check_move(clone,who_played,rindex,rpush_from)
                if checking== True:
                    clone = apply_move(clone,who_played,rindex,rpush_from)   
                    win = check_victory(clone,who_played) 
                    if win==who_played:
                        # index=rindex
                        # push_from=rpush_from
                        A=True
                        
                        return (rindex,rpush_from)
                   
                    
                    #this part only makes an immediate win move for comp. does not avoid immediate loss
        for rindex in indexlist:
            #check all indexes
            for rpush_from in pushlist:
                l=[]
                #check all push directions
                clone=copy.deepcopy(board)
                #make a copy so that real board isnt affected by 'experiments'
                if who_played%2==0:
                    player=1
                else:
                    player=2
                checking = check_move(clone,who_played,rindex,rpush_from)
                if checking == True:
                    rclone = apply_move(clone,who_played,rindex,rpush_from)
                    for humindex in indexlist:
                        for humpush_from in pushlist:
                            if check_move(rclone,player,humindex,humpush_from)==True:
                                humclone=apply_move(rclone,player,humindex,humpush_from)
                                if check_victory(humclone,player)==player:
                                    l.append(humindex)
                if len(l)==0 and check_move(clone,who_played,rindex,rpush_from)==True:
                    B=True
                    
                    return (rindex,rpush_from)
                
                                    
        if A!=True and B!=True:
            index = random.choice(indexlist)
            push_from = random.choice(pushlist)
            if check_move(board, turn, index, push_from)==True:
               

                return (index, push_from)
            

def display_board(board):
    # implement your function here
    
    size=int(math.sqrt(len(board)))
    nboard=np.array(board).reshape(size,size)
    print(nboard)
    
    
def menu():
    # implement your function here
    turn=1
    
    while True:
        #loop for size
        #ask player for board size
        size=input('What size board would you like? Choose a number greater than 2: ')
        
        if size.isdigit()==False:
            print('Choose a positive number.')
            continue
        else:
            size=int(size)
            board=[0]*(size**2)
    
            if size>2:
                display_board(board)
                while True:
                    #loop for player1/player2
                    player=input("Do you want to be Player 1 or Player 2?\nPlayer 1 goes first\nEnter your input:")
                    if player.isdigit()==False:
                        print("Enter a valid digit.")
                        continue
                    elif int(player)>=3 or int(player)<=0:
                        print("Enter 1 or 2.")
                        continue
                    else:
                        player = int(player)
                        while True:   
                            #loop for human/computer
                            print("Who do you want to play with?")
                            print("1. Human")
                            print("2. Computer")
                            opponent = input("Enter your input: ")
                            print()
                            if opponent.isdigit() == False:
                                print("Error. Please input a valid input.")
                                print()
                                continue
                            else:
                                opponent=int(opponent)
                                if opponent == 1:
                                    print("You are about to play againist another human.")
                                    break
                                elif opponent == 2:
                                    
                                    
                                    while True:  
                                        #loop for level
                                        level = input("Select the difficulty level (1,2): ")
                                        
                                        if level.isdigit() == False:
                                            print("Error. Please input a valid difficulty level.")
                                            print()
                                            continue
                                        else:
                                            level=int(level)
                                            if level == 1:
                                                print("Difficulty 1 is selected")
                                                break
                                            elif level == 2:
                                                print("Difficulty 2 is selected")
                                                break
                                            else:
                                                print("Error. Please input a valid difficulty level.")
                                                print()
                                                continue
                                        break
                                    break
                                else:
                                    print("Error. Please input a valid input.")
                                    print()
                                    continue
                    break            
            else:
                print("Choose a number greater than 2")
                continue
            break
    
    #Ask player for index
    print()
    print('TYPE EXIT AT ANY TIME TO END THE GAME')   #Able to exit at any point of time after choosing difficulty level of bot or while playing with human
    print()
    while True:
       index_range=range(0,size**2)
       if turn%2==0:
           turn=2
       else:
           turn==1
       if turn==1:
           who_played=1
       else:
           who_played=2
       print()
       print('************ Player', who_played,'************')
       
       display=np.arange(size**2).reshape((size, size))
       print('Blocks are arranged as such:')
       print(display)
       print()
       if who_played == player or opponent == 1:
           index=input("Which block do you want to move? Choose an integer: ")
           if index==str('exit') or index==str('Exit'):
               print('GAME OVER')
               return
           elif index.isdigit()==False:
               print("'",index,"'","is not an integer. \nPlease select a valid integer.")
               continue
          
           else:
               index=int(index)
               push_from=input('Choose a valid push direction, Top, Bottom, Left, or Right! Enter T,B,L or R.').upper()
               if push_from==str('EXIT'):
                   print('GAME OVER')
                   return
                  
       else:
           index, push_from = computer_move(board, turn, level)
           print("Opponent selected index", index,"pushing from", push_from,".\n")
           
       if index not in index_range:
           print('Choose an integer on the edge')
           
           continue
       else:
           checking = check_move(board, turn, index, push_from)
           if checking==True:
               print('valid!')
               apply_move(board, turn, index, push_from)
               print("[board returned, displaying]")
               
               board=apply_move(board, turn, index, push_from)
               check_victory(board,who_played)
               display_board(board)
               victory=check_victory(board,who_played)
             
               if victory==1 and victory!=2:
                   print('Congrats! Player 1 won!')
                   return
               elif victory==1 and victory==2 and who_played ==1:
                   print('Congrats! Player 2 won!')
                   return
               elif victory==2 and victory!=1:
                   print('Congrats! Player 2 won!')
                   return
               elif victory==1 and victory==2 and who_played ==2:
                   print('Congrats! Player 1 won!')
                   return
                   
              
               turn+=1
               if turn%2==0:
                   turn=2
               else:
                   turn=1
             
           else:
               print()
               print('Invalid entry. Choose a valid block and push direction.')
               continue
          
     
if __name__ == "__main__":
    menu()
  